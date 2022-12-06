import re
import os

os.remove("test.txt")
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    tab = []
    for line in lines:
        for i in range(len(line) - 3):
            if (
                (
                    line[i] != line[i + 1]
                    and line[i] != line[i + 2]
                    and line[i] != line[i + 3]
                )
                and (
                    line[i + 1] != line[i]
                    and line[i + 1] != line[i + 2]
                    and line[i + 1] != line[i + 3]
                )
                and (
                    line[i + 2] != line[i]
                    and line[i + 2] != line[i + 1]
                    and line[i + 2] != line[i + 3]
                )
                and (
                    line[i + 3] != line[i]
                    and line[i + 3] != line[i + 1]
                    and line[i + 3] != line[i + 2]
                )
            ):
                tab.append(i + 4)

        for j in range(len(line) - 14):
            f2 = open("test.txt", "a")
            f2.write(line[j : j + 14])
            f2.write("\n")
            f2.close()

    print("\n")
    print(
        "############################################################################ PART 1 ############################################################################"
    )
    print("Answer Part 1:", tab[0])

with open("test.txt", "r", encoding="utf-8") as f3:
    lines2 = f3.readlines()
    tab2 = []
    for line2 in lines2:
        s = set(line2)
        if len(s) == 15:
            tab2.append(line2)
    tab2[0] = tab2[0].replace("\n", "")

    print("\n")
    print(
        "############################################################################ PART 2 ############################################################################"
    )
    print("Answer Part 2:", line.index(tab2[0]) + 14)
