with open('example.txt') as file:
    all_lines = file.readlines()
    print(all_lines)
    for line in all_lines:
        if line == "\n":
            continue
        print(line)
