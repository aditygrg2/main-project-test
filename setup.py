from setuptools import setup, find_packages

setup(
    name="main-project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "execA @ git+https://github.com/aditygrg2/test-package.git#egg=execA"
    ],
)
