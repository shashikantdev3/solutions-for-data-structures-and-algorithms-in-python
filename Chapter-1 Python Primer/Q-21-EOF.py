lines = []
try:
    while True:
        line = input("Enter a line: ")
        lines.append(line)
except EOFError:
    lines.reverse()
    for line in lines:
        print(line)