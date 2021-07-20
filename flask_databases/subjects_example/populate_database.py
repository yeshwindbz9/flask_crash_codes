# This script will create some students, colleges, and owners!
from models import db, Students, Colleges, Subjects

# creating two students
sam = Students("Sammy")
pam = Students("Pammy")

# adding students to database
db.session.add_all([sam, pam])
db.session.commit()

# check with a query, prints all students
print(Students.query.all())

# grab Sammy from database
# trying to grab all students named Sammy, returns a list
# thus we grab the first index
sam = Students.query.filter_by(name="Sammy").all()[0]

# create a college for Sammy
xie = Colleges("XIE", sam.id)

# giving subjects to Sammy
math = Subjects("Maths", sam.id)
phy = Subjects("Physics", sam.id)

# commit these changes to the database
db.session.add_all([xie, math, phy])
db.session.commit()

# let's check Sammy after all the updates
sam = Students.query.filter_by(name="Sammy").all()[0]
print(sam)

# show subjects
print(sam.report_subjects())