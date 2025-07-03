# Mini Challenge: Inheritance (Oops 1st Pillar)

class person:
    name = "Naveen"
    age = 23
    def introduce(self):
        print("He is genius employer")
    
class employee(person):
    job_title = "DevOps Engineer"
    salary = 50,00,000                      #50,00,000 ❌ 5000000 or 5_000_000 ✅
    def introduce(self):
        super().introduce()          
    
e=employee()
e.introduce()

