

def get_binary(num_to_analize: int) -> str:
    if num_to_analize <= 1:
        return str(num_to_analize)

    return get_binary(num_to_analize // 2) + str(int(num_to_analize % 2))


print(get_binary(233))
print(get_binary(1333))