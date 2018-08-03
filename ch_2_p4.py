class MonoAlphabeticCipherText:
    def __init__(self, cipher):
        self.original = cipher
        self.replace = {}
    
    def replace_val(self, original, replace):
        self.replace[original] = replace
    
    def print_orig(self):
        print self.original
    
    def __repr__(self):
        txt = self.original
        for o, n in self.replace.iteritems():
            txt = txt.replace(o,n)
        return txt

    def __str__(self):
        return self.__repr__()

    
    def ngram_freq(self, n):
        grams = {}
        for i in range(len(self.original) - n + 1):
            gram = self.original[i:i+n]
            if gram in grams:
                grams[gram] += 1
            else:
                grams[gram] = 1
        
        result = [(key, val) for key, val in grams.iteritems()]
        result.sort(key=lambda x: -x[1])
        return result


with open("ch_2_p4.txt") as f:
    text = MonoAlphabeticCipherText(f.read())

