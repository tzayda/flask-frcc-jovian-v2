from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Bamberg, Germany',
    'salary': '€ 5.000,000'
}, {
    'id': 2,
    'title': 'Blockchain Engineer',
    'location': 'Boston, USA',
    'salary': '$ 6.000,000'
}, {
    'id': 3,
    'title': 'Linux/DevOps Engineer',
    'location': 'Remote',
    'salary': '$ 7.000,000'
}, {
    'id': 4,
    'title': 'Backend Developer',
    'location': 'Nuremberg, Germany',
    'salary': '€ 8.000,000'
}]


#html route
@app.route('/')
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Tayril")


#api route
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
