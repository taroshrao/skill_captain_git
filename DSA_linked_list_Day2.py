class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_List:
    
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:  # Checking for an empty list
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1  # Incrementing length
    
    def reverse_list(self):
        self.head, self.tail = self.tail, self.head  # Swapping head and tail
        before = None
        temp = self.tail  # Use self.head instead of self.tail
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def print_list(self):
        if self.length == 0:
            print("List is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.value, end=",")
            temp = temp.next
        print()
        

if __name__ == "__main__":
    my_list = Linked_List(1)  # Creating an instance of Linked_List
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    

    print("Original list:")
    my_list.print_list()

    my_list.reverse_list()

    print("Reversed list:")
    my_list.print_list()
