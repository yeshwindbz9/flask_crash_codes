from basic import db, Students

# create 
stu = Students("Raja", 19)
db.session.add(stu)
db.session.commit()
print("--------------------------")

# read
all_students = Students.query.all() # list of all stu objects
print(all_students)
print("--------------------------")
# select by id
first_student = Students.query.get(1)
print(first_student.name)
print("--------------------------")
# filters: produces the sql code
stu = Students.query.filter_by(name="Pammy")
print(stu.all())
print("--------------------------")

# update
first_student = Students.query.get(1)
first_student.age = 24
db.session.add(first_student)
db.session.commit()
print("--------------------------")

# delete
second_student = Students.query.get(2)
db.session.delete(second_student)
db.session.commit()
print("--------------------------")

# select all
all_stu = Students.query.all()
print(all_stu)