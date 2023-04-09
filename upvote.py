import csv
from flask import Flask, request

app = Flask(__name__)

@app.route('/upvote', methods=['POST'])
def create_account():
    score = request.form['score']
    pid = request.form['pid']
    with open('posts.csv', mode='r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csvfile:
            if pid == row['pid']: 
                row['upvotes'] += score


    return 'Score Changed'

