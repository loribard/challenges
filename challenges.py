def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?

    Is the word an anagram of a palindrome?

    A palindrome is a word that reads the same forward and backwards (eg, “racecar”, “tacocat”). An anagram is a rescrambling of a word (eg for “racecar”, you could rescramble this as “arceace”).

    Determine if the given word is a re-scrambling of a palindrome.

    The word will only contain lowercase letters, a-z.

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("aab")
    False
    """
    dict_letters = {}
    for character in word:       
        dict_letters[character] = dict_letters.get(character,0) + 1
    single_count = 0
    for key in dict_letters.keys():
        if dict_letters[key] % 2.0 == 0:
            continue
        else:
            single_count+=1

    if single_count <= 1:
        return True
    else:
        return False

print is_anagram_of_palindrome("a")
print is_anagram_of_palindrome("ab")
print is_anagram_of_palindrome("aab")
print is_anagram_of_palindrome("aab")




