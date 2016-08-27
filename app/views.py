from flask import url_for, render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('layout.html',
                            title="Home",
                            content_body="TEST")

@app.route('/about')
def about():
    return render_template('layout.html',
                            title="About",
                            content_body="ABOUT TEST")

@app.route('/resume')
def resume():
    return render_template('layout.html',
                            title="Resume",
                            content_body="RESUME TEST")

@app.route('/projects')
def projects():
    return render_template('layout.html',
                            title="Projects",
                            content_body="PROJ TEST")

@app.route('/contact')
def contact():
    return render_template('layout.html',
                            title="Contact Information",
                            content_body="CONTACT TEST")
