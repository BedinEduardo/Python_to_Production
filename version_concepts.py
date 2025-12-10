# 1.0.0
def add_numbers(a,b,c):
	return a + b + c

# 1.0.1	
def add_numbers(a, b,c):
	# faster and secure - debug errors
	return a + b + c

# 2.0.0
def add_numbers(a, b, c, d):
	# added support for four numbers - new functionality
	print(f"Adding four numbers: {a}, {b}, {c}, {d}")
	return a + b + c + d

add_numbers(1, 2, 3, 4)

# pip install version-concepts==1.0.0
# pip install version-concepts<=2.0.0