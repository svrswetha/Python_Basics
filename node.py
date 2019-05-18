class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None

    # def getdata(self):
    #     return self.data
    #
    # def getnext(self):
    #     return self.next_node
    #
    # def setnext(self,new_next):
    #     self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head =  Node()

    def append(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next!= None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next!= None:
            total +=1
            cur = cur.next
        return total

    def display(self):
        elements_list = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elements_list.append(cur.data)
        return elements_list

    def get(self,index):
        if index >= self.length():
            print("ERROR: 'GET' Index out of range! ")
        cur_index = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur_index== index:return cur.data
            cur_index +=1

    def erase(self, index):
        if index >= self.length():
            print("ERROR! 'Erase' Index out of range!")
            return
        cur_index = 0
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur_index == index:
                last_node.next = cur.next
                return
            cur_index +=1




mylist = LinkedList()

# print(mylist.display())

mylist.append(1)

mylist.append(2)


mylist.append(3)
mylist.append(4)


print(mylist.display())

print("elements at 2nd index: %d" % mylist.get(2))

mylist.erase(2)

print(mylist.display())


