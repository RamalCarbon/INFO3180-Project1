from . import db
from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    name1 = db.Column(db.String(80))
    name2 = db.Column(db.String(80))
    gender = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(255))
    location = db.Column(db.String(255))
    biography = db.Column(db.String(300))
    image = db.Column(db.String(255))
    
    def __init__(self, name1, name2, gender, email, locaion, biography, image):
        self.name1 = first_name
        self.name2 = last_name
        self.gender = username
        self.email = email
        self.location = location
        self.biography = biography
        self.image = image

    def is_authenticated(self):
        return True
stop fucking with me....
    def is_active(self):
        return True
        
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
