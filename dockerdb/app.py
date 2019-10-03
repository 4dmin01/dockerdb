from flask_api import FlaskAPI
from flask import request

app = FlaskAPI(__name__)

@app.route('/', methods=['GET', 'PUT'])
def example():
    if request.method == 'PUT':
        note = str(request.data.get('DATA', ''))
        if note == '':
            return 'Nothing has been put in the database'
        with open('db.txt', 'r') as f:
            db = f.read()
        if [db][0] == '':
            with open('db.txt', 'a') as f:
                f.write(note)
        else:
            with open('db.txt', 'a') as f:
                f.write('\n'+note)
        return note+' has been put in the database'
    elif request.method == 'GET':
        with open('db.txt') as f:
            db = f.read()
        db = str(db.split('\n'))
        return db+'\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
