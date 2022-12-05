from setuptools import find_packages,setup
from typing import list

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:list[str] = []

    return requirement_list


setup(

    name="sensor",
    version="0.0.1",
    author="udaya",
    author_email="udaya276@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)