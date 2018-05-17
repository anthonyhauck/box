# box
This repository includes an example function for Hypar and all of the additional files required to publish a function to Hypar.

## What does all of this stuff do?

### hypar.json
This file contains the following parameters:
- `function` - This is the fully qualified name of the function that is called by the system. For this example, we want to call the `box` function in the `box` module, so the value is `box.box`.
- `parameters` - A dictionary of parameter types, range values, and descriptions.
  - Supported parameter types:
    - `number` - A floating point number.
- `returns` - A dictionary of return value descriptions, keyed by the return name.
- `runtime` - The runtime used to execute the function.
  - Supported runtime values:
    - `python3.6`

### requirements.txt
The `requirements.txt` file lists packages that are required by your function. You can find out more about requirements files [here](https://pip.readthedocs.io/en/1.1/requirements.html). The benefit of having a `requirements.txt` file, in addition to making your function compatible with Hypar, is that you can install dependencies locally as well using `pip install -r requirements.txt`.

### LICENSE
Your repository should included a license file. This is suggested by GitHub, but not required by Hypar. Keep in mind that Hypar will make every function that is pushed to the platform publicly available to other users.

### README.md
The world wants to know what your function does. Include a README file that explains how to use your function. The Hypar interface will link to this README for documentation of your function. To run the tests locally, you can do `python3 -m unittest`.

### test
Every function should have tests. Hypar does not require that your function have unit tests, but it is good practice, and if a `test` folder exists, Hypar will run the tests. Hypar uses python's `unittest` package. If testing your function fails, your function will not be pushed to Hypar.



