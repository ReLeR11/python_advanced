def bubble_sort(nums):
    is_sorted = False
    sorted_nums = 0

    while not is_sorted:
        is_sorted = True

        for j in range(1, len(nums) - sorted_nums):
            i = j - 1
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                is_sorted = False

        sorted_nums += 1

numbers = [int(num) for num in input().split()]
bubble_sort(numbers)
print(*numbers)
