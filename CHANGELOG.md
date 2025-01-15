# Change Log

_Reference log of changes done to the original rtm_doorstop version._ 

**MODIFIED for generating an RVM instead with doorstop for requirements.**
_Version 1.1.1 of [rtm_doorstop](https://github.com/asimon-1/rtm_doorstop) used as a base._

## Contents
- [Change Log](#change-log)
  - [Contents](#contents)
  - [Edits Overview](#edits-overview)
  - [Command Adjustments](#command-adjustments)

----------------

## Edits Overview
_List of changes / feature additions to `rtm_doorstop`._

- **Added** RVM columns in [rtm_doorstop.py](rtm_doorstop.py) to generate an RVM instead of traceability matrix. 
  - **Includes:** UID, Text, Test Method(s), Tier and Status 
  - Potentially will have this as a config file if needed.
- **Removed** RTM columns in [rtm_doorstop.py](rtm_doorstop.py) _(Has Test, Need Test, Tests, Header)_.
  - Removed header as short name is different now on doorstop and header is another value presently in the modified version (doorstop-ewan).
- **Added** markdown output functionality.
  - Will make a csv file regardless by default but also make a markdown table for the RVM data selected if the path ends in 'markdown' or 'md'.
  - Using `--path instead` of `--csv_path`.
    - Shown in [Command Adjustments](#command-adjustments) 
- **Added** new requirements to the [requirements.txt](requirements.txt).
- **Removed** test directory
  - Since this will be used in a submodule for pearl_requirements, workflow will fail if test directory is present as it contains doorstop requirements / part of a doorstop tree. 
  - Will flag as 'multiple roots' and have an issue importing the first requirements document.
  - Removing allows this to be in a submodule and decreases the time for pearl_requirement workflows to run.
- **Removed** github workflow directory
- 
----------------

## Command Adjustments
_Overview of commands that have been adjusted from the Version 1.1.1 of [rtm_doorstop](https://github.com/asimon-1/rtm_doorstop). Refer to the [base README.md](README.md#rtm_doorstop-information) section for `rtm_doorstop` for additional information on commands, install, and base usage._

Adjustment from `--csv_path` to `--path` in command line.<br>

`rtm_doorstop 'PREFIX' --path`<br>

**Additional Information:**<br>
- `PREFIX` = The requirement _'document'_ in doorstop you want to generate an RVM for. 
  - Ex.) `L0` for Level 0 requirements
- `--path` = Directory for where the output RVM will be written too. 
  - The file extension also determines if a `markdown` or a `csv` file will be generated.
  - Ex.) `dist/latex/L4-RVM.md` or `dist/latex/L4-RVM.markdown`
  - Ex.) `dist/L4-RVM.csv`

--------