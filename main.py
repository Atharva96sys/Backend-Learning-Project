import json
class Student:
    def __init__(self,RN,Name,Marks,SID):
        self.RN = RN
        self.Name = Name
        self.Marks = Marks
        self.SID = SID
    def display(self):
        print(f"Roll No: {self.RN}")
        print(f"Name: {self.Name}")
        print(f"Marks: {self.Marks}")
        print(f"SID: {self.SID}")
        print()

    def to_dict(self):
        temp_dict = {}
        temp_dict.update({"RN":self.RN, "Name":self.Name, "Marks":self.Marks, "SID":self.SID})

        return temp_dict

students=[]  

def dict_to_list():
    list_of_dict = []
    for s in students:
        list_of_dict.append(s.to_dict())
    
    return list_of_dict

def to_object(list_of_dict):
    for s_dict in list_of_dict:
        add_student(s_dict["RN"],s_dict["Name"],s_dict["Marks"],s_dict["SID"])

def save_students():
    data =  dict_to_list()
    with open("student.json",'w') as g:
        json.dump(data,g)



def load_students():
    try:
        with open("student.json",'r') as r:
            data = json.load(r)
            to_object(data)
    except FileNotFoundError:
        print("No Student database found.Starting with an empty database.")
        pass



def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number")

def add_student(RN,Name,Marks,SID):
    for s in students:
        if s.SID == SID:
            print("SID already Exists")
            return
        
    ns=Student(RN,Name,Marks,SID)
    students.append(ns)
    save_students()

def view_students():
    if len(students)==0:
        print("No Students Found")
        return
    
    for s in students:
        s.display()

def search_student(SID):
    found=False
    for s in students:
        if s.SID == SID:
            s.display()
            found=True
    if not found:
        print("Student Not Found")

def delete_student(SID):
    found=False
    for s in students:
        if s.SID == SID:
            found=True
            s.display()
            print("Do You Want to Delete it is an irreversible process")
            key = input("Yes or No {Y/N}").upper()
            if key == "Y":
                students.remove(s)
                print("Success")
                break

            save_students()
                       
    if not found:
        print("Student Not Found")
   


def update_student(SID):
    found=False
    for s in students:
        if s.SID == SID:
            print("What you want to update ")
            print("SID cannot be update by user it can only be done by Admin contact Head-Officer for further information")
            print("1:Roll No Change.\n2:Name Change.\n ")
            found=True
            s.display()
            a=get_integer("Input 1/2 to Proceed:-")

            if a == 1:
                print("Enter your new Roll No")
                s.RN = get_integer("Here")
                print("RollNo Successfully changed")
                print("RollNo:-",s.RN,"\n")
                s.display()
            elif a == 2:
                print("Enter your new Name")
                s.Name = input("Here")
                print("Name Successfully changed")
                print("Name:-",s.Name,"\n")
                s.display()
            else:
                print("Enter valid command No.")
                return 
            save_students()
        
    if not found:
        print("Invalid SID")












load_students()
while True:
    
    print("Menu")
    print("1:Add Student")
    print("2:View All Student")
    print("3:Search Student")
    print("4:Update Student")
    print("5:Delete Student")
    print("6:Exit")

    key=get_integer("Input:-")

    if(key==1):
        print("New Enrollment")
        RN=get_integer("Enter RollNo:-")
        Name=input("Enter Name of Student:-")
        Marks=get_integer("Enter Marks obtained:-")
        SID=input("Enter SID of Student:-")
        add_student(RN,Name,Marks,SID)

        print("Student Successfully Added")
        search_student(SID)
    elif(key==2):
        print("List of All Students")
        view_students()

    elif(key==3):
        print("Search Student By SID")
        search_student(input("Enter SID-"))
    elif(key==4):
        print("Update Student By SID")
        update_student(input("Enter SID-"))
    elif(key==5):
        print("Delete By SID")
        delete_student(input("Enter SID-"))
    elif(key==6):
        print("Exiting Program")
        print(":)")
        exit()
    else:
        print("Invalid Input")