# python-hafb

## Instructor Project
https://github.com/hugo-wsu/python-hafb

### Sample scripts
```buildoutcfg
https://icarus.cs.weber.edu/~hvalle/hafb/
```

## Local installations

Login to system using:
- Username: **txx** (xx is terminal number)
- Password: **Hello123**


need to open a terminal and run the following commands
```bash
pip install pytest
```

Reload Pycharm

## Setup pytest to run in `Powershell`
Run the following command:
```bash
# username is your login to your session
$Env:PATH += ";C:\users\t25\appdata\roaming\python\python39\Scripts"
```
Then, run your test script
```bash
pytest -xv test_hello.py
```