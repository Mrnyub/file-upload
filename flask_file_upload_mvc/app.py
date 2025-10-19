import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

os.makedirs(app.config['LOG_FOLDER'], exist_ok=True)
logging.basicConfig(
    filename=f"{app.config['LOG_FOLDER']}/app.log",
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

from controllers.file_controllers import file_bp
app.register_blueprint(file_bp)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)