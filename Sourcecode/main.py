
from flask import Flask, jsonify, request
from flask_cors import CORS
from Abstraction.Accesspoints import Accesspoints
from Abstraction.Switches import Switches
from Abstraction.Gateways import Controllers

aps = Accesspoints.Accesspoints()
switches = Switches.Switches()
controllers = Controllers.Controllers()
devices = []
dbAdapter = None

users = {
    "serviceUser": "sehrGeheim"
}

app = Flask("Translate-Service-Rest-API")
CORS(app)

# Get all devices
@app.route('/devices', methods=['GET'])
def get_devices():
    devices = []
    devices.append(switches.getDevices())
    devices.append(aps.getDevices())
    devices.append(controllers.getDevices())
    return jsonify({"Devices": devices}), 200

# Get a specific device by product number
@app.route('/device/<productnumber>', methods=['GET'])
def get_device(productnumber):
    switch = switches.getDevice(productnumber)
    if switch != None:
        return jsonify({"Device": switch}), 200
    ap = aps.getDevice(productnumber)
    if switch != None:
        return jsonify({"Device": ap}), 200
    controller = controllers.getDevice(productnumber)
    if switch != None:
        return jsonify({"Device": controller}), 200
    else:
        return jsonify({"Device": "Not found"}), 404
    

# Update the status of a switch
@app.route('/switch', methods=['PATCH'])
def update_switch():
    data = request.json
    productnumber = data.get('productnumber')
    device = data.get('Device')

    switches.updateDevice(productnumber, device)
    
    return jsonify({"Success": "Switch updated"}), 200

# Translate switch action
@app.route('/switch/translate', methods=['POST'])
def translate_switch_action():
    data = request.json
    pn = data.get('ProductNumber')

    result = switches.translate(pn)

    return jsonify({"Result": result})

# Update the status of an AP
@app.route('/ap', methods=['PATCH'])
def update_ap():
    data = request.json
    productnumber = data.get('productnumber')
    device = data.get('Device')

    aps.updateDevice(productnumber, device)
    
    return jsonify({"Success": "AP updated"}), 200

# Translate AP action
@app.route('/ap/translate', methods=['POST'])
def translate_ap_action():
    data = request.json
    pn = data.get('ProductNumber')

    result = aps.translate(pn)

    return jsonify({"Result": result})

# Update the status of a controller
@app.route('/controller', methods=['PATCH'])
def update_controller():
    data = request.json
    productnumber = data.get('productnumber')
    device = data.get('Device')

    controllers.updateDevice(productnumber, device)
    
    return jsonify({"Success": "Controller updated"}), 200

# Translate controller action
@app.route('/controller/translate', methods=['POST'])
def translate_controller_action():
    data = request.json
    pn = data.get('ProductNumber')

    result = controllers.translate(pn)

    return jsonify({"Result": result})

# Authentication
@app.route('/auth', methods=['POST'])
def authenticate():
    data = request.json
    username = data.get('username')
    password = data.get('secret')

    if users.get(username) == password:
        return jsonify({"message": "Authentication successful"})
    else:
        return jsonify({"error": "Authentication failed"}), 401

def initialize():
    return


if __name__ == '__main__':
    initialize()
    app.run(debug=True)