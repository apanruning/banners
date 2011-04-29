# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='banners',
      version=version,
      description="A simple banner manager app",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Banners, Django',
      author='Revoluciones Informáticas',
      author_email='info@revolucionesweb.com.ar',
      url='http://revolucionesweb.com.ar',
      license='',
      packages=find_packages(exclude=['ez_setup']),
      package_data={
        'banners' : ['templates/*.html'],
      },
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'django'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
