import csv
class School:
    def __init__(self , Name , Age):
        self.Name = Name
        self.Age = Age
        
       

    def info(self):
        print("----Student Info----")
        print(f"Name Of Student is {self.Name}")
        print(f"{self.Name} is a student of class {self.Class}")
        print(f"Age Of Student is {self.Age}")
        print(f"Roll no. Of Student is {self.Roll_no}")
        print(f"Percentage of {self.Name} is {self.Percentage}")


class students (School):
    def __init__(self , Name , Class , Age , Roll_no , Percentage):
        super().__init__(Name,Age)
        self.Class = Class
        self.Roll_no = Roll_no
        self.Percentage = Percentage

    def studentinfo(self):
        print(f"The Name Of the Student is {self.Name}, and its Roll no. is {self.Roll_no}")

        with open ("students.csv","a") as f1:
            writer = csv.writer(f1)
                        
            writer.writerow([f"{self.Name}" , f"{self.Class}" , f"{self.Age}", f"{self.Roll_no}" , f"{self.Percentage}"])
            print("Data entered successfully !")

class teachers (School):
    def __init__(self , Name , Age , subject , salary  ):
        super().__init__(Name , Age)
        self.subject = subject
        self.salary = salary
        

    def teacherinfo(self):
        print(f"The Name Of the Teacher is {self.Name}, and his subject is {self.subject}")

        with open ("Teachers.csv","a") as f1:
            writer = csv.writer(f1)
                        
            writer.writerow([f"{self.Name}" , f"{self.Age}", f"{self.subject}" , f"{self.salary}"])
            print("Data entered successfully !")

print("For Students Enter 'S'")
print("For Teachers Enter 'T'")


choice = input("Enter here : ")

if choice == "S":
    a = input("Entr Student name : ")
    b = input("Enter Student class : ")
    c = int(input("Enter Student age : "))
    d = int(input("Enter roll no. : "))
    e = float(input("Enter Student Percentage % : "))
              
    x = students(a,b,c,d,e)
    x.studentinfo()

elif choice == "T":

    A = input("Entr Teacher's name : ")
    B = int(input("Enter Teacher's age : "))
    C = input("Enter Teacher's teaching Subject : ")
    D = int(input("Enter Teacher's Salary : "))
              
    y = teachers(A,B,C,D)
    y.teacherinfo()