
from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('base.html')

@app.route('/story')
def generate_story():
    print(request.form)
    print(request.args)
    full_story = story.generate(request.args)
    return f"""
    <h1> Your Story </h1>
    <p> {full_story}
    """
