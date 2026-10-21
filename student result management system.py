class student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.subject = []
        self.marks = []
        

    def display_details(self):
        print("\n\n=============================")
        print("      STUDENT REPORT          ")
        print("=============================\n")
        print("name:", self.name)
        print("roll no:",self.roll_no, "\n")
        print("subject         marks")
        print("------------------------")
        for i in range(len(self.subject)):
           print(f"{self.subject[i]}\t\t{self.marks[i]}")

        print("\nTotal Marks:",sum(self.marks),"/",(100*len(self.marks)))
        for i in range(len(self.marks)):
            if self.marks[i] <33:
                print("RESULT : Fail")
                print(f"Failed Subjects: {self.subject[i]}")
                break
        else:
            print("RESULT : Pass")

    @property
    def percentage(self):
        return f"{sum(self.marks)/len(self.marks):.2f}%"

    def add_subject(self,no):
        self.no = no
        for i in range(self.no):
            sub = input(f"\nenter {i+1}th subject :")
            self.subject.append(sub)
            while True:
                mark = int(input(f"enter {sub}'s marks:"))
                if mark<0 or mark>100:
                    print("invalid marks!! Please enter marks btw 0 to 100")
                else:
                    self.marks.append(mark)
                    break
            

user = input("enter your name:")
roll = input("enter your roll number:")

s1 = student(user,roll)

n = int(input("enter number of subjects:"))
if n ==0 :
    print("invalid subject number!!")
else:
    s1.add_subject(n)
    s1.display_details()
    print(f"PERCENTAGE :{s1.percentage}")

print("=============================")




