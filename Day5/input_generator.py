with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    substring = "move"

    for line in lines:
        if substring in line:
            f2 = open("test.txt", "a")
            f2.write(line)
            f2.close()
