import os
from math import ceil


def read_values_from_file():
    with open(f'{os.getcwd()}/src/day05/input.txt') as file:
        lines = file.read().splitlines()

    file.close()
    return lines
    # return [
    #     'FBFBBFFRLR',
    #     'BFFFBBFRRR',
    #     'FFFBBBFRRR',
    #     'BBFFBBFRLL'
    # ]


class Day05Solution:

    def part_one(self):
        highest_seat_id = 0
        boarding_passes = read_values_from_file()
        for boarding_pass in boarding_passes:
            row_coordinates = boarding_pass[:7]
            column_coordinates = boarding_pass[-3:]

            row = self.i_am_too_lazy_to_properly_name_this_function_sorry(
                inferior_limit=0,
                superior_limit=127,
                lower_half_command='F',
                upper_half_command='B',
                sequence=row_coordinates
            )
            column = self.i_am_too_lazy_to_properly_name_this_function_sorry(
                inferior_limit=0,
                superior_limit=7,
                lower_half_command='L',
                upper_half_command='R',
                sequence=column_coordinates
            )

            seat_id = (row * 8) + column
            if seat_id > highest_seat_id:
                highest_seat_id = seat_id

        return highest_seat_id

    def i_am_too_lazy_to_properly_name_this_function_sorry(
            self,
            inferior_limit,
            superior_limit,
            lower_half_command,
            upper_half_command,
            sequence
    ):
        """
        But it basically iterates through the binaries
        and picks the right value depending on the limit
        and whatnots.
        """
        temp_superior_limit = superior_limit
        temp_inferior_limit = inferior_limit
        for item in sequence:
            if item == lower_half_command:
                temp_superior_limit = (temp_inferior_limit + temp_superior_limit) // 2
            elif item == upper_half_command:
                temp_inferior_limit = ceil((temp_inferior_limit + temp_superior_limit) / 2)

        return temp_inferior_limit

    def part_two(self):
        seat_ids = []
        boarding_passes = read_values_from_file()
        for boarding_pass in boarding_passes:
            row_coordinates = boarding_pass[:7]
            column_coordinates = boarding_pass[-3:]

            row = self.i_am_too_lazy_to_properly_name_this_function_sorry(
                inferior_limit=0,
                superior_limit=127,
                lower_half_command='F',
                upper_half_command='B',
                sequence=row_coordinates
            )
            column = self.i_am_too_lazy_to_properly_name_this_function_sorry(
                inferior_limit=0,
                superior_limit=7,
                lower_half_command='L',
                upper_half_command='R',
                sequence=column_coordinates
            )

            seat_id = (row * 8) + column
            seat_ids.append(seat_id)

        sorted_seat_ids = sorted(seat_ids)
        all_seats = range(sorted_seat_ids[0], sorted_seat_ids[-1])
        for seat in all_seats:
            inferior_value = seat - 1
            superior_value = seat + 1
            seat_ids_contains_both_values = set(list([inferior_value, superior_value])).issubset(set(sorted_seat_ids))
            seat_not_present = seat not in sorted_seat_ids
            if seat_ids_contains_both_values and seat_not_present:
                return seat
