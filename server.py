from flask import Flask, render_template, request, redirect
import json
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('data.json', 'a') as f:
        # file = f.write()
        json.dump(data, f)

def write_to_csv(data):
    with open('data.csv', 'a') as f2:
        # file = f.write()
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(f2, delimiter=',' ,quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # return render_template('login.html', error=error)
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'form not submitted'
