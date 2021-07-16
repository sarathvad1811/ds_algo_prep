class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def getNumNodes(self):
        temp = self.head
        count = 0
        while temp:
            count = count + 1
            temp = temp.next
        return count

    def deleteDuplicates(self):
        if self.head is None or self.head.next is None:
            return self.head

        curr_node = self.head

        while curr_node.next and curr_node:
            if curr_node.data == curr_node.next.data:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next

        return self.head

    def hasCycle(self):
        # solution using visited array and extra space
        #         curr = head
        #         visited = []
        #         while curr.next:
        #             if curr in visited:
        #                 return True
        #         visited.append(curr)
        #         curr = curr.next
        #         return False
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    def printMiddle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    #         numNodes = self.getNumNodes()
    #         i = 0
    #         mid = 0
    #         curr=self.head
    #         if numNodes % 2 != 0:
    #             mid = numNodes//2
    #         else:
    #             mid = numNodes//2 + 1
    #         for i in range(mid):
    #                 curr = curr.next
    #                 i = i + 1
    #         return curr.data
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

        if curr is None:
            print("No elements to display")
            return

        st = ""
        while curr:
            if st != "":
                st = st + " -> " + str(curr.data)
            else:
                st = str(curr.data)
            curr = curr.next

        print(st)

    def reverseLL(self):
        curr_node = self.head
        prev_node = None
        next_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

    def reverseLLRec(self, head):
        if head is None or head.next is None:
            return head
        rest = self.reverseLLRec(head.next)
        head.next.next = head
        head.next = None
        return rest


ll = LinkedList()
ll.insertNode(1)
ll.insertNode(2)
ll.insertNode(3)
ll.insertNode(4)
ll.insertNode(5)
ll.insertNode(6)
ll.insertNode(7)
ll.insertNode(8)
ll.insertNode(9)
ll.__str__()
# print("Count is", ll.getNumNodes())
print("Middle is", ll.printMiddle())
# ll.reverseLL()
# ll.reverseLLRec(ll.getHead())
# print("LinkedList after reversing")
# ll.displayLL()
