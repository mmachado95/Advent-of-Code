# Used pythons literal sets that make this problem simpler to solve


# First part of the problem
def lonely_santa_moves():
    x, y = 0, 0
    houses = {(x, y)}
    with open("inputs.txt", "r") as file:
        for line in file:
            for char in line:
                print(char)
                if char == '^':
                    y -= 1
                elif char == 'v':
                    y += 1
                elif char == '<':
                    x -= 1
                elif char == '>':
                    x += 1
                houses.add((x, y))
    print(len(houses))


# Second part of the problem
def santa_with_robot_moves():
    x_santa, y_santa = 0, 0
    x_robot, y_robot = 0, 0
    houses = {(0, 0)}
    with open("inputs.txt", "r") as file:
        for line in file:
            char_index = 0
            for char in line:
                if char_index % 2 == 0:
                    if char == '^':
                        y_robot -= 1
                    elif char == 'v':
                        y_robot += 1
                    elif char == '<':
                        x_robot -= 1
                    elif char == '>':
                        x_robot += 1
                    houses.add((x_robot, y_robot))
                else:
                    if char == '^':
                        y_santa -= 1
                    elif char == 'v':
                        y_santa += 1
                    elif char == '<':
                        x_santa -= 1
                    elif char == '>':
                        x_santa += 1
                    houses.add((x_santa, y_santa))
                char_index += 1
    print(len(houses))


if __name__ == '__main__':
    santa_with_robot_moves()