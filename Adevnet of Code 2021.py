#Day 1 Sonar Sweep
import urllib
from urllib import request

url = 'https://adventofcode.com/2021/day/1/input'

#file = urllib.request.urlopen(url)

new = []

#for line in file:
#	decoded_line = line.decode("utf-8")
#	new.append(decoded_line)

#print(new)




object = [1,2,3,4,5,6,7,8,9,8]

def increase(lst):
    count = 0
    for idx in range(1,len(lst)):
        for each in lst:
            if each < lst[idx]:
                count += 1
                break
            else:
                break
    return count
#dont know how to import data

print(increase(object))

#day 2 Dive!

class Submarine:
    def __init__(self,initial_x,initial_y):
        self._initial_x = initial_x
        self._initial_y = initial_y

    def forward(self, f_value):
        return (self._initial_x + f_value)

    def up(self, d_value):
        return (self._initial_y - d_value)

    def down(self, d_value):
        return (self._initial_y + d_value)

    def get_position(self):
        return self._initial_x, self._initial_y

germans = Submarine(0,0)
germans.forward(5)
print(germans)
print(germans.forward(10))
 #dont know to have the instance of the class remember input data

 #Recursive problems

def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num-1) * num

print(factorial(10))

def product(lst):
    num = 1
    if len(lst) == 0:
        return num
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[len(lst) -1] * product(lst[:len(lst)-1])


print(product([2,3,4,5,6]))

def backwards(word):
    reverse = ''
    if len(word) == 0:
        return reverse
    else:
        return reverse.append(word[-1]) + backwards(word[:len(word)-1])

print(backwards('same'))