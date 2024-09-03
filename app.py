from flask import Flask, jsonify, make_response, request, send_file
from functools import wraps
from typing import Any, Callable
import os.path

app = Flask(__name__)

model_name = "r820"


def authorization(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        authorization = request.headers.get("Authorization")

        if not authorization:
            return make_response(jsonify({"message": "Unauthorized"}), 401)

        if authorization != "Basic cm9vdDpjYWx2aW4=":
            return make_response(jsonify({"message": "Still unauthorized"}), 401)

        return func(*args, **kwargs)

    return wrapper


@app.route("/redfish/v1")
def ServiceRoot():
    if not os.path.exists(f"static/{model_name}/ServiceRoot.json"):
        return jsonify({"Error": "File not found"}), 404

    return send_file(
        f"static/{model_name}/ServiceRoot.json", mimetype="application/json"
    )


@app.route("/redfish/v1/Chassis")
@authorization
def ChassisCollection():
    if not os.path.exists(f"static/{model_name}/ChassisCollection.json"):
        return jsonify({"Error": "File not found"}), 404

    return send_file(f"static/{model_name}/ChassisCollection.json")


@app.route("/redfish/v1/Managers")
@authorization
def ManagerCollection():
    if not os.path.exists(f"static/{model_name}/ManagerCollection.json"):
        return jsonify({"Error": "File not found"}), 404

    return send_file(f"static/{model_name}/ManagerCollection.json")


@app.route("/redfish/v1/Managers/<string:manager>")
@authorization
def Manager(manager):
    if not os.path.exists(f"static/{model_name}/Managers/{manager}.json"):
        return jsonify({"Error": "File not found"}), 404

    return send_file(f"static/{model_name}/Managers/{manager}.json")


@app.route("/redfish/v1/Systems")
@authorization
def ComputerSystemCollection():
    if not os.path.exists(f"static/{model_name}/ComputerSystemCollection.json"):
        return jsonify({"Error": "File not found"}), 404

    return send_file(f"static/{model_name}/ComputerSystemCollection.json")


@app.route("/redfish/v1/Systems/<string:system>")
@authorization
def ComputerSystem(system):
    if not os.path.exists(f"static/{model_name}/Systems/{system}.json"):
        return jsonify({"Error": "File not found"}), 404

    return send_file(f"static/{model_name}/Systems/{system}.json")


@app.route("/redfish/v1/Systems/<string:system>/Storage")
@authorization
def StorageCollection(system):
    if not os.path.exists(
        f"static/{model_name}/Systems/{system}/StorageCollection.json"
    ):
        return jsonify({"Error": "File not found"}), 404

    return send_file(f"static/{model_name}/Systems/{system}/StorageCollection.json")


@app.route("/redfish/v1/Systems/<string:system>/Storage/<string:storage>")
@authorization
def Storage(system, storage):
    if not os.path.exists(
        f"static/{model_name}/Systems/{system}/Storage/{storage}.json"
    ):
        return jsonify({"Error": "File not found"}), 404

    return send_file(f"static/{model_name}/Systems/{system}/Storage/{storage}.json")


@app.route("/redfish/v1/Systems/<string:system>/Storage/Drives/<string:drive>")
@authorization
def StorageDrive(system, drive):
    if not os.path.exists(
        f"static/{model_name}/Systems/{system}/Storage/Drives/{drive}.json"
    ):
        return jsonify({"Error": "File not found"}), 404

    return send_file(
        f"static/{model_name}/Systems/{system}/Storage/Drives/{drive}.json"
    )


@app.route("/redfish/v1/Systems/<string:system>/Storage/<string:controller>/Volumes")
@authorization
def VolumeCollection(system, controller):
    if not os.path.exists(
        f"static/{model_name}/Systems/{system}/Storage/{controller}/VolumeCollection.json"
    ):
        return jsonify({"Error": "File not found"}), 404

    return send_file(
        f"static/{model_name}/Systems/{system}/Storage/{controller}/VolumeCollection.json"
    )


@app.route("/redfish/v1/Systems/<string:system>/Storage/Volumes/<string:volume>")
@authorization
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
