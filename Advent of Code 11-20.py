#Day 11
#Dumbo Octupus
data = '2682551651322313426358484714127438334862873132157364152335745564726843668345644585823461124617588236'
insert = []
for d in data:
    insert.append(int(d))
print(insert)
iteration = 100

def do_it_right(graph, num_of_iterations):
    counter = 0
    flash_counter = 0
    while num_of_iterations != counter:
        for each in graph:
            graph[each] += 1 #add one each time through the
            counter += 1
        for num in graph:
            if num == 9:
                flash_counter += 1
                nbrs = [graph[num - 1], graph[num + 1], graph[num + 10], graph[num - 10], graph[num - 11], graph[num - 9], graph[num + 11], graph[num + 9]]
                for nbr in nbrs:
                    if nbr == 9:
                        graph[nbr] = 0
                        counter += 1
                        flash_counter += 1
                        return do_it_right(graph, counter)
                    else:
                        graph[nbr] += 1
    return graph, flash_counter

print(do_it_right(insert, iteration))
#print(low_points(inputs,10))

#Day 13
#Transparent Origami
#lst is a list of lists:
#set an empty dictionary named frank
#set value as the length of the lst minus 1
#for line in range(0, len(lst)/2):
    #line + lst[value] = frank #needs work
    #value -= 1
#return frank
screw = '6,10,0,14,9,10,0,3,10,4,4,11,6,0,6,12,4,1,0,13,10,12,3,4,3,0,8,4,1,10,2,14,8,10,9,0'
new = screw.split(',')
print(new)
almost= []
for each in new:
    almost.append(int(each))
print(almost)
final = []
for idx in range(len(almost)-1):
    final.append(list(almost[idx] and almost[idx+1]))
print(final)


    


#def fold_horizontally(lsts):
#    frank = []
#    value = len(lsts) - 1
#    for idx in range(0,len(lsts) / 2):
#        for num in zip(lsts[idx], lsts[value]):
#            frank.append(lst(num))
#    return frank
#
#
#print(fold_horizontally())
