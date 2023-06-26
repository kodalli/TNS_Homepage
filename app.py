from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/social')
def social():
    return render_template('social.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/news')
def news():
    return render_template('news.html')

# https://flowbite.com/docs/getting-started/flask/
# npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch

if __name__ == '__main__':
    app.run(debug=True)



