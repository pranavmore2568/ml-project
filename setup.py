#from django import VERSION
from pkg_resources import Requirement
from setuptools import setup
from typing import List

def get_requirements_list()->List[str]:
    """
    Description: This functio will return the list of requirement given in 
    requirement.txt 

    returns: This function is going to return the list of libraries given in 
    requirements.txt
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.0.1"
AUTHOR = "Avinash Yadav" 
DESCRIPTION = "This is a first FSDS machine learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

setup (
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()


)

