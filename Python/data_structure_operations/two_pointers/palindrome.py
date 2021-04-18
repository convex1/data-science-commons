"""

~~~IS THE STRING A VALID PALINDROME~~~


Given a string find if it's a palindrome or not i.e. if the string is same witten/read forward or backward


"""


def isPalindrome(s):
    v = [x.lower() for x in list(s) if x.isalnum()]

    if len(v) == 2:
        if v[0] != v[1]:
            return False
        else:
            return True

    mid_point = len(v) // 2

    if len(v) % 2 == 0:
        end_index = mid_point
    else:
        end_index = mid_point + 1

    start_index = mid_point - 1

    while start_index >= 0 and end_index < len(v):

        if v[start_index] != v[end_index]:
            return False

        start_index -= 1
        end_index += 1

    return True




print(isPalindrome("A man, a plan, a canal: Panama"))

print(isPalindrome("A man, a plan"))