def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)  # Bug 1：空列表会除零报错

def get_user_name(user):
    return user["name"].upper()  # Bug 2：如果 user 是 None 会报错
