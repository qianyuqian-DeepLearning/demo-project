from utils import calculate_average, get_user_name

print(calculate_average([1, 2, 3]))     # 正常，应该输出 2.0
print(calculate_average([]))              # Bug！会崩溃
print(get_user_name({"name": "Alice"}))   # 正常，应该输出 ALICE
print(get_user_name(None))                # Bug！会崩溃
