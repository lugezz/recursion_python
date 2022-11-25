

def is_palindrome(str_to_analize: str) -> bool:
    # Stopping condition
    if len(str_to_analize) <= 1:
        return True

    if str_to_analize[0] == str_to_analize[-1]:
        return is_palindrome(str_to_analize[1:-1])

    return False


list_of_words = ['kayak', 'cachula', 'neuquen', 'anutforajaroftuna',
                 'A nut for a jar of tuna', 'amore, roma']


for word in list_of_words:
    is_pal = '' if is_palindrome(word) else "NOT"
    print(f'{word} is {is_pal} a palindorme')