from flask import Flask
from flask_coralillo import Coralillo

app = Flask(__name__)

engine = Coralillo(app)

import views
