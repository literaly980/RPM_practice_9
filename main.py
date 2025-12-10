import ctypes
import os
import sys

LIB_NAME = "math_lib.dll"

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(current_dir, LIB_NAME)

try:
    math_lib = ctypes.CDLL(lib_path)
    print("Успех")
except Exception as e:
    print("Ошибка")
    sys.exit(1)

math_lib.calculate_circle_area.argtypes = [ctypes.c_double]
math_lib.calculate_circle_area.restype = ctypes.c_double

radius_value = 5.0
area = math_lib.calculate_circle_area(radius_value)

print(f"\nВызов C++ функции: calculate_circle_area({radius_value})")
print(f"Площадь круга с радиусом {radius_value} равна {area:.4f}")
