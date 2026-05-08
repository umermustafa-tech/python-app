from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!!!!!!!!!!!!gggggggggggttttttttttuuuuuuuuuuuuuuugggggggggg!!!!fffffffffffffff how tttttttttttre yougg!!!!!!!!!!!!!!!!!!!!!!!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
