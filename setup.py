from setuptools import setup

setup(name="systeminformation",
      version="1.0",
      description="Basic system information",
      url="",
      author="Patrick Malatesta",
      author_email="patrick.malatesta@ucdconnect.ie",
      license="GPL3",
      packages=['systeminformation'],
      entry_points={
          'console_scripts':['systeminformation=systeminformation.main:main']
          }
      )