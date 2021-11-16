from flask import jsonify, Flask, request


app = Flask()

data = {
    "data": [
        {
            "Contact": "9987644456",
            "Name": "Raju",
            "done": False,
            "id": 1
        },
    ]
}

@app.route("/add-data", methods=["POST"])

def add_task():

    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data"
        },400)

add_task()

contact = {
    'id': tasks[-1]['id'] + 1,
    'Name': request.json['Name'],
    'Contact': request.json.get('Contact', ""),
    'done': False
    }

data.append(contact)

return jsonify({
    "status": "successful",
    "message": "Task added successfully"
})

