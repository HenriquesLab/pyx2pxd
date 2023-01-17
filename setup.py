#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Bruno Manuel Santos Saraiva",
    author_email='bruno.msaraiva2@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Automatically generates pxd files form pyx files",
    entry_points={
        'console_scripts': [
            'pyx2pxd=pyx2pxd.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='pyx2pxd',
    name='pyx2pxd',
    packages=find_packages(include=['pyx2pxd', 'pyx2pxd.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/brunomsaraiva/pyx2pxd',
    version='0.0.1',
    zip_safe=False,
)
