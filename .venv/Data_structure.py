import array

class data:
    def __init__(self, arr_type):
        self.arr_node = array.array(arr_type, [])

    ## Working
    def append(self, value):
        self.arr_node.append(value)

    ## Working
    def prepend(self, value):
        self.arr_node.insert(0, value)

    ## Working
    def size(self):
        return len(self.arr_node)

    ## Working
    def head(self):
        return self.arr_node[0]

    ## Working
    def tail(self):
        return self.arr_node[-1]

    ## Working
    def index(self,x):
        return self.arr_node[x]

    ## Working
    def pop(self):
        #python does -0 for the last position in the array
        self.arr_node[-0] = self.arr_node.pop()

    ## Working
    def contains(self, item):
        return item in self.arr_node

    ## Working
    def find(self, item):
        for index, value in enumerate(self.arr_node):
            if value == item:
                return index, item

    ## Working
    def print(self):
        for node in self.arr_node:
            print(node)