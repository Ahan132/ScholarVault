import csv
from flask import Flask, request

app = Flask(__name__)

@app.route('/create_account', methods=['POST'])
def create_account():
    # retrieve data from the AJAX call 
    status = request.form['status']
    subjects = request.getlist['subject']
    courses = request.form.getlist('courses[]')
    posts = request.form.getlist('posts[]') #hey how should i see results any idea. I think that you can runn the create_post python file in the terminal that should work please tell me if it works
    upvotes = request.form['upvotes']

    # append the data to the CSV file
    with open('accounts.csv', mode='a', newline='') as csv_file:
        fieldnames = ['Status', 'Subject', 'Courses', 'Posts', 'Upvotes']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'Status': status, 'Subject': subjects, 'Courses': courses, 'Posts': posts, 'Upvotes': upvotes})

    return 'Account created successfully'

if __name__ == '__main__':
    app.run(debug=True)

