# author: jrcheeseman

"""
Problem 1

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

count = 0
for letter in s:
   if letter in ('a','e','i','o','u'):
        count += 1
print('Number of vowels: ' + str(count))


"""
Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

count = 0
i = 0
for letters in s:
    if s[i:i+3] == 'bob':
        count += 1
    i += 1        
print('Number of times bob occurs is: ' + str(count))


"""
Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

temp = s[0:2]
strings = []
substring = s[0]
for i in range(len(s)-2): 
    if temp[0] <= temp[1]:
        substring += temp[1]
        strings.append(substring)
        temp += s[i+2]
        temp = temp[-2:]
        if i == len(s)-3:
            substring += temp[1]
            strings.append(substring) 
    else:        
        temp = s[i+1:i+3]
        substring = temp[0]
if strings == []:
    strings.append(s[0])      
print('Longest substring in alphabetical order is: ' + max(strings, key=len))
