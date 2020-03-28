to publish:
 1. Create api token on [pypi](https://pypi.org/manage/account/token/) 
 1. python3 -m pip install --user --upgrade twine
 1. python3 setup.py sdist
 1. python3 -m twine upload dist/*