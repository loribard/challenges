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


def primes(count):
    """
    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]
    """
    num = 3
    prime_number = [2]

    while len(prime_number) < count:

        for i in range(0,len(prime_number)):
            print "i", i, "prime number", prime_number[i], "num", num, prime_number
            if num % prime_number[i] == 0:
                print "num", num,"breaking",prime_number[i]
                num += 1
                break
            elif i == len(prime_number) - 1:
                prime_number.append(num)
                num += 1


    print prime_number
    return prime_number

primes(1)  
primes(2)  
primes(4) 
primes(7)   

def print_digits(num):
    """Given an integer, print each digit in reverse order, starting with the ones place.

    For example, if you were given 1 you should simply print 1, if given 314 you should print 4, 1, 3, and if given 12 you should print 2, 1:

    >>> `print_digits(1)`:cmd:
    1
    >>> `print_digits(314)`:cmd:
    4
    1
    3
    >>> `print_digits(12)`:cmd:
    2
    1
    """

    num = list(str(num))

    for i in range(0,len(num)):
        print num.pop()

 

print " "
print_digits(1)
print_digits(314)
print_digits(12)

def print_recursively(lst):
    """Print items from a list using recursion.

    For example, if you have a list of [1, 2, 3]:

    >>> print_recursively([1, 2, 3])
    1
    2
    3
    """
    if lst:
        print lst.pop(0)
        print_recursively(lst)

print ""
print_recursively([1,2,3])


def recursive_index(needle, haystack, start_at=None):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """
    if start_at == len(haystack):
        return None

    if haystack[start_at] == needle:
        return start_at

    return recursive_index(needle,haystack,start_at + 1)
   
    


print ""
print recursive_index("I",["hey","there","you"],0)
print recursive_index("you",["hey","there","you"],0)



# """Given a node in a linked list, remove it.

# Remove this node from a linked list. Note that we do not have access to
# any other nodes of the linked list, like the head or the tail.

# Does not return anything; changes list in place.

# For example::

#     >>> ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))  # 1->2->3->4->5
#     >>> three_node = ll.next.next
#     >>> remove_node(three_node)
#     >>> ll.as_string()
#     '1245'

# It's possible to remove the first node::

#     >>> ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))  # 1->2->3->4->5
#     >>> one_node = ll
#     >>> remove_node(one_node)
#     >>> ll.as_string()
#     '2345'

# This will never be asked to remove the tail node.
# """

# class Node(object):
#     """Class in a linked list."""

#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

#     def as_string(self):
#         """Represent data for this node and it's successors as a string.

#         >>> Node(3).as_string()
#         '3'

#         >>> Node(3, Node(2, Node(1))).as_string()
#         '321'
#         """

#         out = []
#         n = self

#         while n:
#             out.append(str(n.data))
#             n = n.next

#         return "".join(out)


# def remove_node(node):
#     """Given a node in a linked list, remove it.

#     Remove this node from a linked list. Note that we do not have access to
#     any other nodes of the linked list, like the head or the tail.

#     Does not return anything; changes list in place.
#     """

    

#     if not node.next:
#         raise ValueError("Cannot remove tail node")

#     node.data = node.next.data
#     node.next = node.next.next

# print ""

# ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))  # 1->2->3->4->5
# print ll.as_string()
# three_node = ll.next.next
# remove_node(three_node)
# print ll.as_string()
   

# print ""
# ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))  # 1->2->3->4->5
# print ll.as_string()
# one_node = ll
# remove_node(one_node)
# print ll.as_string()
# print ""

# class Node(object):
#     """Class in a linked list."""

#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

#     def as_string(self):
#         """Represent data for this node and it's successors as a string.

#         >>> Node(3).as_string()
#         '3'

#         >>> Node(3, Node(2, Node(1))).as_string()
#         '321'
#         """

#         out = []
#         n = self

#         while n:
#             out.append(str(n.data))
#             n = n.next

#         return "".join(out)


# def reverse_linked_list(head):
#     """Given LL head node, return head node of new, reversed linked list.

#     >>> ll = Node(1, Node(2, Node(3)))
#     >>> reverse_linked_list(ll).as_string()
#     '321'
#     """

#     list_of_nodes = []
#     for 


# ll = Node(1, Node(2, Node(3)))
# new_ll = reverse_linked_list(ll)
# new_ll.as_string()   #321
print "'"

#Tower of Hanoi


def tower(n):

    source = "a"
    spare = "b"
    dest = "c"
    move_disc(n,source,dest,spare)

def move_disc(n,source,dest,spare):

    if n ==1:
        print source,spare

    else:
        move_disc(n-1,source,spare,dest)
        move_disc(1,source,dest,spare)
        move_disc(n-1,spare,dest,source)


print tower(3)


# LINKED LISTS
 
# def InsertNth(head, data, position):
   
   
#     if head is None or position == 0:
#         new_node = Node(data)
#         new_node.next = head
#         head = new_node
#     else:
#         current_position = 0
#         current = head
#         while current.next is not None:
#           if current_position == position - 1:
#             new_node = Node(data)
#             new_node.next = current.next
#             current.next = new_node
#             break
#           else:
#             current = current.next
#           current_position += 1
#         if position > current_position and current.next is None:
#             current.next = Node (data)
#     return head


# SAVE HUMANITY HACKERRANK TIMED OUT ON SOME EXAMPLES

# # Enter your code here. Read input from STDIN. Print output to STDOUT

# number_of_test_cases = raw_input()
# number_of_test_cases = int(number_of_test_cases)
# if number_of_test_cases == 0:
#     print "No Match!"      
# for test_case in range(number_of_test_cases):
#     PV = raw_input()
#     P,V = PV.split()
#     answer = []
#     testln = len(V)
#     patientln = len(P)
#     if testln > patientln:
#         print "No Match"
#     for i in range(patientln-testln+1):
#         Psub = P[i:i+testln]
#         if sum(Psub[i] != V[i] for i in range(len(V)))>=2:
#             i += 1
#         else:
#             answer.append(i)
#             i +=1     
#     if len(answer) == 0:
#         print "No Match!"
#     else:
#         string_answer = ""
#         for item in answer:
#             string_answer += str(item) + " "
#         print string_answer
        

# DELETE A NODE FROM A LINKED LIST

#  def Delete(head, position):
#     current = head
#     current_position = 0
#     if position == 0:
#         head = current.next
#         return head
#     while current.next:
#         if current_position == position - 1:
#             current.next = cugrrent.next.next
#             return head

#         else:
#             current=current.next
#             current_position += 1   



def flatten_dict_1(d):
    result = {}
    agenda = {}

    agenda = d.copy()

    while True:
        new_agenda = {}

        for (k,v) in agenda.iteritems():
            if type(v) == int:
                result[k]= v
            else:

                for (k2, v2) in v.iteritems():
                    if type(v2) == int:
                        result[str(k) + '.' + str(k2)] = v2
                    else:
                        new_agenda[str(k) + '.' + str(k2)] = v2
        if len(new_agenda) == 0:
            break
        else:
            agenda = new_agenda
    print result
    return result

            
d = {1:2,3:4,5:{6:{7:{8:9}}}}
flatten_dict_1(d)







print ""
print ""

def flatten_dict_recursion(d):
  
    for k,v in d.iteritems():
      
        if type(v) != int:      
            
            new_k = v.keys()[0]
            k1 = str(k) + "." + str(new_k)
            d[k1] =  v.values()[0]
            del d[k]
            flatten_dict_recursion(d)
    return d


d = {1:2,3:4,5:{6:{7:{8:9}}}}
print flatten_dict_recursion(d)






          



























