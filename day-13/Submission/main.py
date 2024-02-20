from flask import Flask, jsonify

app = Flask(__name__)

csv_file = "/home/vee/Personal/15-Days-of-Python/day-13/Submission/programming_languages.csv"


def read_csv():
    """
    reads the csv from the variable `csv_file`

    returns:
        json (str): converted json value from csv
    """
    try:
        return [
            dict(
                zip(["name", "creator", "date", "usage"], (i.replace("\n", "")).split(","))
                )
                for i in (open(csv_file).readlines())[1:-1]
            ]
    except Exception as e:
        return {"error" : str(e)}


@app.route("/", methods=["GET"])
def get_langs():
    return jsonify(read_csv())


if __name__ == "__main__":
    app.run(debug=True)
