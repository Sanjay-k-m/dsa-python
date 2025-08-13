class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 
        
    def print_list(self):
        temp = self.head
        if self.length == 0:
            print("List Empty")
        while temp is  not None:
            print(temp.value)
            temp = temp.next
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.length -= 1
        self.tail = pre
        self.tail.next = None
        if self.length == 0:
            self.head = None
            self.tail = None        
        return temp.value
            # print(temp.value)
            # print(pre.value)
    def prepend(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            temp = self.head
            self.head = newNode;
            self.head.next = temp
        self.length +=1
        return True
    def pop_first(self):
        if(self.head.next == None):
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
        self.length -= 1
        return temp.value
    def get(self,index):
            
        temp = self.head;
        current_index = 0
        while current_index !=index+1:
            if current_index == index:
                return temp.value
            current_index += 1 
        
        
                
                
program_running = True
my_ll = LinkedList(input("Enter first number: "))

while program_running:
    print("\nSelect a choice from below:")
    print("1. Print list")
    print("2. Append")
    print("3. Pop")
    print("4. Prepend")
    print("5. Pop First")
    
    print("6. Quit")
    print("7. Get")
    
    
    user_input = input("Enter your choice: ")
    
    if user_input not in ['1', '2', '3', '4', '5','6','7']:
        print("Invalid input. Please enter a number between 1 and 7.")
        continue
    
    if user_input == '1':
        print("\nCurrent Linked List:")
        my_ll.print_list()
    elif user_input == '2':
        num = input("Enter a number to append: ")
        my_ll.append(num)
        print(f"Appended: {num}")
    elif user_input == '3':
        if my_ll.length == 0:
            print("Linked List is empty. Cannot pop.")
        else:
            value = my_ll.pop()
            print(f"Popped: {value}")
    elif user_input == '4':
        num = input("Enter a number to prepend: ")
        my_ll.prepend(num)
        print(f"Prepended: {num}")
    elif user_input == '5':
        if my_ll.length == 0:
            print("Linked List is empty. Cannot pop.")
        else:
            value = my_ll.pop_first()
            print(f"Popped: {value}")   
    elif user_input == '6':
        program_running = False
        print("Goodbye!")
    elif user_input == '7':
        index = int(input("Enter the Index"))
        value = my_ll.get(index)
        if value == None:
            print("Invalid Index")
        else:
            print(f"value for {index} is : {value}")