#!/usr/bin/env python2.7
from setuptools import setup

setup(
    name='sdfbuilder',
    version='0.2',
    description='Pragmatic utility library for building SDF files',
    author='Elte Hupkes',
    author_email='elte@hupkes.org',
    url='https://github.com/ci-group/sdf-builder',
    packages=[
        'sdfbuilder',
        'sdfbuilder.joint',
        'sdfbuilder.math',
        'sdfbuilder.physics',
        'sdfbuilder.sensor',
        'sdfbuilder.structure',
        'sdfbuilder.util'
    ],
    install_requires=['numpy']
)
