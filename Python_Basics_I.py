# %%
a = 56
b = 11
# 1) Basic Operations
# Addition +
# Subtraction -
# Multiplication *
# Division /
# Integer Division //
ans = a // b
print('Integer Division: ', ans)

# Modulo
ans = a % b
print('Modulo: ', ans)

# Exponentiation 
# square one of the variables
''' 
Note that a ^ b  will run but give you the wrong results. 
In python the ^ operator does not exponentiate like a normal person would expect it to, instead it does a bitwise XOR (if you do not know what that means its not very important and you will probably never use it in this course... neither in the rest of your life)
'''
ans = a ** b 
print('Exponentiation: ', ans)
# %%
# 2) Loops

''' 
a) Using only one for loop, draw the following shape:


size = 5
*
**
***
****
*****
'''
for i in range(6):
    print( '*' * i)
    print()
'''
b) Using two for loops, draw the following shape:
(if you'r feeling adventurous try doing it with 1 for loop)
'''
size = 5
for i in range(size, 0, -1):
    print(' ' * (size - i), '*' * ((2*i)-1))
for i in range(2,size +1):
    print(' ' * (size -i), '*' * ((2*i)-1))
m=0
d=-1   
for i in range(size,0, d):
    if i !=0:
       print(' ' * (size -i), '*' * ((2*i)-1)) 
       continue
    else:
       if i==1:
           d=1
           m= 5
           size= 1
    print(' ' * (m -i), '*' * ((2*i)-1))


'''
size = 5
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
c) Using a while loop brute force trying to find the square root of a perfect square and print it. If the number is not a perfect square, print 'square root not found'.
'''
# a)
size = 5
# Fill in the code here


# b)
size = 5
# Fill in the code here


# c)
n= 212300000
# Fill in the code here
i= 1
square_root=0
while n>0:
    n= n- i
    i +=2
    square_root +=1 
if n ==0:
    print("It is a perfect square number")
else:
    print('It is not a perfect square number')





# %%

# 3) Functions 
#  Write a function that takes a String and checks if it is a palindrome or 
# not. (a palindrome is a word that is read the same left to right and right to left i.e.: 'civic', 'anna' and '1001001' are palindromes but 'car' is not ) 

# Fill in the code here

def is_palindrome(x):
    if x[:]== x[::-1]:
        return "The string is palindrome"
    else:
        return "The string is not a palindrome"
    
print(is_palindrome('1001001'))
print(is_palindrome('Roua'))
