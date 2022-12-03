with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    my_list = [] 
    var=0
    for line in lines:
        if line.strip():
            var += int(line)
        else:
            my_list.append(var)
            var = 0
            my_list= sorted(my_list,reverse=True)
            Ordered_Tab=sorted(my_list,reverse=True)
            total_Calories_Part_2 = sum(Ordered_Tab[0:3])

    print("############################################################################ PART 1 ############################################################################")
    print("Answer Part 1", max(my_list))

    print("############################################################################ PART 2 ############################################################################")
    print("Answer Part 2",total_Calories_Part_2)
