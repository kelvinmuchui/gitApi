from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello")
def hello():
	return "hello"

#geting use post and adding
@app.route("/", methods= ['GET', 'POST'])
def home():
    if request.method == 'POST':
    	value_one = int(request.form['number_one'])
    	value_two = int(request.form['number_two'])
        total = value_one + value_two
        return render_template('index.html', value = total)	
    return render_template('index.html')		    


if __name__ == '__main__':
	app.run(debug=True)