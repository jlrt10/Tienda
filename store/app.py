from flask import render_template
from appInitialize import app

@app.route('/')
def index ():
    return render_template('index.html')

if __name__ == '__main__':    
    app.run(host='0.0.0.0', debug=True)