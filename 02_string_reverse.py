

def string_reverse(str_to_reverse: str) -> str:
    # What is the base case? Empty string
    # What is the smallest amount of work I can do in each iteration. 1 letter
    if str_to_reverse == '':
        return ''
    
    return string_reverse(str_to_reverse[1:]) + str_to_reverse[0]

print(string_reverse('Cachula es Cachula en Neuquén'))