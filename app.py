from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return 'halo flask'

@app.route('/about')
def about():
    return 'About me'

app.run(debug=True)  #  debug agar kalau ada error akan terlihat di bagian mananya
