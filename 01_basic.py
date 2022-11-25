
def message3():
    return "Friend!"


def message2():
    return "my " + message3()


def split_message():
    return "Hello " + message2()


print(split_message())