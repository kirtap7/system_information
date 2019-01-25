from setuptools import setup

setup(name="system_information",
      version="1.0",
      description="Basic system information",
      url="",
      author="Patrick Malatesta",
      author_email="patrick.malatesta@ucdconnect.ie",
      license="GPL3",
      packages=['system_information'],
      entry_points={
          'console_scripts':['system_information=system_information.main:main']
          }
      )