"""Create a traceability matrix between requirements and tests from Doorstop items."""
import doorstop
import rapidtables
import csv
import fire
import pandas as pd
import numpy as np
import subprocess
from pathlib import Path

fieldnames = ["UID", "Name", "Verification Plan", "Method", "Phase", "Status"]


def rtm_builder(
    prefix: str, root: str = None, sort_key: str = None, path: str = None,
) -> str:
    """Generate a traceability matrix, and output to either stdout or csv.

    Args:
        prefix: The prefix for Doorstop requirements.
        root: The root path to search for Doorstop documents.
        sort_key: If the RTM should be sorted, sort by this key.
            Should be one of 'UID', 'Has Test', 'Tests', or None. Defaults to None.
        path: If the RTM should be written to file, write to this path.
            If omitted, the RTM will be returned. Defaults to None.
    """
    tree = doorstop.build(root=root)
    reqs_doc = tree.find_document(prefix)
    csv_path = path.replace(".md", ".csv").replace(".markdown", ".csv")

    # Run doorstop export command to generate doorstop csv file (if it does not exist)
    directory = Path(csv_path)
    if directory.exists():
        print("Requirement csv files already exist. Skipping doorstop export command process...")
    else:
        export_cmd = "doorstop export " + prefix + " " + csv_path
        subprocess.run(export_cmd, shell=True)

    # NOTE: If labels for the table_data are edited, change the fieldnames variable as well
    table_data = [
        {
            "UID": str(item), # Requirement UID
            "Name": item.short_name, # Requirement name
            #"Text": item.text, # Requirement shall statement
            "Verification Plan": item.verification_plan, # Link to Verification Plan
            "Method": item.verification_methods, # Test Methods for verification (ex. Test, Inspection, Analysis, Demonstration)
            "Phase": item.phase, # Phase verification is performed
            "Status": item.status, # Status of verification of requirement (ex. Coming soon)
        }
        for item in reqs_doc.items
    ]

    if sort_key:
        table_data = sorted(table_data, key=lambda x: x[sort_key])

    table = rapidtables.make_table(table_data, tablefmt="md")

    if path:
        with open(csv_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in table_data:
                writer.writerow(row)
        if path.endswith(".md") or path.endswith(".markdown"):
            df = pd.read_csv(csv_path)
            df = df.replace(np.nan, "")
            with open(path, 'w') as md:
                df.to_markdown(buf=md)
        return f"Successfully wrote requirement verification matrix (RVM) to {path}"
    else:
        return table


def main():
    """Entry point."""
    fire.Fire(rtm_builder)


if __name__ == "__main__":
    main()
