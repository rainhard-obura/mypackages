from setuptools import setup, find_packages

setup(
    name = "tutorialpackaging",
    version = "0.0.1",
    packages= find_packages(exclude=['tests']),
    description = "A small example package",
    long_description = open("README.md").read()
 )