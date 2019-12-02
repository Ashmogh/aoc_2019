import operator

int_code = [int(x) for x in open("source.txt").read().split(",")]
operator_chart = {
    "1": operator.add,
    "2": operator.mul
}


def get(array, i, pos):
    return array[array[i + pos]]


# ------- Part 1 -------
def magic_smoke(array):
    halt = 99
    for i in range(0, len(array), 4):
        opcode = str(array[i])
        op = operator_chart.get(opcode)
        if op is not None:
            array[array[i + 3]] = op(get(array, i, 1), get(array, i, 2))
        elif array[i] == halt:
            return array
        else:
            print("Invalid opcode")


# ------- Part 2 -------
def jack_in_the_box(array, wanted):
    for i in range(0, 99):
        for j in range(0, 99):
            arr_copy = array[:]
            arr_copy[1], arr_copy[2] = i, j
            result = magic_smoke(arr_copy)[0]
            if result == wanted:
                return 100 * i + j


if __name__ == "__main__":
    # print(jack_in_the_box(int_code, 19690720))
    print(magic_smoke(int_code))
