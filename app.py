from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Ondo state, Nigeria',
    'salary': 'N300,000',
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'lagos state, Nigeria',
    'salary': 'N500,000',
  },
{
  'id': 3,
  'title': 'Frontend engineer',
  'location': 'remote',
  'salary': 'N300,000',
},
{
  'id': 4,
  'title': 'backend engineer',
  'location': 'sanfrancisco, USA',
  'salary': '$100,000',
}
]

@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)