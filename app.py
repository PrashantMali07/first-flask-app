from flask import Flask, render_template_string, request, render_template, url_for, jsonify, redirect

app = Flask(__name__)

# Define HTML templates as strings
welcome_template = "<h1>Welcome to the home page of the Flask App</h1>"
index_template = "<h2>Welcome to the index page of the Flask App</h2>"

#1
@app.route("/", methods=["GET"])
def welcome():
    return render_template_string(welcome_template)

#2
@app.route("/index", methods=["GET"])
def index():
    return render_template_string(index_template)

## Post methods route #1
@app.route('/success/<int:total_score>/<float:average_score>')
def success(total_score, average_score):
    return "Congratulations!! you've passed the test & scored:" + str(total_score) + " | Average score: " + str(average_score)

## Post methods route #1
@app.route('/fail/<int:total_score>/<float:average_score>')
def fail(total_score, average_score):
    return "Sorry!! you've failed the test & scored:" + str(total_score) + " | Average score: " + str(average_score)

## Routes to calculate result and URL Redirection with HTML page rendering
@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        # Retrieve form data
        subject1 = float(request.form['maths'])
        subject2 = float(request.form['science'])
        subject3 = float(request.form['history'])

        # Calculate scores
        total_score = subject1 + subject2 + subject3
        average_score = (total_score / 3)
        average_score = round(average_score,2)

        ## return render_template('form.html', total_score=total_score, average_score=average_score)

        res=""

        if average_score >= 50 and total_score >= 150:
            res = "success"
        else:
            res = "fail"
        
        return redirect(url_for(res, total_score=total_score, average_score=average_score))
    
## Flask API Creation
@app.route('/api', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])

    return jsonify(a_val+b_val)

if __name__ == "__main__":
    '''
    debug = True helps to show changes without stopping Flask Server

    app.run() --> takes 2 args, host and port, by default its runs on server: 'localhost' at port: 5000 
    '''
    app.run(debug=True)