from flask import Flask

app = Flask(__name__)

import cursopython.views.api
import cursopython.views.web
