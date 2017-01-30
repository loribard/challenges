 
#double turtle
def palindrome_count(stringa):
    palindrome_count = 0

    for i in range(1,len(stringa)):
        j = 0
        if stringa[i-1] == stringa[i]:
            string_to_look_at = [stringa[i-1],stringa[i]]
        elif (i < len(stringa)-2) and stringa[i-1] == stringa[i+1]:
            string_to_look_at = [stringa[i-1],stringa[i+1]]
        else:
            string_to_look_at = []
        while string_to_look_at and string_to_look_at[0] == string_to_look_at[-1]:
            print "inside while loop"
            print "Palindrome Found!", string_to_look_at
            palindrome_count += 1
            j += 1
            print i, j, string_to_look_at
            if i -j > 0 and i + j <= (len(stringa)-1):
                string_to_look_at = [stringa[i-1-j],stringa[i+j]]
                print string_to_look_at
            else:
                print "breaking"
                break
    print palindrome_count



palindrome_count("abddbacbcc")             














 
            