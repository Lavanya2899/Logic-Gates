from setuptools import setup

with open('README.md', 'r') as file:
     long_description = file.read()

setup(
    name='logic gates',
    version='1.0',
    description='A package that can calculate logical arithmetic functions in logic gates ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['logic gates'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    url="https://github.com/Lavanya2899/Logic-Gates.git",
    author='Lavanya.C, Venkateswar.S',
    author_email='lavslyra28@gmail.com'
)

