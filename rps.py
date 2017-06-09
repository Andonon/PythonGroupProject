''' This is the programe for the PRS'''

from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def HomePage():
#this is the home page for RPS
    return render_template('rps.html')
    #this will navigate to our HomePage


@app.route('/roll',methods=['GET','POST'])
def rollpage():
#this is the home page for RPS
    print request.form
    rps = request.form['rps']
    random_num = random.randint(1,3)

    if random_num == 1:
        itrps = 'Rock'
    elif random_num == 2:
        itrps = 'Paper'
    elif random_num == 3:
        itrps = "Scissors"

    if rps == itrps:
        status = 'Tie'

    elif rps == "Rock" and itrps == "Paper":
        status = 'Lose'

    elif rps == 'Rock' and itrps == 'Scissors':
        status = 'Win'

    elif rps == 'Paper' and itrps == 'Rock':
        status = 'Win'

    elif rps == 'Paper' and itrps == 'Scissors':
        status = 'Lose'

    elif rps == 'Scissors' and itrps == 'Rock':
        status = 'Lose'

    elif rps == 'Scissors' and itrps == 'Paper':
        status = 'Win'


    return render_template('roll.html', rps=rps, itrps=itrps, status=status)
    #this will navigate to our HomePage
    #define random number 1-3,


app.run(debug=True)


@app.route('/result')
def resultpage():
#this is the home page for RPS
    return render_template('result.html')
    #this will navigate to our HomePage
