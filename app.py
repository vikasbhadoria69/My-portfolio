from flask import Flask, render_template,request
app = Flask(__name__,template_folder='template')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/startup")
def startup():
    return render_template('Startup.html')

@app.route("/work")
def work():
    return render_template('work.html')

@app.route("/notes")
def notes():
    return render_template('notes.html')

if __name__ == "__main__": 
    app.run(debug=True)