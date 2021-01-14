
def flooring_cost(width, length, unit_cost) -> float:
    """Estimates the total cost of flooring based on area and unit price of
    materials.

    Args:
        width (float):
        length (float):
        unit_cost (float):

    Returns:
        float: Total cost rounded to two decimals.

    """
    area = float(width) * float(length)
    total = area * float(unit_cost)
    return abs(round(total, 2))


if __name__ == '__main__':

    user_width = abs(float(input('Enter the width: ')))
    user_length = abs(float(input('Enter the length: ')))
    user_unit_cost = abs(float(input('Enter the unit cost per square unit: ')))

    result = flooring_cost(user_width, user_length, user_unit_cost)

    response = 'A room {0} unit(s) wide by {1} unit(s) long has a total estimated cost of {2}.'
    print(response.format(user_width, user_length, result))
