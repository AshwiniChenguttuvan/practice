from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def student():
        return render_template('student.html')


@app.route('/next', methods=['post'])
def next():
    form_dict = request.form
    if 'login' in form_dict:
        return render_template('login.html')
    else:
        return render_template('register.html')


if __name__ == "__main__":
    app.run()
