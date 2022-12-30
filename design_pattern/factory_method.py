class FrenchLocalizer:
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicycle",
                             "cycle": "cycle"}

    def localize(self, msg):
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    def __init__(self):
        self.translation = {"car": "Tuxedo", "bike": "nike",
                            "cycle":"module"}

    def localize(self, msg):
        return self.translation.get(msg, msg)

class EnglishLocalizer:
    def localize(self, msg):
        return msg

def Factory(language="English"):
    localizes = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizes[language]()

if __name__ == "__main__":

    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))