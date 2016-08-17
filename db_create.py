from app import db
from models import BlogPost


# # create the database and the db tables
# db.create_all()

# #inset
# db.session.add(BlogPost("Good", "I\'m good"))
# db.session.add(BlogPost("Well", "I\'m well"))

# #commit the changes
# db.session.commit()



def addIt(p1,p2):
	db.session.add(BlogPost(p1,p2))
	db.session.commit()


a1 = "add"
a2 = "I added it"
addIt(a1,a2)