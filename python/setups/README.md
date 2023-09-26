## Virtualenv

```
pip install -r python/setups/requirements.txt 
virtualenv my_env
virtualenv -p /usr/bin/python3 my_env
source my_env/bin/activate
(my_env)$ pip install Django==1.9
(my_env)$ pip list
(my_env)$ deactivate
```

## pipenv

```
pipenv shell
(golang-python) @govindarajanv ➜ /workspaces/golang-python (main) $ python
Python 3.10.8 (main, Aug 19 2023, 00:31:12) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.executable
'/home/codespace/.local/share/virtualenvs/golang-python-m9tixErq/bin/python'
cat Pipfile Pipfile.lock
```
