"""
    NOTE: PACKAGE WILL BE READ WHERE THE FUNCTION IS EXECUTED
"""

from another_package import function_b
from package import function_d


print(function_b(4))
print(function_d(4))

print(5/0)

print("Final text")