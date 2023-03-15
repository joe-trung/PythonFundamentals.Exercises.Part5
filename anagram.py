def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    # check = False
    # if len(first_string) == len(second_string):
    # for letter in first_string:
    #     if letter in second_string:
    #         check = True
    # return check

    return sorted(first_string) == sorted(second_string)