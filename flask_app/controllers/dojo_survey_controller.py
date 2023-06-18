from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo_survey_model import DojoSurvey


@app.route('/')
def index():
    return redirect('/dojo_survey')

@app.route('/dojo_survey')
def show_survey():
    return render_template('dojo_survey.html')

#ACTION PAGE FOR SURVEY
@app.route('/survey_process', methods=['POST'])
def successful_survey():
    # session['name'] = request.form['name']
    # session['location'] = request.form['location']
    # session['language'] = request.form['language']
    # session['comments'] = request.form['comments']
    # # session['stacks'] = request.form['webfund']
    # return redirect('/results')
    if not DojoSurvey.validate_survey(request.form):
        return redirect('/')
    DojoSurvey.save(request.form)
    return redirect ('/results')

#SHOW PAGE FOR RESULTS
@app.route('/results')
def survey_results():
    one_survey = DojoSurvey.get_last()
    return render_template('dojo_results.html', one_survey = one_survey)