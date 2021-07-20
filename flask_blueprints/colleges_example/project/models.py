from project import db
# models
class Colleges(db.Model):

    __tablename__ = 'colleges'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    student = db.relationship('Students',backref='colleges',uselist=False)

    def __init__(self, name):
        # Note how a college only needs to be initalized with a name!
        self.name = name

    def __repr__(self):
        if self.student:
            return f"Student {self.student.name} is from College {self.name}"
        else:
            return f"College {self.name}."

class Students(db.Model):

    __tablename__ = 'students'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    clg_id = db.Column(db.Integer,db.ForeignKey('colleges.id'))

    def __init__(self,name,clg_id):
        self.name = name
        self.clg_id = clg_id

    def __repr__(self):
        return f"Student Name: {self.name}"
