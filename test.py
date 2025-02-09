def sum_numbers(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total

def greet(name):
    full_name = name
    print("Hello, " + full_name + "!")

def divide(a, b):
    try:
        return a / b
    except:
        return "Error: Division by zero is not allowed"


def generate_string(n):
    result = ""
    for i in range(n):
        result += "Hello, "
    return result

import math

def calculate_area(radius):
    return radius ** 2


def calculate_area_circle(radius):
    return 3.14 * radius ** 2

def calculate_area_rectangle(width, height):
    return width * height

def calculate_area_triangle(base, height):
    return 0.5 * base * height