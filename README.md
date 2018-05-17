# box
This repository includes an example function for Hypar and all of the additional files required to make a Hypar package.

## What does all of this stuff do?
Your function will be identified in Hypar using the format `<organization>-<name>`.

### Config
Your repository must include a `hypar.json` file. This file contains the following parameters:
- `handler` - This is the fully qualified name of the function that is called by the system.
- `parameters` - A dictionary of parameter types, range values, and descriptions.
- `returns` - A Dictionary of return types and descriptions.
- `runtime` - Currently only `python3.6` is supported.

### Dependencies
If your function has dependencies that would typically be installed locally using `pip install`, they will need to be listed in the `requirements.txt` file. You can find out more about requirements files [here](https://pip.readthedocs.io/en/1.1/requirements.html).



