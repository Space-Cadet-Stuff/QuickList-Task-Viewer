from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash
from setup_db import User, ToDo

#Connect to the database
engine = create_engine('sqlite:///todo.db')
Session = sessionmaker(bind=engine)
session = Session()

#Insert users with hashed passwords
user1 = User(username='john_doe', email='johndoe@email.com',
password = generate_password_hash('password123'))
user2 = User(username='jane_doe', email='janedoe@email.com',
password = generate_password_hash('mypassword'))

session.add(user1)
session.add(user2)
session.commit()

#Insert tasks
task1 = ToDo(name='Learn SQLAlchemy', done=False, user_id=user1.id)
task2 = ToDo(name='Learn Build an App', done=False, user_id=user2.id)

session.add(task1)
session.add(task2)
session.commit()

print('User and tasks inserted successfully')