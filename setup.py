# setup.py
from setuptools import setup, find_packages

setup(
    name='parser_argv',
    version='0.1',
    packages=find_packages(),
    description='extract terminal arguments values easily.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='m0opha',
    author_email='jsaguamoraga@gmail.com',
    url='https://github.com/m0opha',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)

