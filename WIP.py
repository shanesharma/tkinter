class node:
    def __init__(self, val):
        self.next = None
        self.val = val
        self.history = set()
    def set_link(self, link):
        self.next = link
    def get_history(self):
        return self.history
    

class obj:
    def __init__(self, data, children = ()):
        self.data = data
        self.prev = set(children)

    def __add__(self, other):
        ret = self.data + other.data
        return(ret, (self, other))
    
    def child_tree(self):
        if(len(self.prev) == 0):
            print(self.data)
        else:
            for i in range(len(self.prev)):
                child_tree()

    



if __name__ == '__main__':
    x_1 = node(1)

    x_2 = node(2)
    x_1.set_link(x_2)
    x_3 = node(3)
    x_2.set_link(x_3)
    

    for i in x_3.history:
        print(i)

    a = obj(2)
    b = obj(3)
    c = a+b
    print(c)


    
    
