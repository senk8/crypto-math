#!/bin/sh

# python3 setup.py build_ext --inplace
python3 setup.py install 
cd src
rm *.cpp
rm *.c