#Day 6 LanternFish

lanternfish = [3,5,2,5,4,3,2,2,3,5,2,3,2,2,2,2,3,5,3,5,5,2,2,3,4,2,3,5,5,3,3,5,2,4,
                        5,4,3,5,3,2,5,4,1,1,1,5,1,4,1,4,3,5,2,3,2,2,2,5,2,1,2,2,2,2,3,4,5,2,
                        5,4,1,3,1,5,5,5,3,5,3,1,5,4,2,5,3,3,5,5,5,3,2,2,1,1,3,2,1,2,2,4,3,4,1,
                        3,4,1,2,2,4,1,3,1,4,3,3,1,2,3,1,3,4,1,1,2,5,1,2,1,2,4,1,3,2,1,1,2,4,3,5,
                        1,3,2,1,3,2,3,4,5,5,4,1,3,4,1,2,3,5,2,3,5,2,1,1,5,5,4,4,4,5,3,3,2,5,4,4,1,
                        5,1,5,5,5,2,2,1,2,4,5,1,2,1,4,5,4,2,4,3,2,5,2,2,1,4,3,5,4,2,1,1,5,1,4,5,1,2,
                        5,5,1,4,1,1,4,5,2,5,3,1,4,5,2,1,3,1,3,3,5,5,1,4,1,3,2,2,3,5,4,3,2,5,1,1,1,2,2,5,
                        3,4,2,1,3,2,5,3,2,2,3,5,2,1,4,5,4,4,5,5,3,3,5,4,5,5,4,3,5,3,5,3,1,3,2,2,1,4,4,5,
                        2,2,4,2,1,4]
print(len(lanternfish))




#if num == 0:
    #first_gen_fish.append(8)
    #num should equal 6 again
#Else;
    #num -=1
#days +=1

def fish_count(input_days, number_of_lanternfish):
    days = 0
    first_gen_fish = []
    while days != input_days:
        for fish in number_of_lanternfish:
            if fish == 0:
                first_gen_fish.append(8)
                fish = 6
            else:
                fish -= 1
        if len(first_gen_fish) != 0:
            for babies in first_gen_fish:
                if babies == 0:
                    first_gen_fish.pop(babies)
                    number_of_lanternfish.append(6)
                    first_gen_fish(8)
                else:
                    babies -= 1
        days += 1
    return len(first_gen_fish) + len(number_of_lanternfish)

print(fish_count(80, lanternfish))