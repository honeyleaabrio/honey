class Student:
        def __init__(self, name, age, course):
         self.name = name
         self.age = age
         self.course = course
    
        def introduce(self):
           print(f"Hello, my name is {self.name}. I am {self.age} years old, and I am studying {self.course}.")

student1 = Student("Janille Jem", 19, "Diploma Information Technology")
student2 = Student("Ma. Darlene", 19, "Nutrition and Dietetics")
student3 = Student("Korina Dell", 20, "Secondary Education Major in English")

student1.introduce()
student2.introduce()
student3.introduce()