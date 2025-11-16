# To create this directory as a package. So that anyone can import this as a module
from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e.'

def get_requirments(file_path:str)->List[str]:
    with open(file_path) as file:
        requirments=file.readlines()
        requirments=[requirment.replace('\n',"") for requirment in requirments ]
    if HYPEN_E_DOT in requirments:
        requirments.remove(HYPEN_E_DOT)
    return requirments

setup(
    name='Bank Customers Crunch',
    version='0.0.0.1',
    author='Pranay',
    author_email='pranay6243@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')
    )