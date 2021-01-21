import os


def read_values_from_file():
    with open(f'{os.getcwd()}/src/day04/input.txt') as file:
        lines = file.read()

    file.close()
    return lines


def validate_date(date, valid_length, valid_start_date, valid_end_date):
    valid_length = len(date) == valid_length
    valid_date_range = valid_start_date <= int(date) <= valid_end_date
    return valid_length and valid_date_range


def validate_byr(byr):
    return validate_date(byr, 4, 1920, 2002)


def validate_iyr(iyr):
    return validate_date(iyr, 4, 2010, 2020)


def validate_eyr(eyr):
    return validate_date(eyr, 4, 2020, 2030)


def validate_hgt(hgt):
    if 'in' not in hgt and 'cm' not in hgt:
        return False

    height_value = hgt[:-2]
    height_type = hgt.replace(height_value, '')

    min_height = 150 if height_type == 'cm' else 59
    max_height = 193 if height_type == 'cm' else 76

    return min_height <= int(height_value) <= max_height


def validate_hcl(hcl):
    """
    valid characters: 0-9 or a-f
    """
    if len(hcl) != 7:
        return False

    if hcl[0] != '#':
        return False

    valid_characters = []
    for i in range(10):
        valid_characters.append(str(i))
        ascii_char = chr(i + 97)
        if ascii_char <= 'f':
            valid_characters.append(ascii_char)

    for char in hcl[1:]:
        if char not in valid_characters:
            return False

    return True


def validate_ecl(ecl):
    valid_eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in valid_eye_colours


def validate_pid(pid):
    return len(pid) == 9


passport_field_validator_map = {
    'byr': validate_byr,
    'iyr': validate_iyr,
    'eyr': validate_eyr,
    'hgt': validate_hgt,
    'hcl': validate_hcl,
    'ecl': validate_ecl,
    'pid': validate_pid,
}


class Day04Solution:

    def part_one(self):
        required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        separated_passports = read_values_from_file().rsplit('\n\n')
        invalid_passwords = 0

        for passport in separated_passports:
            for field in required_fields:
                if not passport.__contains__(field):
                    invalid_passwords += 1
                    break

        return len(separated_passports) - invalid_passwords

    def part_two(self):
        separated_passports = read_values_from_file().rsplit('\n\n')
        valid_passports = [
            passport for passport in separated_passports
            if self.passport_is_valid(passport)
        ]
        return len(valid_passports)

    def passport_is_valid(self, passport):
        required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        for field in required_fields:
            if not passport.__contains__(field):
                return False

        passport_entries = passport.replace(' ', ',').replace('\n', ',').split(',')
        for entry in passport_entries:
            colon_index = entry.index(':')
            passport_field = entry[:colon_index]
            field_value = entry[colon_index + 1:]
            if not self.is_field_valid(passport_field, field_value):
                return False

        return True

    def is_field_valid(self, field, value):
        if field == 'cid':
            return True

        validator = passport_field_validator_map[field]
        return validator(value)
