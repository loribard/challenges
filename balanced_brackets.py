class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)  


def balanced(stringa):
    s = Stack()
    dict_symbol = {"[":"]","(":")","{":"}"}
    
    index = 0
    while index < len(stringa):
        symbol = stringa[index]
        if symbol == "(" or symbol == "{" or symbol == "[":
            s.push(symbol)
        elif s.size()>0:  
            if symbol == dict_symbol[s.peek()]:
                s.pop()
            else:
                print "NO"
                return
        else:
            print "NO"
            return

        index += 1
    if s.size() == 0:
        print "YES"
    else:
        print "NO"




stringa = "{]]{()}{])"


print balanced(stringa)



