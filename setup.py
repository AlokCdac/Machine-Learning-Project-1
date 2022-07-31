from setuptools import setup
from typing import List



PROJECT_NAME='House Price Predictor'
VERSION='0.0.1'
AUTHOR='ALOK DWIVEDI'
DESCRIPTION='This is my first END TO END Project'
PACKAGES='housing'
INSTALL_REQUIRES=get_requirements()
REQUIREMENT_FILE="requirements.txt"

def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE) as requirement_file:
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    packages=PACKAGES,
    install_requires=get_requirements()


)


if __name__'__main__':
    print(get_requirements())