def validate_data(height, weight):
    if not (1.00 < height < 2.50 and weight < 200):
        raise ValueError("Invalid height or weight")

def calculate_bmi(height, weight):
    validate_data(height, weight)
    return weight / (height / 100) ** 2