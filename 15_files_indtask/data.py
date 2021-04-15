import requests
question_data = str(requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean").text)
    
