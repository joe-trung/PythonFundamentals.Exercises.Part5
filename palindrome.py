def is_palindrome(value: str) -> bool:
    return value.lower().replace(" ", "") == value[::-1].lower().replace(" ","")
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    # i = 0
    # check = True
    # while (i < len(value)) and (check == True):
    #     if value[i] == value[-1-i]:
    #         i = i+1
    #     else:
    #         check = False
    # return check

