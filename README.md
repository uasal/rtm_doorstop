# Modified rtm_doorstop 
**MODIFIED for generating an RVM instead with doorstop for requirements.**

_Version 1.1.1 of [rtm_doorstop](https://github.com/asimon-1/rtm_doorstop) used as a base._

## Change Log
_Quick reference of changes done to the original rtm_doorstop version._  

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

## Command Adjustments
_Overview of commands that have been adjusted from the main version of rtm_doorstop. Refer to the [base README.md](#rtm_doorstop-information) section for rtm_doorstop for additional information on commands, install, and base usage._

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

# rtm_doorstop Information
_Same README.md from [rtm_doorstop](https://github.com/asimon-1/rtm_doorstop)._

![PyPI Version](https://img.shields.io/pypi/v/rtm_doorstop)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rtm_doorstop)
![PyPI - License](https://img.shields.io/pypi/l/rtm_doorstop)
![Sonarcloud](https://img.shields.io/sonar/quality_gate/scuriosity_rtm_doorstop?server=https%3A%2F%2Fsonarcloud.io)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A tool to generate Requirement Traceability Matrices (RTMs) from [Doorstop](https://doorstop.readthedocs.io/en/latest/) documents.

--------

## Table of Contents

- [rtm_doorstop](#rtm_doorstop)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Usage](#usage)
  - [Installation](#installation)
    - [Dependencies](#dependencies)
  - [Contributing](#contributing)
  - [License](#license)

--------

## Features

The `rtm_doorstop` tool can be used to quickly build an Requirements Traceability Matrix (RTM) from a [Doorstop](https://doorstop.readthedocs.io/en/latest/) tree. RTMs map product requirements to test cases, which verify that said requirements are met. They are particularly useful to quickly understand the requirement coverage and any areas deficient in quality checks.

This tool can generate RTMs that are in Markdown-compliant format, or write to a CSV file.

```Markdown
| UID     | Header | Text                | Has Test | Need Test | Tests                   |
|---------|--------|---------------------|----------|-----------|-------------------------|
| REQ0001 | Ch 1   | Requirement A       | True     | True      | TST0001                 |
| REQ0002 | Ch 1.1 | Just a note         | False    | False     |                         |
| REQ0003 | Ch 1.2 | Another requirement | True     | True      | TST0003 TST0004 TST0005 |
```

```csv
UID,Header,Text,Has Test,Need Test,Tests
REQ0001,Ch 1,Requirement A,True,True,TST0001
REQ0002,Ch1.1,Just a note,False,False,
REQ0003,Ch 1.2,Another requirement,True,True,TST0003 TST0004 TST0005
```

--------

## Usage

The tool can be invoked via command line, and has one required argument: PREFIX

```cmd
rtm_doorstop --prefix=PREFIX
```

or simply

```cmd
rtm_doorstop PREFIX
```

Optional arguments are --root, --sort_key, and --csv_path.

| Argument | Description |
| ----- | ----- |
| root | If Doorstop cannot build a valid tree from the current working directory, you can specify the path to the tree root here |
| sort_key | If the RTM should be sorted, you can specify the key to sort by here. Valid options are 'UID', 'Has Test', or 'Tests' When omitted, no ordering is guaranteed. |
| csv_path | The filepath where the tool should save the RTM to. When omitted, the RTM is printed to console in Markdown format. |

Tests are assumed to be linked to the requirements as as child links. Doorstop specifies these links in the "links" yaml key. For instance, the following test would be linked to requirement REQ046.

```YAML
active: true
custom: 1
derived: false
header: ''
level: 4
links:
- REQ046: m9tMd0JM8O8idHTViqyYy1OL3dLiVY69bT63jNAGxPs=
normative: true
ref: test_yaml_encoding
reviewed: TIwopA6cvyjBMF17bB6p_RUNA7clNMaaEhXGYlAdpdk=
test_commit_last_passed: d670460b4b4aece5915caf5c68d12f560a9fe3e4
test_commit_latest: d670460b4b4aece5915caf5c68d12f560a9fe3e4
test_result_latest: passed
text: |
  Test that inputs can be loaded from a UTF-8 encoded YAML file.
```

--------

## Installation

You can install "rtm_doorstop" via
[pip](https://pypi.org/project/pip/) from
[PyPI](https://pypi.org/project):

```cmd
pip install rtm_doorstop
```

### Dependencies

-   [Doorstop](https://pypi.org/project/doorstop/)
-   [rapidtables](https://pypi.org/project/rapidtables/)
-   [fire](https://pypi.org/project/fire/)

--------

## Contributing

Contributions are very welcome, both in Issues and in Pull Requests. Tests can be run with
[tox](https://tox.readthedocs.io/en/latest/).

```bash
$ tox
```

If you encounter any problems, please [file an
issue](https://github.com/scuriosity/rtm_doorstop/issues) along with
a detailed description.

--------

## License

Distributed under the terms of the [GNU GPL
v3.0](http://www.gnu.org/licenses/gpl-3.0.txt) license,
"rtm_doorstop" is free and open source software
