char2 = [ ['F','T','N','Z','M','G','H','J'], ['J','W','V'],  ['H','T','B','J','L','V','G'],  ['L','V','D','C','N','J','P','B'], ['G','R','P','M','S','W','F'], ['M','V','N','B','F','C','H','G'],  ['R','M','G','H','D'],  ['D','Z','V','M','N','H'], ['H','F','N','G'] ]
with open('test.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    tab=[]
    for line in lines:
        x = re.findall('[0-9]+', line)
        tab.append(x)
        if (len(tab)==1):
            char[int(tab[0][2])-1]= list(reversed(char[int(tab[0][1])-1][:int(tab[0][0])]))+char[int(tab[0][2])-1]
            del char[int(tab[0][1])-1][:int(tab[0][0])]
            tab.clear()
    print('\n')
    print("############################################################################ PART 1 ############################################################################")
    print("Answer Part 1:", char)
