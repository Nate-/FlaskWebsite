from flask import url_for, render_template
from app import app
from exp import Exp

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    experience = []
    experience.append(Exp("dolby.png",
                            "Dolby Laboratories, Inc.",
                            "Software Engineer",
                            "VR"))
    experience.append(Exp("ulukau.png",
                            "Ulukau: The Hawaiian Electronic Library",
                            "Software Engineer",
                            "Frontend"))
    experience.append(Exp("uhh.png",
                            "University of Hawaii at Hilo",
                            "Electrical Engineer, Intern",
                            "Research"))
    return render_template('resume.html',
                            exp = experience)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
