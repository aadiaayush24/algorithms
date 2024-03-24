''' Two Pointer technique explained:
1) Two pointers to maintain track of two separate indices of array(s).
2) The pointers can either both start from one direction, or from opposite directions.
3) The pointers move as per a condition is matched.
'''

def isSubsequence1(str1: str, str2: str):
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

'''
Adding a recursive solution to check for subsequence.
'''
def isSubsequence2(s: str, t: str) -> bool:
    if t == '':
        return True
    elif s == '':
        return False
    else:
        if t[0] == s[0]:
            return isSubsequence2(s[1:], t[1:])
        else:
            return isSubsequence2(s[1:], t)

if __name__ == "__main__":
    print(isSubsequence1("abcddef", "abdf"))
    print(isSubsequence2("abcddef", "abdf"))
