from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test')
def index():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')