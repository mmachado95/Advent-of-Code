# To solve this problem I decided to play a bit around with python generators
def get_dimensions(filename):
    with open(filename, 'r') as handle:
        for line in handle:
            line = line.strip()
            l, w, h = line.split('x')
            yield l, w, h


def wrapping():
    lines = get_dimensions("inputs.txt")
    total_wrapping = 0
    total_ribbon = 0
    try:
        while True:
            line = next(lines)
            ribbon(line)
            area1 = int(line[0]) * int(line[1])
            area2 = int(line[1]) * int(line[2])
            area3 = int(line[2]) * int(line[0])
            # First part of the problem
            total_wrapping += min(area1, area2, area3)
            total_wrapping += 2 * (area1 + area2 + area3)
            # Second part of the problem
            total_ribbon += ribbon(line)
    except StopIteration:
        pass
    print(total_wrapping)
    print(total_ribbon)


# Function to help solve the second part of the problem
def ribbon(dimensions):
    dims = [int(dim) for dim in list(dimensions)]
    l = dims[0]
    w = dims[1]
    h = dims[2]
    min1 = min(dims)
    dims.remove(min1)
    min2 = min(dims)
    return min1 * 2 + min2 * 2 + l * w * h


if __name__ == '__main__':
    wrapping()
