def read_file_lines():
    file = open("inputs.txt", "r")
    lines = []
    for line in file:
        lines.append(line)
    file.close()
    return lines


def find_right_floor(inputs):
    curr_floor = 0
    char_position = 0
    for line in inputs:
        for i in range(len(line)):
            # First part of the problem
            if line[i] == '(':
                curr_floor += 1
            else:
                curr_floor -= 1
            # Second part of the problem
            if curr_floor == -1 and char_position == 0:
                char_position = i + 1
    print(char_position)
    print(curr_floor)


if __name__ == '__main__':
    inputs = read_file_lines()
    find_right_floor(inputs)