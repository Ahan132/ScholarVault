import csv
from flask import Flask, request

def search():
    correct_posts = []
    subject = request.form['subject']
    course = request.form['course']
    with open('posts.csv', 'r') as data:
        for row in csv.DictReader(data):
            if row['course'] == course and row['subject'] == subject:
                row["pid"] = int(row["pid"])
                row["score"] = int( row["score"])
                row["score"] = row["upvotes"] + row['pid'] 
                correct_posts.append(row)
    
    
    for current in range(len(correct_posts)):
        max_rel = current
        for i in range(current, len(correct_posts)):
            if correct_posts[i]["score"] > correct_posts[max_rel]["score"]:
                max_rel = i
        temp = correct_posts[current]
        correct_posts[current] = correct_posts[max_rel]
        correct_posts[max_rel] = temp

    sorted_posts = correct_posts
        

