from flask import render_template, request
from cursopython import app


@app.route("/")
def index():
    persona = request.args.get('persona', 'Nadie')
    # persona = request.args['persona']

    return render_template('index.html',
        persona=persona
    )


@app.route("/<persona>")
def index_persona(persona):
    return render_template('index.html',
        persona=persona
    )
