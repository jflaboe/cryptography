class CipherUtility:
    """
    A Class for common operations among the Engima Machine modules
    """

    @staticmethod
    def alpha_to_index(char):
        """
        Returns the index of 0 - 25 corresponding to A - Z
        """
        return ord(char) - ord('A')

    @staticmethod
    def index_to_alpha(idx):
        """
        Given a 0 - 25 index, returns the corresponding A - Z character
        """
        
        return chr(ord('A') + idx)




class Plugboard:
    """
    An implementation of the Plugboard
    """

    def __init__(self, pairs_string):
        pairs = Plugboard.parse_pairs(pairs_string)
        self.map = Plugboard.generate_alphabet_mapping(pairs)
        

    def forward(self, char):
        """
        Performs the plugboard swap and returns the corresponding alphabet index
        """

        return CipherUtility.alpha_to_index(self.map[char])

    def reverse(self, idx):
        """
        Given an index to the plugboard, performs the reverse swap and returns the corresponding character
        """

        return self.map[CipherUtility.index_to_alpha(idx)]
    
    @staticmethod
    def parse_pairs(pairs_string):
        """
        Takes a Plugboard pair string and parses it into a list of pairs (ex: ['AB', 'CF', 'ZT'])
        """

        return pairs_string.split()

    @staticmethod
    def generate_alphabet_mapping(pairs):
        """
        Takes a list of character pairs and generates a plugboard mapping.
        """

        alphabet_map = {}

        #The plugboard maps A to A, B to B, C to C if no swaps are specified
        for i in range(26):
            alphabet_letter = CipherUtility.index_to_alpha(i)
            alphabet_map[alphabet_letter] = alphabet_letter
        
        #Change the mappings for pairs in the swap list
        for pair in pairs:
            first_letter = pair[0]
            second_letter = pair[1]

            alphabet_map[first_letter] = second_letter
            alphabet_map[second_letter] = first_letter

        return alphabet_map




class Scrambler:
    def __init__(self, alphabet_configuration, initial_shift_key='A', notch_position=0):
        self.shift_position = CipherUtility.alpha_to_index(initial_shift_key)
        self.alphabet_configuration = alphabet_configuration

        #location in the scrambler where the adjacent scrambler shifts
        self.notch_position = notch_position

    def forward(self, idx):
        """
        Given an index, forwards the signal through the scrambler to retrieve the new index
        An index corresponds to a letter on the front half of the scrambler, and is wired
        to the same letter on the other half of the scrambler, potentially at a new index,
        which is returned.
        """

        #we know the state of the wiring when unshifted, so unshift the index
        unshifted_input_idx = (idx + self.shift_position) % 26

        #convert the index to an alphabetical character, then find the matching unshifted index
        #that it's wired to
        unshifted_output_idx = self.alphabet_configuration.find(CipherUtility.index_to_alpha(unshifted_input_idx))

        #re-shift the indices to get the correct output
        shifted_output_idx = (unshifted_output_idx - self.shift_position) % 26

        return shifted_output_idx

    def shift(self):
        """
        Shifts the scrambler. Returns true if the notch position has been reached
        and the next scrambler should also be shifted
        """

        self.shift_position = (self.shift_position + 1) % 26
        
        #The notch will trigger the shift of another scrambler
        if self.shift_position == self.notch_position:
            return True

        return False

    def reverse(self, idx):
        """
        The opposite of forward. Given an index to the back half of the scrambler,
        returns the corresponding index on the front half.
        """

        #unshift the index because we know the unshifted wiring matches
        unshifted_output_idx = (idx + self.shift_position) % 26

        #convert the output index to a character, and retrieve the corresponding 0-25 A to Z index
        unshifted_input_index = CipherUtility.alpha_to_index(self.alphabet_configuration[unshifted_output_idx])

        #reshift the index
        shifted_input_index = (unshifted_input_index - self.shift_position) % 26

        return shifted_input_index



class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring
        self.rotates = False
        self.start = 0
    
    def rotate(self):
        return
    
    def forward(self, idx):
        """
        Returns the matching character index given an input index
        """
        return CipherUtility.alpha_to_index(self.wiring[idx])

    def reverse(self, idx):
        """
        The same as forward
        """
        return self.forward(idx)

class EnigmaMachine:
    def __init__(self, pb_pairs, sc_wirings, sc_keys, rf_wiring):
        self.plugboard = Plugboard(pb_pairs)
        self.scramblers = [Scrambler(sc_wirings[i], initial_shift_key=sc_keys[i]) for i in range(len(sc_keys))]
        self.reflector = Reflector(rf_wiring)

    def encode_one(self, v):

        #move forward through the plugboard
        idx = self.plugboard.forward(v)

        #the initial keypress always causes the first scrambler to shift
        shift_next = True

        #forward the input through all the scramblers, 
        #shift the next scrambler if a notch is reached
        for sc in self.scramblers:
            if shift_next is True:
                shift_next = sc.shift()
            idx = sc.forward(idx)
        
        #reflect the input
        idx = self.reflector.forward(idx)

        #reverse the output through the scramblers
        for i in range(len(self.scramblers)):
            sc = self.scramblers[len(self.scramblers) - 1 - i]
            idx = sc.reverse(idx)
        
        #reverse the output through the plugboard and return
        return self.plugboard.reverse(idx)


    def encode_all(self, s):
        output = ""
        for v in s:
            output += self.encode_one(v)
        return output


WIRING1 = "UWYGADFPVZBECKMTHXSLRINQOJ"
WIRING2 = "AJPCZWRLFBDKOTYUQGENHXMIVS"
WIRING3 = "TAGBPCSDQEUFVNZHYIXJWLRKOM"
REFLECTOR = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

PLUGBOARD_PAIRS = 'AB SZ UY GH LQ EN'
SCRAMBLER_STARTS = 'AEB'


if __name__ == "__main__":
    e = EnigmaMachine(PLUGBOARD_PAIRS, [WIRING2, WIRING1, WIRING3], SCRAMBLER_STARTS, REFLECTOR)
    print(e.encode_all("GYHRVFLRXY"))