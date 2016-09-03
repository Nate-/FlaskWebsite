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
                            ["When I joined Dolby, the company was still trying to break into the VR market. I joined a brilliant team \
                            of software engineers aiming to adapt existing Dolby technologies for a VR environment. To do so, I initially \
                            tasked with streamlining the audio rendering portion of the the audio SDK. This required to me to develop a \
                            system to match the rotational axes of the the device, like an Oculus or GearVR, to our internal axes then map \
                            the changes in head position between axis systems to adjust audio according to head positioning. After finishing \
                            the task, I was responsible for making sure that my work had cross-platform functionality."
                            , "After redesigning the audio rendering SDK, I was lucky enough to be given the opportunity to work on the \
                            complementary decoder library. I was told that Dolby was built off Hollywood and that all movies and soundtracks \
                            prior to 1994 were all encoded using an older standard of compression. Thus, I was given the chance to find \
                            a means of implementing backwards compatibility for legacy content, which I accomplished by establishing \
                            virtual audio sources set at home theatre locations and accounting for audio change according to a given \
                            surround sound set up."],
                            ["C++", "C", "C#", "Java", "Android NDK"]))
    experience.append(Exp("ulukau.png",
                            "Ulukau: The Hawaiian Electronic Library",
                            "Software Engineer",
                            ["Ulukau is the principle attempt at preserving Hawaiian culture digitally for all generations to come. \
                            The resources collected range from historical land deads to genealogy to children's story books written in \
                            Hawaiian. As a student at University of Hawaii, I wanted to use the skills I've learned to give back to the \
                            community that so graciously accepted me. When I learned that Ulukau was making the transition from Oahu to \
                            the Big Island, I reached out to see if there was anyway I could be a part of the process."
                            , "Fortune smiled upon me as I reached out. They were looking for a Front End Software Engineer to revamp \
                            their appearance and provide a means of easily updating and maintaining the project after I finished since it was \
                            cost-prohibitive to hire a web administrator. Thus, my partner and I hopped on board to work out the major \
                            issues like Section 508 compliance before setting up routine back ups and redesigning the entire website \
                            from the ground up."],
                            ["PHP", "HTML", "CSS", "JavaScript", "JQuery", "MySQL"]))
    experience.append(Exp("uhh.png",
                            "University of Hawaii at Hilo",
                            "Electrical Engineer, Intern",
                            ["In Hawaii, energy costs are typically 6 times more expensive than on the mainland. A lot of Hawaiians choose \
                            to live off the grid, so the energy grid infrastructure is not as developed as it could be. To address the issue, \
                            Cornell University set up a joint task force of sorts to investigate leading causes of energy inefficiency. This \
                            included measuring phantom loads, which occurs when electricity is drawn when devices are turned off but plugged into \
                            an outlet, and finding infrastructure conflicts causing increased demand on energy, such as single paned windows or \
                            shutters that do not close. After combing through the electrical systems on campus, we mapped energy usage by building \
                            and identified that 20% of the energy was being wasted. After learning about the severity of the problem, the \
                            chancellor decided that she would have to look into budgeting for architectural and electrical upgrades throughout \
                            campus."],
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
    proj.append(Project("NQuan.me", 
                        "www.nquan.me", 
                        "Web application built using Flask framework to highlight who I am as a professional and individual.", 
                        ["Flask", "Python", "BootStrap", "HTML5", "CSS3", "JavaScript"]))
    proj.append(Project("24 Game Solver", 
                        "github.com/nate-/Math24", 
                        "When I was volunteering as a tutor and assistant coach for the Pinole Math Club, I helped \
                        co-found a Math 24 tournament for the club members. During the tournament, the club members \
                        competed to solve Math 24 cards, where four numbers are given and any combination of basic arithmetic operations \
                        could be used to create a mathematical equation equating to 24. During that tournament, in the last minutes of \
                        each round, when the hardest cards were given and couldn't be solved in time, my students came to me to seek the\
                        answer. However, before I could even start thinking about the possible solution, they were ushered into the next \
                        round. At that point, I decided to create this solver to help quickly provide them with an answer as well as \
                        stimulate some interest in Computer Science.",
                        ["Python"]))
    proj.append(Project("Bytecode",
                        "github.com/nate-/bytecode",
                        "As the graduating requirement of my Compiler Theory independent study course, I was \
                        tasked with creating my own language that could be compiled into executable JVM bytecode. \
                        This project is the manifestation of that assignment. For this project, I invented an \
                        arbitrary imperative language based on Python and C with basic functionality, such as loops, \
                        conditional statements, variable and function declarations, that would be parsed and \
                        translated into JVM bytecode.",
                        ["Java"]))
    proj.append(Project("League of Legends LCS 2014 Statistics",
                        "github.com/nate-/LCS2014Spring",
                        "In a heated debate during Database Systems class with fellow classmates and League of Legends \
                        players about who the best players and which team was best, I decided to track the e-sport \
                        tournament religiously and create a normalized database to store all the statistics that could \
                        be collected for the Spring 2014 tournament. After gathering the data, I launched a simple PHP \
                        template front-end that amalgamated all the relevant statistics to our arguments into a single \
                        website. It was a great way to have some objective source of performance and to ease the \
                        arguments from team loyalties.",
                        ["SQL", "PHP", "HTML", "JavaScript", "CSS"]))
    return render_template('projects.html', 
                            pageHeader="Projects",
                            proj=proj)