# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.0'


setup(
    name='django-file',
    version=version,
    keywords='Django File',
    description='Django File Relative',
    long_description=open('README.rst').read(),

    url='https://github.com/django-xxx/django-file',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['django_file'],
    py_modules=[],
    install_requires=['django-file-md5'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
