from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirement(file_path: str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='dsproject',
    version='0.0.1',
    author='Sathwik',
    author_email='sathwikrenaissance@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt'),
)
