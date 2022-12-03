with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    Score=[]
    Score2=[]
    for line in lines:
        if "A X" in line:     ## DRAW:  
            Score.append(1+3)

        if "A Y" in line:   ## WIN:  
            Score.append(2+6)

        if "A Z" in line:   ## LOSE:  
            Score.append(3+0)
            
        if "B X" in line:   ## LOSE:  
            Score.append(1+0)

        if "B Y" in line:   ## DRAW:  
            Score.append(2+3)

        if "B Z" in line:   ## WIN:  
            Score.append(3+6)

        if "C X" in line:   ## WIN:  
            Score.append(1+6)

        if "C Y" in line:   ## LOSE:  
            Score.append(2+0)

        if "C Z" in line:   ## DRAW:  
            Score.append(3+3)
    print("############################################################################ PART 1 ############################################################################")
    print("Answer Part 1:", sum(Score))

    for line in lines:
        ################# SITUATION IN WHICH WE HAVE TO LOSE
        if "A X" in line:
            Score2.append(3+0)

        if "B X" in line:
            Score2.append(1+0)

        if "C X" in line:
            Score2.append(2+0)

        ################# SITUATION IN WHICH WE HAVE TO END THE ROUND WITH A DRAW
        if "A Y" in line:
            Score2.append(1+3)

        if "B Y" in line: 
            Score2.append(2+3)

        if "C Y" in line:
            Score2.append(3+3)
        
        ################# SITUATION IN WHICH WE HAVE TO WIN
        if "A Z" in line:
            Score2.append(2+6)
       
        if "B Z" in line:   
            Score2.append(3+6)

        if "C Z" in line:
            Score2.append(1 + 6)
    
    print("############################################################################ PART 2 ############################################################################")
    print("Answer Part 2:", sum(Score2))
