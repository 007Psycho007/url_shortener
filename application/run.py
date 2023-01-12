from waitress import serve
from application import app

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80) 
    serve(app, host='0.0.0.0', port=8080)
