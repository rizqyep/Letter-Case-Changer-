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
