# Create a program that takes the length of the password and generates a random password of the same length.

import random

passwordlength = int(input("Enter the length of password: "))
s = "abcdefghijklmnipqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%"
p = "".join(random.sample(s,passwordlength))
print(p)