all_methods = ["meth_one","meth_two","meth_three","meth_four"]

class ObjTest:
    def meth_one(self, a, b):
        return "Test meth_one" + str(a+b)
    
    def meth_two(self, a, b):
        return "Test meth_two" + str(a+b)
    
    def meth_three(self, a, b):
        return "Test meth_three" + str(a+b)
    
    def meth_four(self, a, b):
        return "Test meth_four" + str(a+b)


class CalObj:
    def return_object_list(self):
        obj = ObjTest()
        meth_list = []
        meth_list.append(obj.meth_one)
        meth_list.append(obj.meth_two)
        meth_list.append(obj.meth_three)
        meth_list.append(obj.meth_four)
        return meth_list
        
        
obj1 = CalObj()
test_obj = obj1.return_object_list()
for each_obj in test_obj:
    print(each_obj(2,3))
