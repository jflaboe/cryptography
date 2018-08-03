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


print "\n\nOriginal text"
print text

print "\nSingle letter frequencies"
print text.ngram_freq(1)

print "\nTrigram frequencies"
print text.ngram_freq(3)

print "\nFirst replacement"
text.replace_val('8', 'E')
text.replace_val('4', 'H')
text.replace_val(';', 'T')
print text

print "\nSecond replacement"
text.replace_val('(', 'R')
text.replace_val('d', 'O')
text.replace_val('?', 'U')
text.replace_val('3', 'G')
print text

print "\nThird replacement"
text.replace_val(')', 'S')
text.replace_val('*', 'N')
text.replace_val('6', 'I')
text.replace_val('9', 'M')
text.replace_val('5', 'A')
print text

print "\nFourth replacement"
text.replace_val('s', 'D')
text.replace_val('0', 'L')
text.replace_val('1', 'F')
text.replace_val('2', 'B')
text.replace_val(':', 'Y')
text.replace_val('-', 'C')
text.replace_val('.', 'P')
text.replace_val(']', 'W')
text.replace_val('p', 'V')
print text

