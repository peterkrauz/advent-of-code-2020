import os


def read_values_from_file():
    with open(f'{os.getcwd()}/src/day02/input.txt') as file:
        lines = file.readlines()

    file.close()
    return lines


class Day02Solution:

    def dismember_entry_into_policy_and_password(self, password_entry):
        colon_index = password_entry.index(':')
        password_policy = password_entry[:colon_index]
        password = password_entry[1 + colon_index:].strip()
        return password_policy, password

    def get_values_from_entry_tuple(self, policy):
        dash_index = policy.index('-')
        minimum_character_occurrences = int(policy[:dash_index])
        maximum_character_occurrences = int(policy[1 + dash_index:3 + dash_index])
        return minimum_character_occurrences, maximum_character_occurrences

    def count_character_occurrences(self, password, policy_character):
        character_occurrences = 0
        for character in password:
            if character == policy_character:
                character_occurrences += 1
        return character_occurrences

    def part_one(self):
        valid_passwords = 0

        for password_entry in read_values_from_file():
            policy, password = self.dismember_entry_into_policy_and_password(password_entry)
            min_occurrences, max_occurrences = self.get_values_from_entry_tuple(policy)

            policy_character = policy[len(policy) - 1]
            character_occurrences = self.count_character_occurrences(password, policy_character)

            if min_occurrences <= character_occurrences <= max_occurrences:
                valid_passwords += 1

        return valid_passwords

    def part_two(self):
        valid_passwords = 0

        for password_entry in read_values_from_file():
            policy, password = self.dismember_entry_into_policy_and_password(password_entry)
            first_position, second_position = self.get_values_from_entry_tuple(policy)
            policy_character = policy[len(policy) - 1]

            first_occurrence = password[first_position - 1]
            second_occurrence = password[second_position - 1]

            matches_first = first_occurrence == policy_character
            matches_second = second_occurrence == policy_character
            match_exists = matches_first or matches_second
            if match_exists and first_occurrence != second_occurrence:
                valid_passwords += 1

        return valid_passwords
