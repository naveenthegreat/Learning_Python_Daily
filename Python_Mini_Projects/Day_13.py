class employee:

    company_name = "FusionDragon"

    def __init__(self,name,salary):                     # Constructor (Instance Variables)
        self.name = name
        self.salary = salary
        
    def show_details(self):                             # Instance Method
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")

    @classmethod
    def change_company_name(cls,new_name):              # Class Method
        cls.company_name = new_name
        print(f"\nCompany name is change to {cls.company_name}\n")

    @staticmethod
    def company_policy():                               # Static Method
        print("\nCompany Policy :")
        print("1. Be Punctual")
        print("2. Maintain Professionalism")


# Creating Objects(Employees) :
e1 = employee("Naveen",5000000)
e2 = employee("Gayatri",5000000)

# Show details of each employee :
e1.show_details()
print("----------")
e2.show_details()

# Change Company name using class method :
employee.change_company_name("Codecafe")

# Show Updated Company name for both :
e1.show_details()
print("----------")
e2.show_details()

# Call Static Method :
employee.company_policy()