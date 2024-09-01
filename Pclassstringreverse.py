class reverse:
    def __init__(self,sentence):
        self.sentence = sentence
    def reverse(self,sentence):
        for i in sentence:
            sentence = list(sentence)
            i = i[::-1]
            sentence.append(i)
        return sentence
r= reverse(["Hello","World"])
print(r.reverse(["Hello","World"]))

