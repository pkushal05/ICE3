import unittest


def validate_temp(value: list):
    """Function to validate the input to be within a certain range"""
    if not value:
        return "No input provided!"
    for count in value:
        try:
            count = int(count)
            if not (-50 <= count <= 150):
                raise ValueError("Out-of-bound value detected!")
        except ValueError:
            raise ValueError("Enter integer values")
    return value


# def valid_char(char_value: str):
#     """Function to validate the input to be Y or N"""
#     if char_value in "YyNn":
#         return char_value
#     else:
#         raise ValueError("Please enter Y or N")
#
#
# def get_positive_integer(value: int):
#     """Ensures the user enters a valid non-negative integer"""
#     if value >= 0:
#         return value
#     else:
#         raise ValueError("Please enter a non-negative number.")


def process_temp(validated_list: list):
    """Function to do the final calculations and show required output"""
    if not validated_list:
        return "No input provided!"

    min_temp = min(validated_list)
    max_temp = max(validated_list)
    average_temp = round(sum(validated_list) / len(validated_list), 2)

    return f"Min: {int(min_temp)}\u00b0C, Max: {int(max_temp)}\u00b0C, Avg: {average_temp}\u00b0C"



