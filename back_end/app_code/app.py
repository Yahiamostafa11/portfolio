from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(_name_)
# Load configuration from config.py
app.config.from_object('config.Config')

# Initialize the database with SQLAlchemy
db = SQLAlchemy(app)
# Initialize database migrations with Flask-Migrate
migrate = Migrate(app, db)

# Import the routes after initializing the app and db
from routes import *

# Run the application
if _name_ == '_main_':
    app.run(debug=True)