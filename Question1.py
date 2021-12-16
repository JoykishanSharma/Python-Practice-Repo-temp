# 1. Write a program to create, concatenate and print a string and accessing substring from a given string.

# creating a string
string1 = "Hello"
string2 = "I'm a String"

# concatenating strings using + operator
string3 = string1 + ", " + string2

# concatenating strings using join() operator
string4 = " ".join([string1, string2])

# concatenating strings using % operator
string5 = "% s % s" % (string1, string2)

# concatenating strings using % operator
string6 = "% s % s" % (string1, string2)

# concatenating strings using str.format()
string7 = "{} {}".format(string1, string2)

# print a string
print(string4)
print(string5)
print(string6)
print(string7)

# concatenating strings using ,
print(string1, string2)

# accessing substring, syntax -> str[start:end:steps]
substring1 = string3[0:5:1]
print(substring1)
