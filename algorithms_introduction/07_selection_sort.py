def selection_sort(nums):
    for index in range(len(nums)):
        min_index = index

        for current_index in range(index + 1, len(nums)):
            if nums[current_index] < nums[min_index]:
                min_index = current_index

        nums[index], nums[min_index] = nums[min_index], nums[index]

numbers = [int(num) for num in input().split()]
selection_sort(numbers)
print(*numbers)
