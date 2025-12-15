# When versioning is in 0.0.0 means that the software in still in development phase
# Semantic Versioning - MAJOR.MINOR.PATCH
# the ideas of the software is in initial phase
# any code could change at any time
# 0.1.0 - first release of the software
# 0.1.1 - bug fixes

# The path that authors uses to communicate the changes in the software to the users - that they are making breaking changes or new features

# One example is Python versions
# Python 2.x.x - legacy version
# Python 3.x.x - current version
# A particular feature are not useful in Python 2.x.x but are useful in Python 3.x.x

# A commonb pattern you will see for introducing breacking changes among very mature software projects - deprecation warnings
# Deprecation warnings - remove an existing functionality ot piece of an existing API

# What is the process for deprecating some especific functionality?
# 1. Delete the functionality right away - not recommended  - abrupt change for users
#     a. Commit the change and comment it 
# 	  b. Find other function that made similar functionality (?)
# 2. If add new functionality for the function:
#     a. If all the minor version updates are features that users want to use, but thei are blocked because they are not updates the old codes
#     b. Special topic with large software projects 
#     c. The estrategy: give to the users time to migrate their code to the new functionality - warm up period
#     d. A warning message is added to the old functionality - deprecation warning
#     e. If choose to update to a major version, to send a strong signal to users that have serious breaking changes, and their applications may break if they update to the new major version 
#     f. The reasons to make warning messages:
#         i. Give users time to migrate their code to the new functionality
#         ii. Avoid boring usesrs with unspected breaking changes
#      g. Avoid third party dependencies that are not updated to the new functionality 
from warnings import warn

# 1.0.0
def add_numbers1(a,b,c):
	return a + b + c

# 1.0.1	
def add_numbers(a, b,c):
	# faster and secure - debug errors
	return a + b + c

# 2.0.0
def add_numbers2(a, b, c, d):
	# added support for four numbers - new functionality
	print(f"Adding four numbers: {a}, {b}, {c}, {d}")
	print("Warning: This function will be deprecated in future versions. Please update your code to use the new add_numbers function with four parameters.\n")
	return a + b + c + d

# breaking changes - can be when rename something or pick away functionality

# 1.1.0 - make a breaking change, and implementing the major version component
def add_numbers3(a, b, c, d=0):
	print(f"Adding numbers: {a}, {b}, {c}, {d}")
	warn("Warning: The add_numbers function with four parameters will be deprecated in future versions. Please update your code accordingly.\n", DeprecationWarning)

	return a + b + c + d

add_numbers1(1, 2, 3)
add_numbers3(1, 2, 3)
add_numbers2(1, 2, 3, 4)

# pip install version-concepts==1.0.0
# pip install version-concepts<=2.0.0

