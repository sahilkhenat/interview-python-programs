"""Write a program to count Vowels and Consonants: Count the number of vowels and consonants in a string."""


def count_vowels_and_consonants(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_count = consonant_count = 0
    for char in input_string:
        if char in vowels:
            vowels_count+=1
        else:
            consonant_count+=1
    return vowels_count, consonant_count


def main():
    input_string = input("Enter a string for which you want to find count of vowels and consonants: ")
    vowel_count, consonant_count = count_vowels_and_consonants(input_string)
    print(f"In the given string, number of vowels = {vowel_count}, number of consonants = {consonant_count}")


if __name__ == "__main__":
    main()
