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

    def isPalindrome(self):
        curr = self.head
        stk = []

        while curr:
            stk.append(curr.data)
            curr = curr.next

        curr = self.head
        while curr:
            stk_data = stk.pop()

            if stk_data != curr.data:
                return False
                break

            curr = curr.next

        return True


ll = LinkedList()
ll.insertNode("R")
ll.insertNode("A")
ll.insertNode("D")
ll.insertNode("A")
ll.insertNode("R")
# ll.insertNode("R")
# ll.insertNode("A")
# ll.insertNode("D")
# ll.insertNode("A")
# ll.insertNode("A")
print(ll.isPalindrome())
ll.__str__()
