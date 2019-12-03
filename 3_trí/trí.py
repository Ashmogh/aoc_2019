

instr_set_1 = [x for x in open("instr_set_1.txt").read().split(",")]
instr_set_2 = [x for x in open("instr_set_2.txt").read().split(",")]
print(instr_set_1)


def snake_taxi(instructions):
    position = [0, 0]
    all_nodes = []
    for instruction in instructions:
        distance = int(instruction[1:])
        if instruction[0] == "R":
            position[0] += distance
        if instruction[0] == "L":
            position[0] -= distance
        if instruction[0] == "U":
            position[1] -= distance
        if instruction[0] == "D":
            position[1] += distance
        all_nodes.append(position)
        print(position)


if __name__ == "__main__":
    snake_taxi(instr_set_1)