"""home page"""
from bottle import get, run
import requests
import time

# Home page UI
PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to ChatUp</title>
</head>
<body>
    <form action="http://localhost:8080/post">
        <div>
            Write a post: <textarea name="mytextarea" cols="30" rows="10"></textarea>
        </div>
        <div>
            <input type="submit" value="submit now" name="mypost">
            <input type="reset" value="reset" name="myreset">
        </div>
    </form>
    <hr>
    {previous_posts}
</body>
</HTML>
""".strip()


# API
@get("/")
def home():
    print(time.ctime())
    previous_posts = requests.get("http://localhost:8080/post/get").text
    print(time.ctime())
    return PAGE.format(**{"previous_posts": previous_posts})

run(host='localhost', port=7070)
