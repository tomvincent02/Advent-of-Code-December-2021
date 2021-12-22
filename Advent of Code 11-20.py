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

#Day 12
#