    # Name: Kushal Patel
    # Date: 5th March 2025
    # Title: ICE3 (Temperature sensors)
    # Desc: This is the source code for ICE3

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

def process_temp(validated_list: list):
    """Function to do the final calculations and show the required output"""
    if not validated_list:
        return "No input provided!"

    min_temp = min(validated_list)
    max_temp = max(validated_list)
    average_temp = round(sum(validated_list) / len(validated_list), 2)

    return f"Min: {int(min_temp)}°C, Max: {int(max_temp)}°C, Avg: {average_temp}°C"