#!/usr/bin/python

import setuptools


setuptools.setup(
    name='betterurl',
    version='0.1.0',
    description='A better URL manipulation library',
    keywords = 'URL',
    url='https://github.com/allancaffee/betterurl',
    author='Allan Caffee',
    author_email='allan.caffee@gmail.com',
    license='BSD',
    packages=['betterurl'],
    test_suite='tests',
    long_description=open('README.rst').read(),
    entry_points={},
    zip_safe=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
)
