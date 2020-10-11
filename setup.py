# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in watches/__init__.py
from watches import __version__ as version

setup(
	name='watches',
	version=version,
	description='watch purpose',
	author='Aisha',
	author_email='26j09998@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
