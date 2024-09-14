import requests
from jarvis.voice import speak, take_command
from bs4 import BeautifulSoup
from newsapi import NewsApiClient


def news(category='general', description=False):
    newsapi = NewsApiClient(api_key='676a27920acb4b998181489e7a362160')
    top_headlines = newsapi.get_top_headlines(language='en', category=category, country='in')
    speak(f"Top {category} news are")
    if description:
        if len(top_headlines['articles']) < 5:
            for i in range(len(top_headlines['articles'])):
                speak(top_headlines['articles'][i]['title'])
                speak(top_headlines['articles'][i]['description'])
        else:
            for i in range(5):
                speak(top_headlines['articles'][i]['title'])
                speak(top_headlines['articles'][i]['description'])
    else:
        if len(top_headlines['articles']) < 5:
            for i in range(len(top_headlines['articles'])):
                speak(top_headlines['articles'][i]['title'])
        else:
            for i in range(5):
                speak(top_headlines['articles'][i]['title'])


def quantum_physics_news():
    url = 'https://scitechdaily.com/tag/quantum-physics/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    news = []
    for x in list(dict.fromkeys(headlines)):
        print(x.text.strip())
        news.append(x.text.strip())
    speak("Top quantum  news are")
    if len(news) < 5:
        for i in range(len(news)):
            speak(news[i])
    else:
        for i in range(5):
            speak(news[i])


def main(command):
    activity = []
    if 'descri' in command:
        describe = True
        activity.append('describe')
    elif 'headlines' in command:
        describe = False
        activity.append('headlines')
    else:
        speak("Sir do you want to just hear the headlines or want to hear description as well")
        query = take_command()
        if 'descri' in query:
            describe = True
            activity.append('describe')
        else:
            describe = False
            activity.append('headlines')
    if 'quantum' in command:
        quantum_physics_news()
        activity.append('quantum')
    elif 'sports' in command:
        news('sports', describe)
        activity.append('sports')
    elif 'science' in command:
        news('science', describe)
        activity.append('science')
    elif 'health' in command:
        news('health', describe)
        activity.append('health')
    elif 'business' in command:
        news('business', describe)
        activity.append('business')
    elif 'entertainment' in command:
        news('entertainment', describe)
        activity.append('entertainment')
    elif 'tech' in command:
        news('tech', describe)
        activity.append('tech')
    else:
        news(description=describe)
        activity.append('general')
    return activity
