# IonWorks Project

This project uses PyBaMM (Python Battery Mathematical Modelling), an open-source battery simulation package written in Python. PyBaMM's mission is to accelerate battery modelling research by
providing open-source tools for multi-institutional, interdisciplinary collaboration.
Broadly, PyBaMM consists of
(i) a framework for writing and solving systems
of differential equations,
(ii) a library of battery models and parameters, and
(iii) specialized tools for simulating battery-specific experiments and visualizing the results.
Together, these enable flexible model definitions and fast battery simulations, allowing users to
explore the effect of different battery designs and modeling assumptions under a variety of operating scenarios.

## 🌎 Navigating the repository 
The repository is structured as follows:
- `projectnanme`: contains the source code
- `docs`: contains documentation
- `examples`: contains examples of how to use the code

## 📦 Adding new parameter sets
To add a new parameter set to the package, first add a python file to the `projectname/parameters` folder. The file should define a function `get_parameter_values` that returns a dictionary of parameter values. See the existing PyBaMM parameter sets for examples. Then register a new entry point in `pyproject.toml` under `
[project.entry-points.pybamm_parameter_sets]` with the name of the parameter set and the path to the python file. For example:
```toml
[project.entry-points.pybamm_parameter_sets]
MyCell = "projectname.parameters.mycell:get_parameter_values"

```
After adding new entry points you will need to reinstall the package using `pip install .` (or `pip install -e .` for a local installation) in the root directory.

It is of course possible to simply define a parameter set locally and import it into a script or notebook, but adding an entry point allows it to be used in the same way as the other PyBaMM parameter sets (`pybamm.ParameterValues("name")`).

 
## 📊 Data
All data is stored separately from this repository. You can set a data filepath as an environment varibale by creating a `.env` file in the root folder with the following contents:
```
DATA_PATH="path/to/data"
```
Then, in any script or notebook you can retive the data path by doing

```python3
import hackion

data_path = hackion.utils.environ["DATA_PATH"]
```
Make sure you add `.env` to `.gitignore`. Alternatively, you can simply specify the filepath manually. 

## 🔋 Using the package
The following example...
## 📖 Documentation
Documentation can be found in the `docs` directory.
## 🚀 Installation
The following instruction are for installing the package locally so that its contents can be edited. To install in `site-packages` simply use `pip install .` instead of `pip install -e .`. We recommend installing within a [virtual environment](https://docs.python.org/3/tutorial/venv.html) in order to not alter any python distribution files on your machine.

PyBaMM is available on GNU/Linux, MacOS and Windows. For more detailed instructions on how to install PyBaMM, see [the PyBaMM documentation](https://pybamm.readthedocs.io/en/latest/install/GNU-linux.html#user-install).

### Linux/Mac OS
To install the requirements on Linux/Mac OS use the following terminal commands:

1. Clone the repository or download and unzip the source code.
2. Change into the `project-template` directory 
```bash
cd project-template
```
3. Create a virtual environment
```bash
virtualenv env
```
4. Activate the virtual environment 
```bash
source env/bin/activate
```
5. Install the package
```bash 
pip install -e .
```
Using `pip install -e .` instead of just `pip install .` will install the package in editable mode from the local project path instead of trying to install in `site-packages`. 

### Windows
To install the requirements on Windows use the following commands:

1. Clone the repository or download and unzip the source code.
2. Change into the `project-template` directory 
```bash
cd project-template
```
3. Create a virtual environment
```bash
python -m virtualenv env
```
4. Activate the virtual environment 
```bash
env\Scripts\activate
```
where `env` is the path to the environment created in step 3 (e.g. `C:\Users\'Username'\env\Scripts\activate.bat`).

5. Install the package
```bash 
pip install -e .
```
Using `pip install -e .` instead of just `pip install .` will install the package in editable mode from the local project path instead of trying to install in `site-packages`. 

As an alternative, you can set up [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about). This allows you to run a full Linux distribution within Windows.

### Troubleshooting
**Problem**: `ModuleNotFoundError: No module named 'wheel'`.

**Solution**: Try `pip install wheel` before `pip install .`.

**Problem**: Changes I make to the code in the `project-template` folder aren't reflected when I try to run the code.

**Solution**: Install in editable model by doing `pip install -e .`.
## 📫 Get in touch

If you have any questions please get in touch via email <info@ion-works.com>.
