import json
from requests import get

x = get("https://opentdb.com/api.php?amount=12&difficulty=easy&type=boolean").text
data = json.loads(x)

question_data = data["results"]
