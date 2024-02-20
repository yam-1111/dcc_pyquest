from flask import Flask, jsonify, request

app = Flask(__name__)

aws_services = [
    {"id": 1, "service": "Lambda"},
    {"id": 2, "service": "Simple Storage Service(S3)"},
]


# base url
@app.route("/", methods=["GET", "POST"])
def hello():
    return (
        """
    <h1 style='color:#A020F0; text-align:center;'>hello world!</h1>
    """,
        418,
    )


# /aws_services/get_all
@app.route("/aws_services/get_all", methods=["GET"])
def get_all():
    return jsonify(aws_services)


# /aws_services/<int:service_id>
@app.route("/aws_services/<int:service_id>", methods=["GET"])
def get_service(service_id):
   service = [x for x in aws_services if service_id == x['id']]
   if service:
       return jsonify(service[0])
   else:
       return jsonify({"error" : f"service id: {service_id} not found"}), 404


# /aws_services/add_service
@app.route("/aws_services/add_service", methods=["POST"])
def add_service():
    service = request.get_json()
    # check if item has already in `aws_services`
    duplicate = next((x for x in aws_services if service['id'] == x['id']), None)
    if not duplicate:
        aws_services.append(service)
        return jsonify({"status" : f"succesfully added the entry `{service}`"})
    return jsonify({"status" : "error duplicate records found."}), 409


# /aws_services/delete_service/<int:service_id>
@app.route("/aws_services/delete_service/<int:service_id>", methods=["DELETE"])
def delete_service(service_id):
    # check if the given item is existing
    delete_item = next(((i,x) for i,x in enumerate(aws_services) if service_id == x['id']), None)
    if delete_item:
        aws_services.pop(delete_item[0])
        return jsonify({"status": f"succesfully deleted the `{delete_item[1]}`"})
    return jsonify({"status" : f"unable to find and delete the service id: {service_id}"}), 404


# /aws_services/update_service/<int:service_id>
@app.route("/aws_services/update_service/<int:service_id>", methods=["PUT"])
def update_service(service_id):
    update_item = next(((i,x) for i,x in enumerate(aws_services) if service_id == x['id']), None)
    if update_item:
        try:
            update_item[1].update(request.get_json())
            return jsonify({"status": f"succesfully updated the `{aws_services[update_item[0]]}`"})
        except Exception as e:
            return jsonify({"error" : str(e)}), 500
    return jsonify({"status" : f"unable to find and update the service id: {service_id}"}), 404




if __name__ == "__main__":
    app.run(debug=True)
