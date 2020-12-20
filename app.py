from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
import json
import csv


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formtest', methods=('GET', 'POST'))
def formtest():
    if request.method == "POST":
        req = request.form
        results = dict()
        missing = list()
        for k, v in req.items():
            if v == "":
                missing.append(k)
            else:
                results[k] = v
                
        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("formtest.html", feedback=feedback)

        return redirect(url_for(".results", messages=results, **request.args))
    
    return render_template('formtest.html')


@app.route('/results')
def results():
    messages = request.args['messages']
    messages = eval(messages)
    first_n = messages['fname']
    last_n = messages['lname']
    name = f"{first_n} {last_n}"
    return render_template('results.html', messages=name)

@app.route('/allegiances')
def allegiances():
        s = json.dumps(list(csv.DictReader(open("files/allegiance.csv"))))
        return s




@app.route('/allegiancesdashboard', methods=('GET', 'POST'))
def allegiancesdashboard():
    return render_template('allegiancesdashboard.html')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')





    




    



