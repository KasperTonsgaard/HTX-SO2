import fakeNewsGenerator as fng
import pyttsx3
import time



def SayFakeNews(numberOfTimes=1):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 160)
    i = 0
    while i < numberOfTimes:
        i += 1
        fakeNews = []
        fakeNewsPlusTopic = fng.GenerateFakeArticles()
        for fakeNewPlusTopic in fakeNewsPlusTopic:
            fakeNews.append(fakeNewPlusTopic[0])
        for news in fakeNews:
            engine.say(news)
            engine.runAndWait()

        time.sleep(15)

