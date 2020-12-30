import os


def read_values_from_file():
    with open(f'{os.getcwd()}/src/day01/input.txt') as file:
        lines = file.readlines()

    file.close()
    return lines


class Day01Solution:

    def part_one(self):
        values = [int(value) for value in read_values_from_file()]
        for x in values:
            for y in values:
                if x + y == 2020:
                    return x * y

    def part_two(self):
        values = [int(value) for value in read_values_from_file()]
        for x in values:
            for y in values:
                for z in values:
                    if x + y + z == 2020:
                        return x * y * z
