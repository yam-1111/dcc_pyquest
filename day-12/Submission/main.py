from flask import Flask, jsonify  

app = Flask(__name__)

my_info = {
    "name": "Anthony",
    "course_and_section": "BSCS 2-1",
    "favorite_programming language": "Python",
    "aws_service": "EC2"
}

@app.route('/', methods=['GET'])
def get_info():
    return jsonify(my_info)

if __name__ == '__main__':
    app.run(debug=True)