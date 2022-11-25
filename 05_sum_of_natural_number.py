

def sum_of_natural_number(my_num: int) -> int:
    if my_num <= 1:
        return my_num

    return my_num + sum_of_natural_number(my_num - 1)


print(sum_of_natural_number(10))
print(sum_of_natural_number(100))
# print(sum_of_natural_number(100)) Recursion error