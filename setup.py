# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.3'

setup(name='banners',
      version=version,
      description="A simple banner manager app",
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='Banners, Django',
      author='Revoluciones Informáticas',
      author_email='info@revolucionesweb.com.ar',
      url='http://revolucionesweb.com.ar',
      license='MIT',
      packages=find_packages(exclude=['ez_setup']),
      package_data={
          'banners': ['templates/*.html'],
      },
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'django',
          'django-taggit'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
