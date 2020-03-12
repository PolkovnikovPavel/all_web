# from data import db_session
# from data.users import User
# global_init = db_session.global_init
# create_session = db_session.create_session


name = input()

global_init(name)
session = create_session()
for user in session.query(User):
    if user.address == 'module_1' and (user.speciality != '' or 'ingeneer' not in user.position):
        print(user.id)
