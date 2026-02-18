#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')

    print("Status Code: {}".format(r.status_code))

    for i in r.json():
        print(i["title"])

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = r.json()

    new_dict = []
    for i in data:
        new_dict.append({
            "id": i["id"],
            "title": i["title"],
            "body": i["body"] 
        })

    with open("posts.csv", "w") as csvfile:
        write = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
        write.writeheader()
        write.writerows(new_dict)