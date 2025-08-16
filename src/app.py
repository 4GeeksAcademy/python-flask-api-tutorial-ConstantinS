from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [{"label": "Sample Todo 1", "done": False}]

@app.route('/')
def home():
    return "Hello World"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        todos.pop(position)
        return jsonify(todos), 200
    else:
        return jsonify({"error": "Índice fuera de rango"}), 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3245, debug=True)