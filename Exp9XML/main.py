import xml.etree.ElementTree as ET

tree = ET.parse("student.xml")
root = tree.getroot()

print("=" * 110)
print("{:<12} {:<15} {:<8} {:<10} {:<10} {:<10} {:<30}".format(
    "ID", "Name", "Age", "Gender", "Branch", "Semester", "Email"
))
print("=" * 110)

for student in root.findall("student"):
    student_id = student.find("student_id").text
    name = student.find("name").text
    age = student.find("age").text
    gender = student.find("gender").text
    branch = student.find("branch").text
    semester = student.find("semester").text
    email = student.find("email").text

    print("{:<12} {:<15} {:<8} {:<10} {:<10} {:<10} {:<30}".format(
        student_id, name, age, gender, branch, semester, email
    ))

print("=" * 110)