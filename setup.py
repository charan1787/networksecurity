from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]: #telling that this function returns a list of string type
    "Function for list of requirements"
    requirement_list:List[str]=[] #telling that its a list of string inputs
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines() #reading lines
            for line in lines:
                requirement=line.strip()
                #ignore .env and empty lines
                #.env triggers the setup.py file to start
                if (requirement) and (requirement !='-e .'):
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

setup(
    name = 'Network Security',
    version = '0.0.1',
    author='Charan Shankar',
    author_email='charan.nitap@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)