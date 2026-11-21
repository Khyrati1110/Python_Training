from flask import Flask, app, jsonify,request

app = Flask(__name__)

equipment = {
    101:{
        "id":101,
        "name":"flight control unit",
        "type":"FCU",
        "status":"operational"
    },
    102:{
        "id":102,
        "name":"navigation system",
        "type":"NS",
        "status":"operational"
    }
}

@app.get('/api/equipment')
def get_equipment():
    return jsonify(list(equipment.values())),200

if __name__ == '__main__':
    app.run(debug=False,port=5000)

@app.get('/api/equipment/<int:equipment_id>')
def get_equipment_by_id(equipment_id):
        return jsonify(equipment[equipment_id]),200



if __name__ == '__main__':
    app.run(debug=False,port=5000)