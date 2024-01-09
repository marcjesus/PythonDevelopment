class ClassA:
    def __init__ (self):
        self.value_a = 0

    def set_value(self,val):
        self.value_a = val

    def get_value(self):
        return self.value_a
    

class ClassB:
    def __init__(self):
        self.value_b = 0

    def set_value_from_class_a(self,obj_a):
        self.value_b = obj_a.get_value()

    def get_value(self):
        return self.value_b
    

obj_a = ClassA()
obj_b = ClassB()

obj_a.set_value(11)

obj_b.set_value_from_class_a(obj_a)
value_class_b = obj_b.get_value()

print(f"Class B value is {value_class_b}")