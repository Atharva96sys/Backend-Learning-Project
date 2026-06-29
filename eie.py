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

def add_student(RN,Name,Marks,SID):
    for s in students:
        if s.SID == SID:
            print("SID already Exists")
            return
        
    ns=Student(RN,Name,Marks,SID)
    students.append(ns)
def dict_to_list():
    list_of_dict = []
    for s in students:
        list_of_dict.append(s.to_dict())
    
    return list_of_dict

def to_object():
    for s_dict in list_of_dict:
        add_student(s_dict["RN"],s_dict["Name"],s_dict["Marks"],s_dict["SID"])
    


add_student(1,"Atharva",94,"2401")


print(dict_to_list())


