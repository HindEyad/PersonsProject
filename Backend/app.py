from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class Person:
    def __init__(self, id, name, age, gender, email):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

persons = [
    Person(1, "bella", 23, "female", "bella@example.com"),
    Person(2, "Loai", 49, "male", "loai@example.com"),
    Person(3, "vero", 20, "female", "vero.nader@example.com"),
    Person(4, "mandy", 70, "female", "mandy@example.com")
]

@app.route('/persons', methods=['GET'])
def get_persons():
    return jsonify([person.__dict__ for person in persons])

@app.route('/persons', methods=['POST'])
def add_person():
    new_person = request.get_json(force=True)
    new_person_id = max([person.id for person in persons]) + 1
    new_person_obj = Person(new_person_id, new_person['name'], new_person['age'], new_person['gender'], new_person['email'])
    persons.append(new_person_obj)
    return jsonify({'message': 'Person added successfully', 'person': new_person_obj.__dict__})

@app.route('/persons/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = next((p for p in persons if p.id == person_id), None)
    if person:
        return jsonify(person.__dict__)
    else:
        return jsonify({'error': 'Person not found'})

@app.route('/persons/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    updated_person = request.get_json(force=True)
    person = next((p for p in persons if p.id == person_id), None)
    if person:
        person.name = updated_person['name']
        person.age = updated_person['age']
        person.gender = updated_person['gender']
        person.email = updated_person['email']
        return jsonify({'message': 'Person updated successfully', 'person': person.__dict__})
    else:
        return jsonify({'error': 'Person not found'})

@app.route('/persons/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = next((p for p in persons if p.id == person_id), None)
    if person:
        persons.remove(person)
        return jsonify({'message': 'Person deleted successfully'})
    else:
        return jsonify({'error': 'Person not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
