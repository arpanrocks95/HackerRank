

# Complete the anagram function below.
def anagram(s):
    if len(s) % 2 == 1:
        return -1
    else:
        dict1 = [0] * 26
        count = 0
        for i in range(len(s)):
            if i < int(len(s) / 2):
                dict1[ord(s[i]) - ord('a')] += 1
            else:
                dict1[ord(s[i]) - ord('a')] -= 1
                if dict1[ord(s[i]) - ord('a')] < 0 :
                    count += 1
    return count


if __name__ == '__main__':


    q = int(input())

    for q_itr in range(q):
        s = input()

        print(anagram(s))

