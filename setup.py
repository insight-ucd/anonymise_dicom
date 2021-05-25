#!/usr/bin/env python

from distutils.core import setup
import setuptools

setup(name='anondicom',
      version='1.0',
      description='Python Dicom Anonymiser',
      author='Aonghus Lawlor',
      author_email='aonghus.lawlor@ucd.ie',
      url='https://github.com/insight-ucd/anonymise_dicom',
      packages=setuptools.find_packages(),  # Required

      entry_points={
          'console_scripts': [
              'anondicom = anondicom.dicom_anonymise:main'
          ]
      },

      # This field lists other packages that your project depends on to run.
      # Any package you put here will be installed by pip when your project is
      # installed, so they must be valid existing projects.
      #
      # For an analysis of "install_requires" vs pip's requirements files see:
      # https://packaging.python.org/en/latest/requirements.html
      install_requires=['pydicom', 'python-magic'],  # Optional
      )
