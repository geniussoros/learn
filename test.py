class ParentClass:
    def print_test(self):
        print("Parent Method")
 
class ChildClass(ParentClass):
    def print_test(self):
        print("Child Method")
        # 调用父级的 print_test()
        super().print_test() 

child_instance = ChildClass()
child_instance.print_test()

