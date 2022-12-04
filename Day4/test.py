with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    Score = 0
    Score2 = 0
    for line in lines:
        pair1 , pair2 =line.split(",")
        pair1 = list(range(int(pair1.split("-")[0]), int(pair1.split("-")[1])+1))
        pair2 = list(range(int(pair2.split("-")[0]), int(pair2.split("-")[1])+1))

        Condition1_Part1 = all(item in pair1 for item in pair2)  
        Condition2_Part1 = all(item in pair2 for item in pair1)
        if Condition1_Part1 or Condition2_Part1: 
            Score+=1
        
        Condition1_Part2 = any(item in pair1 for item in pair2)  
        Condition2_Part2 = any(item in pair2 for item in pair1)
        if Condition1_Part2 or Condition2_Part2: 
            Score2+=1

    print("############################################################################ PART 1 ############################################################################")
    print("Answer Part 1", Score)

    print("############################################################################ PART 2 ############################################################################")
    print("Answer Part 2", Score2)
