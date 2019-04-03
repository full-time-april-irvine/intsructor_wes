class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        return self

    def display(self):
        result = []
        curr_node = self.head
        while(curr_node != None):
            result.append(curr_node.val)
            curr_node = curr_node.next
        print(result)
        return self


my_list = SList()
my_list.add_front("D").add_front(10).add_front("B").add_front("A")
my_list.display() # ["A", "B", "C", "D"]






# {
#     "val": "A",
#     "next": {
#         "val": "B",
#         "next": {
#             "val": "C",
#             "next": {
#                 "val": "D",
#                 "next": None
#             }
#         }
#     }
# }