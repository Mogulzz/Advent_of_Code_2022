import re
import os

os.remove("test.txt") 
with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        ch = ','
        for x in range(len(line)):
            if ch == line[x]:
                f2 = open("test.txt", "a")
                f2.write(line[:x])
                f2.write("\n")
                f2.write(line[1+x:])
                f2.write("\n")
                f2.close()


with open('test.txt', 'r', encoding="utf-8") as f2:
    lines2 = f2.readlines()
    count = 0
    count2 = 0
    tab=[]
    for line2 in lines2:
        x = re.findall('[0-9]+', line2)
        tab.append(x)
        print(tab)

        if len(line2)== 1:
            task_elves1 =list((range(int(tab[0][0]), int(tab[0][1])+1)))
            task_elves2 =list((range(int(tab[1][0]), int(tab[1][1])+1)))

            if (task_elves1[0] in task_elves2 and task_elves1[-1] in task_elves2) or (task_elves2[0] in task_elves1 and task_elves2[-1] in task_elves1):
                count+=1

            S1 = set(task_elves1)
            S2 = set(task_elves2)
            if(S1.intersection(S2)):
                count2+=1

            tab.clear()
         
    print("Answer Part 1:", count)
    print("Answer Part 1:", count2)
