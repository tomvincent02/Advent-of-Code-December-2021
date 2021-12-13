#Day 1 Sonar Sweep
import urllib
from urllib import request

url = 'https://adventofcode.com/2021/day/1/input'

file = urllib.request.urlopen(url)

new = []

for line in file:
	decoded_line = line.decode("utf-8")
	new.append(decoded_line)

print(new)




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


print(increase(object))

