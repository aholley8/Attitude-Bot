
import json
import urllib.request

class DictionaryReader:

    def __init__(self):
        self.file = "dict.json"
        self.dictionary = {}
        self.loadDict()
        self.loop = 0

    def loadDict(self):
        try:
            with open(self.file,'r') as f:
                self.dictionary = json.load(f)
        except Exception:
            return
    
    def readDict(self, entry):
        if entry in self.dictionary:
            return str(self.dictionary[entry])
        return str("")

