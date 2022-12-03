with open('input.txt', 'r', encoding="utf-8") as f3:
    lines2 = f3.readlines()
    tab=[]
    tab_score=[]
    char_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    thisdict = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5,"f": 6,"g": 7,"h": 8,"i": 9,"j": 10,"k": 11,"l": 12,"m": 13,"n": 14,"o": 15,"p": 16,"q": 17,"r": 18,"s": 19,"t": 20,"u": 21,"v": 22,"w": 23,"x": 24,"y": 25,"z": 26,"A": 27,"B": 28,"C": 29,"D": 30,"E": 31,"F": 32,"G": 33,"H": 34,"I": 35,"J": 36,"K": 37,"L": 38,"M": 39,"N": 40,"O": 41,"P": 42,"Q": 43,"R": 44,"S": 45,"T": 46,"U": 47,"V": 48,"W": 49,"X": 50,"Y": 51,"Z": 52}

    for line2 in lines2:
        a= int((len(line2)-1)/2)
        for x in char_list:
            if x in line2[a:] and x in line2[:a]:
                tab.append(x)    
    for y in tab:
        if y in thisdict:
            tab_score.append(thisdict[y]) 
    print("############################################################################ PART 1 ############################################################################")
    print("Answer Part 1", sum(tab_score))


with open('test.txt', 'r', encoding="utf-8") as f3:
    lines2 = f3.readlines()
    count = 0
    my_list = [] 
    tab=[]
    tab_score=[]
    char_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    thisdict = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5,"f": 6,"g": 7,"h": 8,"i": 9,"j": 10,"k": 11,"l": 12,"m": 13,"n": 14,"o": 15,"p": 16,"q": 17,"r": 18,"s": 19,"t": 20,"u": 21,"v": 22,"w": 23,"x": 24,"y": 25,"z": 26,"A": 27,"B": 28,"C": 29,"D": 30,"E": 31,"F": 32,"G": 33,"H": 34,"I": 35,"J": 36,"K": 37,"L": 38,"M": 39,"N": 40,"O": 41,"P": 42,"Q": 43,"R": 44,"S": 45,"T": 46,"U": 47,"V": 48,"W": 49,"X": 50,"Y": 51,"Z": 52}
    for line2 in lines2:
        my_list.append(line2)
        if len(line2)== 1:
            for x in char_list:
                if x in my_list[0] and  x in my_list[1] and x in my_list[2]:
                    tab.append(x)
            my_list.clear()
    for a in tab:
        if a in thisdict:
            tab_score.append(thisdict[a]) 
    print("############################################################################ PART 2 ############################################################################")
    print("Answer Part 2",sum(tab_score))
