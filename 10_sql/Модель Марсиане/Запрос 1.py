# from data import db_session


name = input()

global_init(name)
session = create_session()


for user in session.query(User).filter(User.address == 'module_1'):
    print(user)
