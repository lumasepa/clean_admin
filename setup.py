#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import clean_admin

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = clean_admin.__version__

if sys.argv[-1] == 'publish':
    try:
        import wheel
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()

setup(
    name='clean_admin',
    version=version,
    description="""Django Admin with the bootstrap styles""",
    long_description=readme,
    author='Sergio Medina Toledo',
    author_email='lumasepa@gmail.com',
    url='https://gitlab.com/lumasepa/clean_admin',
    packages=[
        'clean_admin',
    ],
    include_package_data=True,
    install_requires=[
        "django",
        'six',
    ],
    license="AGPL",
    zip_safe=False,
    keywords='clean_admin',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
