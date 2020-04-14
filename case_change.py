"""
A program that takes concept of str.upper() and str.lower() method
the last one is based on Alternating Case kata on Codewars 

The idea behind turning string into lower and uppercase here is substract or add the value of their ascii value
for example :
    a = 97
    A = 65 

    as we can see here based on the a and A ASCII value,we could see that the lowercase and uppercase is separated by 32,this will also apply to other letter 

    therefore : 
    to change a to uppercase then the ASCII value need to be substracted by 32 (97-65),this will apply to other letter as well
    to change A to lowercase then the ASCII value need to be added by 32 (65+32= 97 = a),this will apply to other letter as well

    this program will also first check if character that will be converted is alphabetical or not

    while for the reversed case,the idea is just to swap things around,for every lowercase in string,turn it to uppercase
    and for every uppercase letter in string,turn it into lowercase

    for example : AbbA = aBBa 

"""

def to_lower(s):
    lower = ""
    for i in range(len(s)):
        if s[i].isalpha() and ord(s[i]) < 97:
            lower+=chr(ord(s[i])+32)
        else :
            lower+=s[i]
    return lower

def to_upper(s):
    upper = ""
    for i in range(len(s)):
        if s[i].isalpha() and ord(s[i]) > 96:
            upper+=chr(ord(s[i])-32)
        else :
            upper+=s[i]
    return upper

def reverse_case(s):
    reverse = ""
    for i in range(len(s)):
        if s[i].isalpha() :
            if ord(s[i]) > 96 :
                reverse+=chr(ord(s[i])-32)
            else :
                reverse+=chr(ord(s[i])+32)
        else :
            reverse+=s[i]
    return reverse

s = input()
print("Original : {}".format(s))
print("Lowercase : {}".format(to_lower(s)))
print("Uppercase : {}".format(to_upper(s)))
print("Reversed case : {}".format(reverse_case(s)))