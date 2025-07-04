# Mini Challenge: Encapsulation

class studentrecord:
    def __init__(self,name,marks):
        self.__name = name              #private variables for name
        self.__marks = marks            #private variables for marks

    def add_marks(self,new_marks):
        if new_marks > 0:
            self.__marks += new_marks
        else:
            print("Invalid Mark Value. Must Be Positive")

    def check_pass(self):
        if self.__marks >= 35:
            print(f"\n{self.__name} has passed with marks {self.__marks}\n")
        else:
            print(f"\n{self.__name} has failed with marks {self.__marks}\n")

    @property
    def name(self):
        return self.__name
    
    @property
    def marks(self):
        return self.__marks
    
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("❌ Marks should be between 0 and 100.\n")

s1=studentrecord("Naveen", 30)
# Try accessing private variables directly (will fail)
# print(s1.__name)  ❌ AttributeError

print(s1.name)
print(s1.marks)

s1.add_marks(10)
print(s1.add_marks)

s1.check_pass()

s1.marks = 150     # ❌ Warning
s1.marks = 90      # ✅ Updated
print(s1.marks)    # ✅ 90