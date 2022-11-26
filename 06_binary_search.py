

def binary_search(list_to_find: list, int_to_find: int, left: int = 0, right: int = -1) -> int:
    this_len = len(list_to_find)
    if right == -1:
        right = this_len

    if left == right:
        return -1

    mid = left + (right - left) // 2

    if list_to_find[mid] == int_to_find:
        return mid
    elif int_to_find < list_to_find[mid]:
        return binary_search(list_to_find, int_to_find, 0, mid-1)
    else:
        return binary_search(list_to_find, int_to_find, mid+1, right)
    

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 10, 22, 33, 44, 50]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 33, 44, 50]

print(binary_search(list1, 9))
print(binary_search(list1, 0))
print(binary_search(list1, 50))
print(binary_search(list1, 43))
print(binary_search(list2, 9))

