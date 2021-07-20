from basic import db, Students

# creates all tables model -> table
db.create_all()

# create two entries for the table 
sam = Students("Sammy", 21)
pam = Students("Pammy", 26)

# db.session.add(sam)
# db.session.add(pam)
db.session.add_all([sam, pam])

# saves the state of db
db.session.commit()

print("Database has been setup!")