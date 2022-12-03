with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        count += 1
        if(count % 3 == 0):
            f2 = open("test.txt", "a")
            f2.write(line)
            f2.write("\n")
            f2.close()

        else:
            f2 = open("test.txt", "a")
            f2.write(line)
            f2.close()
