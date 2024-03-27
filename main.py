import requests
from send_email import send_email

topic = "tesla"

api_key = "4a4892855d6c4e55b2fef56c04f2af3e"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-02-27&sortBy=publishedAt&apiKey=4a4892855d6c4e55b2fef56c04f2af3e"


request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        print(article['description'])
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)