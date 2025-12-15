# Python 2, lots of syntax/functions
# incompatible with Python 3

# In pyhthon2 we did not have () in print statement
# print "Hello, World!"  # Python 2 syntax

# What is a programming language but a combination of syntax and semantics? And libraries maintened by the community
# python3.5+
name:str = "Peter"

# A token is the smallest unit of a programming language
# A token is identifier, keyword, operator, delimiter, literal, or comment
# A token is identified by its meaning and context in the code,
# A Token example is the match/case statement introduced in Python 3.10, and other examples is f-strings introduced in Python 3.6

# A break point is when we freeze the syntax and semantics of a programming language
# A break point is a moment in time when the programming language maintainers decide to make breaking
# changes to the language, and introduce new syntax or deprecate old syntax

# The syntax below is a Python 3 syntax
if name == "Peter":
	print("Hello, Peter! This is your English name")

elif name == "Pedro":
	print("Hola, Pedro! Este es tu nombre en Español")

elif name == "Pierre":
	print("Bonjour, Pierre! C'est ton nom en Français")
	

else:
	print("Hello! Your name is not recognized in our system.")


# Python 3.11 syntax
match name:
	case "Peter":
		print("Hello, Peter! This is your English name")
	case "Pedro":
		print("Hola, Pedro! Este es tu nombre en Español")
	case "Pierre":
		print("Bonjour, Pierre! C'est ton nom en Français")
	case _:
		print("Hello! Your name is not recognized in our system.")

# Python 3.5
# - type hints!!! We are saved!

# Python 3.7
# - Dataclasses
# -Forward type references: from __future__ import annotations
# - async/await became keywords; assincio more stable
# Python 3.8
# - Walrus operator (:=)
# better f-string syntax, e.g f"{variable=}"

# Python 3.9
# - Merge dictionaries with dict1 | dict2, dict1 |= dict2
# - zoneinfo library for working with time zones

# Python 3.10
# - match/case statement (structural pattern matching)
# - precise error messages when you forget commas,
# don't close parentheses, etc.

# PEP: means Python Enhancement Proposal
# PEP 8 - style guide for Python code
# PEP 20 - The Zen of Python
# PEP 484 - Type Hints

def add_numbers(a,b):
	print(f"Adding numbers: {a}, {b}")
	print(a+b)
	return a + b

result = add_numbers()
print(f"Result: {result}")

def so_some_math()
	sums = 1 +2 +3
	print(f"Sum: {sum}")
	return sum