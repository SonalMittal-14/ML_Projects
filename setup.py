# this file is responsible for creating a machine learning application as a package. so that we can install this package and further use it.


from setuptools import find_packages,setup #find all the packages are there in the entire machine laerning application

from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list pf requirements 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Sonal',
    author_email='sonalmittal140103@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)