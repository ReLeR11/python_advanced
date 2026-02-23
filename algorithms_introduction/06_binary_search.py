def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle_index = (left + right) // 2
        if nums[middle_index] == target:
            return middle_index

        middle_element = nums[middle_index]

        if middle_element == target:
            return middle_index

        if target < middle_element:
            right = middle_index - 1
        else:
            left = middle_index + 1

    return -1

numbers = [int(num) for num in input().split()]
target_num = int(input())
print(binary_search(numbers, target_num))
