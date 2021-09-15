from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__) # instance of Flask app __main__

# @app.route('/<username>/<int:post_id>') # route directory
# def hello_world(username=None, post_id=None): # default param
#     return render_template('index.html', name=username, id=post_id)

@app.route('/') # route directory
def my_home(): # default param
    return render_template('index.html')

@app.route('/<string:page_name>') # dynamically accept url parameters
def html_page(page_name):
    return render_template(page_name) # render data that was entered in url

def write_to_file(data):
    with open('database.txt', mode='a') as database: # same folder so no need for path
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data): # use excel to open csv file
    with open('database.csv', newline='', mode='a') as database2: # same folder so no need for path
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) # where you want to write to, delimiter - what is the separater for each row, quotechar - do you want quotes around the char
        csv_writer.writerow([email,subject,message]) # write like a list


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
      return 'Something went wrong. Try again!'
 