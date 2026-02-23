def sum_numbers(*args):
    neg_num = 0
    pos_num = 0
    for num in args:
        if num < 0:
            neg_num += num
        else:
            pos_num += num

    return neg_num, pos_num


numbers = [int(x) for x in input().split()]
negative_numbers, positive_numbers = sum_numbers(*numbers)

print(negative_numbers)
print(positive_numbers)

if abs(negative_numbers) > positive_numbers:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
