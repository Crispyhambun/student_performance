from setuptools import find_packages, setup
from typing import List
def get_requirments(file_path:str)->List[str]:
    '''return all the requirements'''
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    
    return requirements

setup(
    name="student performance project",
    author="Karan",
    author_email="shinigami709k@gmail.com",
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')
)
