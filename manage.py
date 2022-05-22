from app import app
from flask_script import Manager, Server

app = app ('development') #the app instance

manager = Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
    '''
    run the unit test on file 
    '''
    import unittest
    tests= unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ =='__main__':
    manager.run()