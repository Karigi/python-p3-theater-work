from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Role, Audition

# Set up the database engine
engine = create_engine('sqlite:///theater.db', echo=True)

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()


#------------------------CRUD OPERATIONS------------------------------------------

#Add a Role
new_role = Role(character_name="Garfield")
session.add(new_role)
session.commit()

# Print the Role added
print("Added new Role:")
print(f"Role ID: {new_role.id}, Character Name: {new_role.character_name}\n")

#Add an Audition for that Role
new_audition = Audition(actor="John Doe", location="London", phone=1234567890, role_id=new_role.id)
session.add(new_audition)
session.commit()

# Print the Audition added
print("Added new Audition:")
print(f"Audition ID: {new_audition.id}, Actor: {new_audition.actor}, Location: {new_audition.location}\n")

#Update an Audition's Status (Hiring)
audition = session.query(Audition).filter_by(actor="John Doe").first()
audition.call_back()
session.commit()

# Print the updated Audition status
print("Updated Audition (Hired):")
print(f"Audition ID: {audition.id}, Hired: {audition.hired}\n")

#Retrieve Lead and Understudy
role = session.query(Role).filter_by(id=new_role.id).first()

print("Lead and Understudy for the Role:")
print(f"Lead Actor: {role.lead()}")
print(f"Understudy Actor: {role.understudy()}\n")

#Retrieve all Auditions for the Role
print("All Auditions for the Role:")
for audition in role.auditions:
    print(f"Actor: {audition.actor}, Location: {audition.location}, Hired: {audition.hired}")

session.close()