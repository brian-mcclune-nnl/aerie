"""The aerie setup.py script."""

import setuptools


setuptools.setup(
    name='aerie',
    version='0.1.0',
    author='Brian McClune',
    author_email='bpmcclune@gmail.com',
    description='A plotter and document builder for birds of prey',
    license='MIT',
    keywords='plot document docx',
    packages=['aerie'],
    classifiers=[
        'Proramming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'matplotlib',
        'pandas',
        'python-docx==0.8.10.6',
    ]
)
