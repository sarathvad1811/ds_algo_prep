class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def insertNode(self, data):
        newNode = Node(data)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
        else:
            self.head = newNode

    def __str__(self):
        curr = self.getHead()

        st = ""
        while curr:
            if st != "":
                st = st + " -> " + str(curr.data)
            else:
                st = str(curr.data)
            curr = curr.next

        print(st)

    def nthFromEnd(self, n):
        curr = self.head
        count = 0
        i = 0

        while curr:
            count = count + 1
            curr = curr.next

        curr = self.head

        for i in range(1, count + 1):
            if i == count + 1 - n:
                return curr.data
            curr = curr.next


ll = LinkedList()
ll.insertNode("R")
ll.insertNode("A")
ll.insertNode("D")
ll.insertNode("A")
ll.insertNode("R")
print(ll.nthFromEnd(3))
ll.__str__()
