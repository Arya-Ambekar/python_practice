# PYTHON BASICS REVISION

# print function
print("Hello Python")

# variable declaration
first_name = "Tony"
last_name = "Stark"
age = 51
is_genius = True

# input function to take the input from user
superhero_name = input("Tony, tell me your superhero name: ")
print("Superhero name of Tony is " + superhero_name)

# type conversion
    # 1. int()
    # 2. float()
    # 3. str()
    # 4. bool()

# old_age = input("Enter your age: ")
# new_age = int(old_age) + 2
# print(new_age)

# OR 

old_age = int(input("Enter your age: "))
new_age = old_age + 2
print(new_age)

# Strings
name = "Tony Stark"
print(name.upper()) # doesn't changes original string, instead returns new string as a output
print(name)

print(name.lower()) # doesn't changes original string, instead returns new string as a output
print(name)

print(name.find('y')) # returns the index of element # output => 3
print(name.find('Y')) # returns -1
print(name.find("Stark")) # returns the index of starting letter of word # output => 5
print(name.find("stark")) # returns -1

print(name.replace("Tony Stark", "Ironman")) # doesn't changes original string, instead returns new string as a output
print(name)

# to check if character/string is part of the main string
print("Stark" in name)
print('S' in name)
print('s' in name)


# Arithmetic Operators
print(5 + 2)   # add
print(5 - 2)   # subtract
print(5 * 2)   # multiply
print(5 / 2)   # divide
print(5 // 2)  # floor division i.e returns only int ... numbers after decimal are removed 
print(5 % 2)   # Modulus ... returns the reminder of division
print(5 ** 2)  # Exponent i.e power operator ... here expression is 5 to the power 2

i = 2
i = i + 2
i += 2
i -= 2
i *= 2   # etc,....

# Operator precedence
result = 3 + 4 * 2    # 14 or 11 ?
print(result)

# Comparison Operators
is_greater = 2 > 6
is_lesser = 2 < 6
# 2 <= 5
# 2 >= 5
is_not_equal = 1 != 6
is_equal = 1 == 6
