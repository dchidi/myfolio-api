from flask import Flask, Request

app = Flask(__name__)


# GET
@app.get('/profile')
def get_profile():
    return {'msg': 'profile'}


@app.get('/projects')
def get_project():
    return {'msg': 'project'}


# POST
@app.post('/profile')
def profile():
    return {'msg': 'save profile'}


@app.post('/project')
def project():
    return {'msg': 'save project'}


@app.post('/update_password')
def update_password():
    return {'msg': 'update password'}


@app.post('/contact_me')
def contact_me():
    return {'msg': 'contact message'}


# DELETE
@app.delete('/project')
def delete_project():
    return {'msg': 'delete project'}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
