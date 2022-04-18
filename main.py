from msilib.schema import Error
import os 
import math
import pytest

# Return max value between 2 values
def max(a      , b):
    if a < b:
        return a
    else:
        return b
