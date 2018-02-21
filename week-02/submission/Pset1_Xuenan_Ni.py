##Xuenan Ni
##Feb.20
##Assignment 1

## A. Lists

##A.1. Create a list containing any 4 strings.
lis = ["what", "why", "when", "how"]
##A.2. Print the 3rd item in the list - remember how Python indexes lists!
print(lis[3-1])
#print(lis.index("when"))
##A.3. Print the 1st and 2nd item in the list using [:] index slicing.
#print(lis[0]+ ":" + lis[1])
print(lis[:2])
##A.4. Add a new string with text “last” to the end of the list and print the list.
lis.append("last")
print(lis)
##A.5. Get the list length and print it.
leng = len(lis)
print(leng)
##A.6. Replace the last item in the list with the string “new” and print
lis[leng-1] = "new"
print(lis)

##########################################

## B. Strings
# Given the following list of words stored as strings, complete the following tasks:
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
#B.1. Convert the list into a normal sentence with [`join()`](https://docs.python.org/3/library/stdtypes.html#str.join), then print.
new_sentence_words = " ".join(sentence_words)
print(new_sentence_words + ".")
#B.2. Reverse the order of this list using the `.reverse()` method, then print. Your output should begin with `[“them”, ”visualize”, … ]`.
sentence_words.reverse()
print(sentence_words)

#B.3. Now user the [`.sort()` method](https://docs.python.org/3.3/howto/sorting.html) to sort the list using the default sort order.
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
sentence_words.sort()
print(sentence_words)

#B.4. Perform the same operation using the [`sorted()` function](https://docs.python.org/3.3/howto/sorting.html). Provide a brief description of how the `sorted()` function differs from the `.sort()` method.
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
sor = sorted(sentence_words)
print(sor)
#Difference of .sort and sorted(): .sort is a in-place method, which changes the list; we can assign a new variable with value of sorted() and the original list is not affected.

#B.5. Extra Credit: Modify the sort to do a case [case-insensitive alphabetical sort](http://matthiaseisen.com/pp/patterns/p0005/).
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
sentence_words.sort(key=lambda s: s.lower())
print(sentence_words)

## C. Random Function
from random import randint
import math
##set my lower bound to be 1 and upper bound to be 10

def my_random(high, low=0):
    num = randint(10,1000)
    if low !=0:
        x = 10/low
        y = 1000/high
        if y>x:
            y = y
        else:
            y = x

    else:
        y = 1000/high
    z = math.floor(num/y)
    return z

print(my_random(10,1))

assert(0 <= my_random(10) <= 10)
assert(1 <= my_random(10, low = 1) <= 10)


## D. String Formatting Function
def bestseller(n, tit):

    ranking = "The number {} bestseller today is: {}".format(n , tit.title())

    return ranking

print (bestseller(2, "You Know ME"))

## E. Password Validation Function
'''
+ is 8-14 characters long
+ includes at least 2 digits (i.e., numbers)
+ includes at least 1 uppercase letter
+ includes at least 1 special character from this set: `['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']`
'''
characters = ['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']

def passcode():
    s = input('')
    num_digit = sum(1 for c in s if c.isdigit())
    num_uppercase = sum(1 for c in s if c.isupper())

    if len(s)>=8 and len(s)<=14 and num_digit>=2 and num_uppercase>=1 and any(elem in s for elem in characters):
        mes = "Success!"
    else:
        mes = "Fail!"
    return mes

passcode()


## F. Exponentiation Function
def exp(a,b):
    i=1
    multi = 1
    while i <= b:
        multi = multi * a
        i = i + 1
    return multi
exp(5,2)

## G. Extra Credit: Min and Max Functions

def maximum1():
    empty = []
    test = [34,45,100,101,43,45,77,873434,42342,4,26,7,343,33,33,5465,77]
    while len(test) > 1:

        for j in range(0,len(test)-1):
            if test[j] >= test[j+1]:
                empty.append(test[j])
            else:
                empty.append(test[j+1])
        test = empty
        empty = []
    return test
maximum1()

def minimum1():
    empty = []
    test = [34,45,100,101,43,45,77,873434,42342,4,26,7,343,33,33,5465,77]
    while len(test) > 1:

        for j in range(0,len(test)-1):
            if test[j] <= test[j+1]:
                empty.append(test[j])
            else:
                empty.append(test[j+1])
        test = empty
        empty = []
    return test
minimum1()
