from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  
app.config['SESSION_TYPE'] = 'filesystem'  

Session(app)

@app.route('/')
def index():
    if 'notes' not in session:
        session['notes'] = []
    return render_template('home.html', notes=session['notes'])

@app.route('/add_note', methods=['POST'])
def add_note():
    note = request.form.get('note')
    if note:
        if 'notes' not in session:
            session['notes'] = []
        session['notes'].append(note)
        session.modified = True  
    return redirect('/')

@app.route('/thankyou', methods=['POST'])
def thank_you():
    note = request.form.get("note")
    if note:
        if 'notes' not in session:
            session['notes'] = []
        session['notes'].append(note)
        session.modified = True  
    return render_template('notes.html', notes=session['notes'])

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
