class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
                print("Linked list is empty")
                return
        itr = self.head
        count = 0
        while itr:
            if data_after == itr.data:
                itr = self.insert_at(count + 1, data_to_insert)
                return
            else:
                itr = itr.next
                count += 1

    def remove_by_value(self, data):
        if self.head is None:
                print("Linked list is empty")
                return
        itr = self.head
        count = 0
        while itr:
            if data == itr.data:
                itr = itr.next
                self.remove_at(count)
                return
            else:
                itr = itr.next
                count += 1


ll = LinkedList()
ll.insert_values(["Rohit","Rahul","Virat","Surya"])
ll.print()
ll.insert_after_value("Virat","Hardhik")
ll.print()
ll.remove_by_value("Rahul")
ll.print()
ll.remove_by_value("Rohit")
ll.print()
ll.remove_by_value("Surya")
ll.print()
ll.remove_by_value("Hardhik")
ll.print()
ll.remove_by_value("Virat")
ll.print()
