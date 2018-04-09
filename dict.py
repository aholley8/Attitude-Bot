
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
        if entry == 'more':
            return self.readKeys()
        if entry in self.dictionary:
            return str(self.dictionary[entry][1])
        return str("Command not found. Use _*!help*_ to list available commands")

    def readKeys(self):
        listKeys = "```"
        for key in self.dictionary.keys():
            listKeys += '!' + key + ' - ' + self.dictionary[key][0] + '\n'
        listKeys += "```"
        return listKeys

