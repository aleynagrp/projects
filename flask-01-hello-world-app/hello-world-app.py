from flask import Flask
app = Flask(__name__)
@app.route('/')
def head():
    return 'Hello world Aleyna'
@app.route('/second')
def second():
    return 'This is second page'
@app.route('/third')
def third():
    return 'This is third page'
@app.route('/forth/<string:id>')
def forth(id):
    return f'Id of this page is {id}'
if __name__ == '__main__':
    app.run(debug=True)
<<<<<<< HEAD
    app.run(host= '0.0.0.0', port= 80)
=======
    app.run(host= '0.0.0.0', port=80)
>>>>>>> 165103fa813ccf1f6267ee4ff87668cfc7e02e7d
