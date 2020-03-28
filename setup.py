from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mysql_server_has_gone_away",
    version="1.0.0",
    description="Django myslq backend that fixes issue with long living connection",
    author='Andrew Koidan',
    author_email='deathangel908@gmail.com',
    license="MIT",
    url='https://github.com/akoidan/MySQL-server-has-gone-away',
    long_description=long_description,
    packages=find_packages(),
    long_description_content_type="text/markdown",
)
