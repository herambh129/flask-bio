from flask import Flask, render_template, request
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return render_template('form.html')


@app.route('/biodata', methods=['GET', 'POST'])
def biodata():
    return
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

