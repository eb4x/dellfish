from flask import Flask, jsonify, send_file
import os.path

app = Flask(__name__)

model_name = "r820"


@app.route("/redfish/v1")
def ServiceRoot():
    if not os.path.exists(f"static/{model_name}/ServiceRoot.json"):
        return jsonify({"Error": "File not found"}), 404

    return send_file(
        f"static/{model_name}/ServiceRoot.json", mimetype="application/json"
    )


@app.route("/redfish/v1/Chassis")
def ChassisCollection():
    if not os.path.exists(f"static/{model_name}/ChassisCollection.json"):
        return jsonify({"Error": "File not found"}), 404

    return send_file(f"static/{model_name}/ChassisCollection.json")


@app.route("/redfish/v1/Systems")
def ComputerSystemCollection():
    if not os.path.exists(f"static/{model_name}/ComputerSystemCollection.json"):
        return jsonify({"Error": "File not found"}), 404

    return send_file(f"static/{model_name}/ComputerSystemCollection.json")


@app.route("/redfish/v1/Systems/<string:system>")
def ComputerSystem(system):
    if not os.path.exists(f"static/{model_name}/Systems/{system}.json"):
        return jsonify({"Error": "File not found"}), 404

    return send_file(f"static/{model_name}/Systems/{system}.json")


@app.route("/redfish/v1/Systems/<string:system>/Storage")
def StorageCollection(system):
    print(f"static/{model_name}/Systems/{system}/StorageCollection.json")
    if not os.path.exists(
        f"static/{model_name}/Systems/{system}/StorageCollection.json"
    ):
        return jsonify({"Error": "File not found"}), 404

    return send_file(f"static/{model_name}/Systems/{system}/StorageCollection.json")


@app.route("/redfish/v1/Systems/<string:system>/Storage/<string:storage>")
def Storage(system, storage):
    if not os.path.exists(
        f"static/{model_name}/Systems/{system}/Storage/{storage}.json"
    ):
        return jsonify({"Error": "File not found"}), 404

    return send_file(f"static/{model_name}/Systems/{system}/Storage/{storage}.json")


@app.route("/redfish/v1/Systems/<string:system>/Storage/Drives/<string:drive>")
def StorageDrive(system, drive):
    if not os.path.exists(
        f"static/{model_name}/Systems/{system}/Storage/Drives/{drive}.json"
    ):
        return jsonify({"Error": "File not found"}), 404

    return send_file(
        f"static/{model_name}/Systems/{system}/Storage/Drives/{drive}.json"
    )


@app.route("/redfish/v1/Systems/<string:system>/Storage/Volumes/<string:volume>")
def StorageVolume(system, volume):
    if not os.path.exists(
        f"static/{model_name}/Systems/{system}/Storage/Volumes/{volume}.json"
    ):
        return jsonify({"Error": "File not found"}), 404

    return send_file(
        f"static/{model_name}/Systems/{system}/Storage/Volumes/{volume}.json"
    )


if __name__ == "__main__":
    app.run()
