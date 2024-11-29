# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        return [word for word in words if sorted(self.word) == sorted(word.lower())]

listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])
# => ['inlets']
