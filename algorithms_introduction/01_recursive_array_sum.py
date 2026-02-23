def calculate_sum(numbers, index):
    if index == len(numbers) - 1:
        return numbers[index]

    return numbers[index] + calculate_sum(numbers, index + 1)

nums = [int(num) for num in input().split()]

print(calculate_sum(nums, 0))
