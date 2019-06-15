from datetime import datetime
from random import randint
import wikipedia
wikipedia.set_lang("en")

randomOptions = ["summary", "summary", "category"]
#articles contain lots of uninteresting categories that are removed using this
categoriesToRemove = ["article", "stub", "wiki", "dmy", "death", "birth", "from", "language"]

messageTagOn = "[...]"
messageLength = 280 - len(messageTagOn)

def random(wanted):
    if(wanted == randomOptions[0] or wanted == randomOptions[1]):
        try:
            #sends summary of random article
            toSend = wikipedia.summary(wikipedia.search(wikipedia.random(), 1))
            if(len(toSend) > messageLength):
                return toSend[:messageLength] + messageTagOn
            else:
                return toSend
        except:
            #sends link to random article if summary cannot be found
            pass
            return ("https://en.wikipedia.org/wiki/" + wikipedia.random().replace(" ", "_")[:messageLength])
    if(wanted == randomOptions[2]):
        try:
            #removes uninteresting categories
            categories = wikipedia.WikipediaPage(wikipedia.search(wikipedia.random(), 1)).categories
            for i, category in enumerate(categories):
                categories[i] = category.lower()
            for toRemove in categoriesToRemove:
                categories = [x for x in categories if toRemove not in x]
            #sends random category
            category = categories[randint(0, len(categories) - 1)]
            return (category + " https://en.wikipedia.org/wiki/Category:" + category.replace(" ", "_"))
        except:
            pass
            return ("https://en.wikipedia.org/wiki/" + wikipedia.random().replace(" ", "_")[:messageLength])

while True:
    #if(datetime.now().minute == 0):
    print(random(randomOptions[randint(0, len(randomOptions) - 1)]))
    print()
