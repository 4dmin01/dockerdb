from flask_api import FlaskAPI
from flask import request

app = FlaskAPI(__name__)
@app.route('/', methods=['GET', 'POST'])
def dockerdbgui():
    site = '<form method="post" action="/">\
<input type="text" name="input" value=""><br><br>\
 <input type="submit" value="Submit">\
 </form>'
    if request.method == 'GET':
        with open('db.txt', 'r') as f:
            db = f.read()
        return site

    elif request.method == 'POST':
        try:
            note = str(request.form["input"])
        except:
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
        return site+note+' has been put in the database'
@app.route('/db/', methods=['GET'])
def dockerdb():
    with open('db.txt') as f:
        db = f.read()
    return db
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
