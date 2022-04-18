from msilib.schema import Error
import os 
import math
import pytest

# Return max value between 2 values
def max(a, b):
    this_will_cause_a_error = "asssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
    if a > b:
        return a
    else:
        return b
