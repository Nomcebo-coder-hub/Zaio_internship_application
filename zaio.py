def sum_of_even_numbers(arr):
    return sum(num for num in arr if num % 2 == 0)

array = [1, 2, 3, 4, 5, 6]
print(sum_of_even_numbers(array))
