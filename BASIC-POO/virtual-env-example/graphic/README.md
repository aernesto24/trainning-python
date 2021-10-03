## Example to run virtual envirnments on Python

```
python3.7 -m venv env
```

You start with:
- **python3.7** The python version (in case you have several versions installed)
- **-m** to execute the module
- **venv** to create the virtual environment
- **env** is the name of the environment, you can put other name here

After creating the virtual environment you must activate if

```
source env/bin/activate
```

**NOTE:** This example works fr¡or MAC


Now you can install anything on your environment

To check what is installed on your environment, execute:
```
pip freeze
````

To get out from our virtual environment, we need to execute:
```
deactivate
```

You can also add the requirements to an external **txt** file, and use the following:
```
pip install -r requirements.txt
``` 
