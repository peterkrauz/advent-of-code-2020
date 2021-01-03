import os


def read_values_from_file():
    with open(f'{os.getcwd()}/src/day03/input.txt') as file:
        lines = file.read().splitlines()

    file.close()
    return lines


class Day03Solution:

    def part_one(self):
        course_matrix = [[square for square in list(line)] for line in read_values_from_file()]
        longitude = 0
        trees_in_the_way = 0
        for course_line in course_matrix:
            next_step = course_line[longitude % len(course_line)]
            if next_step == '#':
                trees_in_the_way += 1
            longitude += 3
        return trees_in_the_way

    def part_two(self):
        course_matrix = [[square for square in list(line)] for line in read_values_from_file()]
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        total_trees = []

        for slope in slopes:
            trees_in_the_way = 0
            longitude = 0
            longitude_step = slope[0]
            latitude_step = slope[1]

            for course_line in course_matrix[::latitude_step]:
                next_step = course_line[longitude % len(course_line)]
                if next_step == '#':
                    trees_in_the_way += 1
                longitude += longitude_step

            total_trees.append(trees_in_the_way)

        total_trees_in_the_way = 1
        for count in total_trees:
            total_trees_in_the_way *= count
        return total_trees_in_the_way
