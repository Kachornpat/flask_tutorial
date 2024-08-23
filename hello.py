from flask import Flask, render_template, url_for
app = Flask(__name__)

# to run with command 'flask run'
# set FLASK_APP=filename.py
# set FLASK_DEBUG=1

posts = [
    {
        'author': 'Kachornpat Gullpatpornchai',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 15, 2024'
    },
    {
        'author': 'Yorijo Noda',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 14, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)