from flask import url_for, render_template
from app import app
from exp import Exp
from proj import Project

@app.route('/')
@app.route('/index')
def index():
    """
    Serves the home page
    """
    return render_template('index.html')

@app.route('/about')
def about():
    """
    Serves About page
    """
    return render_template('about.html',
                            pageHeader="About")

@app.route('/resume')
def resume():
    """
    Serves Resume page
    """
    #TO DO: Replace with SQLlite
    experience = []
    experience.append(Exp("dolby.png",
                            "Dolby Laboratories, Inc.",
                            "Software Engineer",
                            ["VR", "Paragraph2"],
                            ["C++", "C", "C#", "Java", "Android NDK"]))
    experience.append(Exp("ulukau.png",
                            "Ulukau: The Hawaiian Electronic Library",
                            "Software Engineer",
                            ["Frontend", "Paragraph2"],
                            ["PHP", "HTML", "CSS", "JavaScript", "JQuery", "MySQL"]))
    experience.append(Exp("uhh.png",
                            "University of Hawaii at Hilo",
                            "Electrical Engineer, Intern",
                            ["Research", "Paragraph2"],
                            []))
    return render_template('resume.html',
                            pageHeader="Resume",
                            exp = experience)

@app.route('/projects')
def projects():
    """
    Serves the projects page
    """
    #TO DO: Replace with SQLite
    proj = []
    proj.append(Project("NQuan.com", 
                        "www.nquan.com", 
                        "Web application built using Flask framework to highlight who I am as a professional and individual.", 
                        ["Flask", "Python", "BootStrap", "HTML5", "CSS3", "JavaScript"]))
    proj.append(Project("24 Game Solver", 
                        "github.com/nate-/Math24", 
                        "Python command line tool that was built for the Math Club students I was coaching.",
                        ["Python"]))
    proj.append(Project("Bytecode",
                        "github.com/nate-/bytecode",
                        "Compiler theory final project where I invented my own simple language, which inspired by \
                        Python and C programming languages. To develop the language, I engineered a parser and \
                        compiler that translated my language into Java bytecode to be executed by a Java Virtual Machine",
                        ["Java"]))
    proj.append(Project("League of Legends LCS 2014 Statistics",
                        "github.com/nate-/LCS2014Spring",
                        "A pet project that arose from a bet on who would be the best League of Legends professional player \
                        during the Spring 2014 LCS tournament. I collected and stored all the statistics throughout the season \
                        in used a MySQL database and filled a PHP template with SQL queries to aggregate statistics into a \
                        sorted table to summarize based on statistics that e-sports enthusiasts care about, such as KDA, etc.",
                        ["SQL", "PHP", "HTML", "JavaScript", "CSS"]))
    return render_template('projects.html', 
                            pageHeader="Projects",
                            proj=proj)