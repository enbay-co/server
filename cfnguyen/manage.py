"""
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ python manage.py db --help
"""

# from flask import Flask
from cfnguyen import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from models import Result, User

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =  "postgresql://postgres:123@localhost/wordcount_dev"


# db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)



if __name__ == '__main__':
    manager.run()
    
        
