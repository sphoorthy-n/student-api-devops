from flask import Flask, request, jsonify
app=Flask(__name__)
students=[
    {"id":101, "name":"Sphoorthy", "age":20},
    {"id":102, "name":"Deepthi", "age":21}
]
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    for s in students:
        if s['id']==id:
            return jsonify(s)
    return jsonify({"error": "Not Found"}), 404

@app.route('/students', methods=['POST'])
def add_student():
    data=request.get_json()
    students.append(data)
    return jsonify(data), 201

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data=request.get_json()
    for i, s in enumerate(students):
        if s['id']==id:
            students[i]={"id": id, **data}
            return jsonify(students[i])
    return jsonify({"error": "Not Found"}), 404

@app.route('/students/<int:id>', methods=['PATCH'])
def patch_student(id):
    data=request.get_json()
    for s in students:
        if s['id']==id:
            s.update(data)
            return jsonify(s)
    return jsonify({"error": "Not Found"}), 404

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    for i, s in enumerate(students):
        if s['id']==id:
            students.remove(s)
            return jsonify({"message": "Deleted"}), 200
    return jsonify({"error": "Not Found"}), 404

if __name__=="__main__":
    app.run(host="0.0.0.0", port=3000)


