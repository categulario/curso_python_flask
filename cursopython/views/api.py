from flask import jsonify
from cursopython import app


@app.route("/api/dog")
def dog_list():
    return jsonify([{
        'name': 'Sparks',
    }])


@app.route("/api/dog/<id>")
def dog_show(id):
    return f'Perro: {id}'


@app.route("/api/dog/<id>", methods=['PUT'])
def dog_update(id):
    return jsonify({
        'name': 'new name',
    })


@app.route("/api/dog", methods=['POST'])
def dog_create():
    new_dog = Dog.validate(
        name=request.form.get('name'),
        age=request.form.get('age'),
    ).save()

    return jsonify(new_dog.to_json()), 201


@app.route("/api/dog/<id>", methods=['DELETE'])
def dog_delete(id):
    return '', 204
