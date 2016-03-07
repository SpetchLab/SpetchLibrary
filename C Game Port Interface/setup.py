from distutils.core import setup, Extension
setup(name='readPort', version='1.0',  \
      ext_modules=[Extension('readPort', ['PortFunctions.c'])])