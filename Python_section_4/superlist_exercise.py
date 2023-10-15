class SuperList(list):
    def __init__(self, list : list):
        self.list = list

    def __len__(self):
        return 1000
    
    def __call__(self):
        print('__call__')
        print(self.list)

#len  - modify. return 1000

super_list1 = SuperList([1,2,3,4,5])
print(len(super_list1))
print((super_list1()))

print(issubclass(list, object))


