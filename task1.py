def count_vowels_and_consonants(string):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    for char in string:
        if char.lower() in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1

    counts = {
        "vowels": vowel_count,
        "consonants": consonant_count
    }

    return counts
a = input()
res = dict()
res = count_vowels_and_consonants(a)
print(res)