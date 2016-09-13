def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome.

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

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses.


    Binary search is one of the most important Computer Science algorithms. It allows you to search a sorted list in O(log n) time, a large improvement over scanning every item in the list (which would be O(n) time).

    To do this, you examine the middle item and, if the sought-for value is smaller, move halfway to the left. If the sought-after value is larger, move halfway to the right.

    Since you use binary search, it will never take more than 7 guesses for a function to find a number in the range 1 to 100 (since log2 100) is just a little under 7).

    For example:

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7"""
    start = 0
    end = 100
    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 1
    guess = int((start+end)/2.0)
    
    while guess != val:

        

        if guess > val:
            end = guess
            
            num_guesses += 1
        elif guess < val:
            start = guess
           
            num_guesses += 1

        guess = int((start + end)/2.0)
        
    return num_guesses

print binary_search(50)
print binary_search(25)
print binary_search(55)
print binary_search(31)
print  ""


def count_recursively(lst,count = None):
    """Return number of items in a list, using recursion.
    >>> count_recursively([])
    0

    >>> count_recursively([1, 2, 3])
    3
    """

    if lst == []:
        return 0

    while lst:
        lst.pop()              
        count = 1 + count_recursively(lst)
        
    return count
      

print count_recursively([1, 2, 3])
print count_recursively([])
print ""

def decode(s):
    """Decode a string.
    >>> decode("0h")
    'h'

    >>> decode("0h1ae2bcy")
    'hey'

    >>> decode("2abh")
    'h'
    """

    final_word = []
    lst = list(s)
    for i in range(0,len(lst)):
        if lst[i].isdigit():
            inc = int(lst[i])
            final_word.append(lst[i + 1 + inc])
    final_word = ''.join(final_word)
    return final_word


print decode("0h")
print decode("2bcd")
print decode("0h1ae2bcy")
print decode("2abh")
print ""

def missing_number(lst,max):
    """
    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8
    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8
    """
    s = set(lst)
    t = set(range(1,max + 1))
    missing = t.difference(s)
    return missing.pop()



print missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
print missing_number([2, 1, 4, 3, 10, 5, 7, 8, 9], 10)
print ""


def pig_latin_word(s):
    """
    >>> pig_latin_word('porcupine are cute')
    'orcupinepay areyay utecay'

    >>> pig_latin_word('give me an apple')
    'ivegay emay anyay appleyay'
    """
    lst_vowels = ["a","e","i","o","u"]
    lst_answer = []
    str = s.split()
    for word in str:
        word_list = list(word)
        if word_list[0] not in lst_vowels:
            word_list.append(word_list[0])
            del word_list[0]
            word_list.extend(("a","y"))
        else:
            word_list.extend(("y","a","y"))
        word = ''.join(word_list)
        lst_answer.append(word)
    return ' '.join(lst_answer)


print pig_latin_word('porcupine are cute')            
print pig_latin_word('give me an apple')
print ""























