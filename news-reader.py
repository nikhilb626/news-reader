import requests
import json


# create speak function to read the news
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.Spvoice")
    speak.speak(str)


if __name__=='__main__':
# now request to fetch data from website through API
    speak("news of the day")
    url="http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=76b7bea6f2584e839a66a22c8eb1d397"
    news=requests.get(url).text

# convert the strings to readable  json arguments 
    news=json.loads(news)
    print(news["articles"])
    arts=news["articles"]

# iterate the news article,title or descriptions
    for article in arts:
        speak(article['title'])
        speak("moving on the next news..listen carefully")