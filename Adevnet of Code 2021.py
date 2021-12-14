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

#print(increase(object))

#day 2 Dive!

class Submarine:
    def __init__(self, initial_x, initial_y):
        self._initial_x = initial_x
        self._initial_y = initial_y

    def forward(self, f_value):
        self._initial_x = self._initial_x + f_value

    def up(self, d_value):
        self._initial_y =  self._initial_y - d_value

    def down(self, d_value):
        self._initial_y = (self._initial_y + d_value)

    def get_position(self):
        return self._initial_x, self._initial_y

germans = Submarine(0,0)
germans.forward(5)
germans.forward(10)
print(germans.get_position())

 #dont know to have the instance of the class remember input data

 #Day 3 Binary Diagonistic

def power_consumption(big_lst):
    gamma_rate = []
    gamma_value = 0
    epsilon_rate = []
    epsilon_value = 0
    lst_1 = {0:0, 1: 0, 2:0, 3:0, 4:0}
    bin_val = [16,8,4,2,1]
    big_lst_length = len(big_lst)
#counting mass list and adding to a list
    for lst in big_lst:
        for number in range(0, 5):
            if lst[number] == 0:
                lst_1[number] += 1
            else:
                pass
#checking to see if the binary number should be 0 or 1 and add to gamma
    for value in lst_1:
        if lst_1[value] >= big_lst_length / 2:
            gamma_rate.append(0)
        else:
            gamma_rate.append(1)
#converting to binary
    for idx in gamma_rate:
        for each in range(len(bin_val)-1):
            if idx == 1:
                gamma_value += bin_val[each]
                break
            else:
                epsilon_value += bin_val[each]
                break
    return (gamma_value * epsilon_value)

print(power_consumption([[0,1,1,1,1],[0,0,1,1,1]]))








