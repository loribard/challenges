class Tracker(object):
  

    def  __init__(self, name = "Bimbo", dict_list = None):
        self.name = name
        self.dict_list = dict_list
        

    def allocate(self, name, dict_list = None):
        self.name = name
        self.answer = self.get_server(self.name, self.dict_list)
        self.number = str(self.answer[0])
        self.dict_list = self.answer[1]
        print self.dict_list
        print self.name + self.number

        
    def get_server(self, name, dict_list):
        self.name = name
        if self.dict_list == None:
            self.dict_list = {}
        if self.name not in self.dict_list.keys():
            self.dict_list[self.name] = [1]
            return [1,self.dict_list]
        elif self.dict_list[self.name] == [1]:
            self.dict_list[self.name] = [1,2]
            return [2,self.dict_list]
        elif self.dict_list[self.name][0] != 1:
            self.dict_list[self.name].append(1)
            self.dict_list[self.name].sort()
            return [1,self.dict_list]
        else:
            for i in range(len(self.dict_list[self.name]) - 1):
                if self.dict_list[self.name][i] != self.dict_list[self.name][i+1] - 1:
                    self.dict_list[self.name].append(i+1)
                    self.dict_list[self.name].sort()
                    return [i+1,self.dict_list]
        self.dict_list[self.name].append(len(self.dict_list[self.name]) + 1)
        return [(len(self.dict_list[self.name])),self.dict_list]

    def deallocate(self,server_name):

        self.server_name = server_name
        print self.server_name
        self.name = ""
        self.number = ''
        for char in self.server_name:
            if char.isalpha():
                print char
                self.name += char
            else:
                print "Number:",char
                self.number += char
        self.number = int(self.number)       
        print self.name, self.number
        print self.dict_list
        if self.number in self.dict_list[self.name]:
            self.dict_list[self.name].remove(self.number)
            print self.dict_list
            return self.dict_list
        else:
            print "No such server exists"

       

        
      


        

# https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort

tracker = Tracker()
tracker.allocate("apibox")
tracker.allocate("apibox")
tracker.allocate("hello")
tracker.allocate("apibox")
tracker.deallocate("apibox1")
tracker.allocate("apibox")
tracker.allocate("apibox")
tracker.allocate("sitebox")
tracker.allocate("hello")



# >> tracker = Tracker()
# >> tracker.allocate('apibox')
# "apibox1"
# >> tracker.allocate('apibox')
# "apibox2"
# >> tracker.allocate('apibox')
# "apibox3"
# >> tracker.deallocate('apibox1')
# True
# >> tracker.deallocate('apibox')
# error/False
# >> tracker.allocate('apibox')
# "apibox1"
# >> tracker.allocate('apibox')
# "apibox4"
# >> tracker.allocate('sitebox')
# "sitebox1"
# >> tracker.allocate('hello')
# "hello1"
