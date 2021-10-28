# Python Intermediate software examples

## Important information to remember

**To create a venv**
```
$python3 -m venv environment_name
```

On linux the required command for python is python3, python alone will not be accepted

**To activate the virtual environment**
On Linux
```
$source venv/bin/activate
```

**TO exit venv**
```
$deactivate
```

## Install dependencies With PIP

PIP is the package installer for python, similar to npm for javascript

**To show modules installed at this time**
```
$pip freeze
$pip3 freeze
```

**To install a file**
```
$pip install name_of_module
```

**NOTE:** THis will make the the module to be installe inside the virtualenv

**You can install requirements and then use the following command to create the requirements.txt to share to other users** 
```
$pip freeze > requirements.txt
```

**After this on the remote computer, you can execute:**
```
$pip install -r requirements.txt
```