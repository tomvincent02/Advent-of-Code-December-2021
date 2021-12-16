#Day 1 Sonar Sweep
import urllib
from urllib import request
from typing import NamedTuple

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

print(power_consumption([[0,1,1,1,1]]))

#Day 4 Giant Squid

INPUT_S = '''\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''

class Board(NamedTuple):
    left = set([])
    ints = []

    @property
    def has_won(self) -> bool:
        for i in range(5):
            for j in range(5):
                if self.nts[i * 5 + j] in self.left:
                    break
                else:
                    return True
            for j in range(5):
                if self.ints[i + 5 + j] in self.left:
                    break
                else:
                    return True
            else:
                return False


    @classmethod
    def parse(cls, Board:str) -> Board:
        ints = [int(s)for s in board.split()]
        left = set(ints)
        return cls(lefts,ints)

first, *rest = INPUT_S_split('\n\n')

boards = (Board.parse(board) for board in rest)
ints = [ints(s) for s in first.split(',')]

def get_numbers() -> int:
    for num in ints:
        for board in boards:
            if board_.has_won:
                board.left.discard(num)
        for board in boards:
            if board_.has_won:
                return sum(board.left + num)

    raise AssertionError("unreachable")

print(get_numbers())

#Day #5 Hydrothermal Venture
from urllib.parse import urlparse, parse_qs
url = 'https://adventofcode.com/2021/day/5/input'
parsed = urlparse(url)
query = parse_qs(parsed.query)
[page] = query['page']
int(page)
#parse the board and add the point to tuples within a list example is [(1,2,1,5),(2,3,5,3)]

def valid_point(parsed_data):
    usable_point = []
    for tup in parsed_data:
        if tup[0] == tup[2]:
            usable_point.append(tup[0] and tup[1])
            usable_point.append(tup[2] and tup[3])
            for each in range(tup[0],tup[2],1):
                usable_point.append(tup[0] ,each)
        if tup[1] == tup[3]:
            usable_point.append(tup[0] and tup[1])
            usable_point.append(tup[2] and tup[3])
            for each in range(tuple[1], tuple[3] + 1, 1)
                usable_point.append(tuple[0],each)
    return usable_point

def doubles(usable_point):
    empty_dict = {}
    for each in usable_point:
        if each not in empty_dict:
            empty_dict[each] = 1
        else:
            empty_dict[each] += 1
    return empty_dict

def final(empty_dict):
    counter = 0
    for value in empty_dict.values():
        if value >= 2:
            counter += 1
    return counter

