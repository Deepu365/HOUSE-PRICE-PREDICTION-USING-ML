import csv
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(self.name, self.age, self.marks)
    def to_list(self):
        return [self.name, self.age, self.marks]
def save_to_csv(student):
    with open("students.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(student.to_list())
def read_students():
    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
students = [
    Student("deepu", 20, 85),
    Student("dam", 15, 25),
    Student("mounika", 56, 95),
    Student("teja", 50, 85),
    Student("tanuja", 40, 75),
    Student("keerthi", 76, 55),
    Student("jyoti", 10, 65),
    Student("liki", 30, 97)
]
for s in students:
    save_to_csv(s)
print("All Students:")
read_students()