# -*- coding: utf-8 -*-

import os

from setuptools import find_packages
from setuptools import setup

version = '2.0a2-4dev'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'deform', 'tests', 'test_deform.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.deform',
    version=version,
    description="Fanstatic packaging of deform",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Fanstatic developers',
    author_email='kotti@googlegroups.com',
    url='https://github.com/fanstatic/js.deform',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=[
        'deform>=2.0.2',
        'fanstatic',
        'js.jquery',
        'js.jquery_form',
        'js.jquery_maskedinput',
        'js.jquery_maskmoney',
        'js.jquery_sortable',
        'js.jquery_timepicker_addon',
        'js.jqueryui',
        'js.modernizr',
        'js.select2',
        'setuptools',
    ],
    extras_require={
        'testing': [
            'pyramid',
            'pyramid_chameleon',
            'pytest>=3.0.0',
            'pytest-cov',
            'pytest-pep8!=1.0.3',
            'pytest-warnings',
        ],
    },
    entry_points={
        'fanstatic.libraries': [
            'deform = js.deform:library',
        ],
    },
)
