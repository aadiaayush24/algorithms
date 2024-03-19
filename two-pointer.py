''' Two Pointer technique explained:
1) Two pointers to maintain track of two separate indices of array(s).
2) The pointers can either both start from one direction, or from opposite directions.
3) The pointers move as per a condition is matched.
'''


def isSubsequence(str1: str, str2: str):
    i, j = 0, 0
    lenStr, lenSub = len(str1), len(str2)
    while (i < lenStr):
        if (str1[i] == str2[j]):
            j += 1
        if j == lenSub:
            return True
        i += 1

    if j == lenSub:
        return True
    else:
        return False

if __name__ == "__main__":
    print(isSubsequence("abcddef", "abdf"))
