from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='banners',
      version=version,
      description="A simple banner manager app",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Banners, Django',
      author='Revoluciones Inform\xc3\xa1ticas',
      author_email='info@revolucionesweb.com.ar',
      url='http://revolucionesweb.com.ar',
      license='',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
