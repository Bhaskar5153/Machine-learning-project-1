from setuptools import find_packages, setup


def get_requirements(file_path:str):

    requirements = []

    with open(file=file_path) as file:
        content = file.readline()

        requirements = [req.replace('\n', '') for req in content]

        if '-e' in requirements:

            requirements.remove('-e')

        return requirements
    


    

setup(
    name='Machine learning project 1',
    version='0.0.1',
    author='Bhaskar',
    author_email='baskar.baskar91@gmail.com',
    packages=find_packages(),
    install_require=get_requirements('requirements.txt')
)