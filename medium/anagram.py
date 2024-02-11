"""Anagram Check: Write a function to check if two strings are anagrams of each other. An anagram is a word or phrase
formed by rearranging the letters of another word or phrase, using all the original letters exactly once. In other
words, an anagram of a word is a permutation of its letters that results in a new word or phrase. For example: The
word "listen" is an anagram of "silent". The word "heart" is an anagram of "earth". The phrase "angel" is an anagram
of "glean". """


def anagram_check(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        chars_dict1 = dict()
        chars_dict2 = dict()
        # For string1 , extract counts of all unique characters
        for i in string1:
            if i not in chars_dict1.keys():
                count_of_i = string1.count(i)
                chars_dict1[i] = count_of_i

        # For string2 , extract counts of all unique characters
        for j in string2:
            if j not in chars_dict2.keys():
                count_of_j = string2.count(j)
                chars_dict2[j] = count_of_j

        # Sort the dictionaries by keys
        sorted_dict1 = {k: chars_dict1[k] for k in sorted(chars_dict1)}
        sorted_dict2 = {k: chars_dict2[k] for k in sorted(chars_dict2)}

        if sorted_dict1 == sorted_dict2:
            return True
        else:
            return False


def main():
    print("-------Palindrome check--------")
    string1 = input("Enter first string:")
    string2 = input("Enter second string:")
    if anagram_check(string1, string2):
        print(f'{string1} and {string2} are anagrams')
    else:
        print(f'{string1} and {string2} are not anagrams')


if __name__ == "__main__":
    main()
