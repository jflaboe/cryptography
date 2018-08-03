<h1>
  Chapter 2 Review Solutions
</h1><br><br>

<a href="#conceptual">
  Conceptual Questions
</a><br>
<a href="#problems">
  Problems
</a><br>
<a href="#coding">
  Coding Problems
</a><br><br>

<h3 id="conceptual">
  Conceptual Questions
</h3><br>

<ol>
  <li>
    Each symmetric cipher requires:
    <ol>
      <li>
        A plain text
      </li>
      <li>
        A cipher text
      </li>
      <li>
        A secret key
      </li>
      <li>
        An encryption algorithm
      </li>
      <li>
        A decryption algorithm
      </li>
    </ol>
  </li><br><br>         
  
  <li>
    The two basic functions used by an encryption algorithm:
    <ol>
      <li>
        Substitution
      </li>
      <li>
        Transposition
      </li>
    </ol>
  </li><br><br>
  
  <li>
    Only one key is required for two people to communicate via a cipher.
  </li><br><br>
  
  <li>
    The main difference between a stream cipher and a block cipher is that for a stream cipher, encryption is applied to one element at a time whereas, in a block cipher, encryption is applied to a block of elements at a time.
  </li><br><br>
  
  <li>
    The two ways to approach breaking a cipher are brute-force methods and cryptanalytic methods.
  </li><br><br>
  
  <li>
    Below is the list of crytanalytic attack types and what the attacker knows for each attack
    <ol>
      <li>
        Ciphertext only:
        <ul>
          <li>
            the cipher text
          </li>
          <li>
            the encryption algorithm
          </li>
        </ul>
      </li>
      <li>
        Known plain text
        <ul>
          <li>
            the cipher text
          </li>
          <li>
            the encryption algorithm
          </li>
          <li>
            One or more plaintext-ciphertext pairs formed by with the secret key
          </li>
        </ul>
      </li>
      <li>
        Chosen plain text
        <ul>
          <li>
            the cipher text
          </li>
          <li>
            the encryption algorithm
          </li>
          <li>
            Plain text chosen by the cryptanalyst, together with its corresponding cipher text formed by the secret key
          </li>
        </ul>
      </li>
      <li>
        Chosen cipher text
        <ul>
          <li>
            the cipher text
          </li>
          <li>
            the encryption algorithm
          </li>
          <li>
            Purported cipher text, together with the corresponding decrypted plain text formed by the secret key
          </li>
        </ul>
      </li>
    </ol>
  </li><br><br>
  
  <li>
    The difference between an unconditionally secure cipher and a computationally secure cipher is that a computationally secure cipher can be solved by brute force without the key, but the value of the information encoded is lost by the time someone would be able to decode the message whereas an unconditionally secure cipher cannot be solved without the secret key.
  </li><br><br>
  
  <li>
    The Caesar cipher is the most basic monoalphabetic cipher, where each letter is substituted with the letter some <i>n</i> letters in front of it. Therefore, there are only 26 unique keys.
  </li><br><br>
  
  <li>
    A monoalphabetic cipher is a simple substitution cipher in which each letter is mapped uniquely to another. Therefore there are 26! possible keys.
  </li><br><br>
  
  <li>
    The Playfair cipher is a substitution cipher that is not monoalphabetic. The key is formed using a 5x5 grid, one space for each letter except for i/j, which share a space. The plain text is encoded two letters at a time. If the letters are in the same row of the key square, the next letter in the same row replaces the letter in the plain text. If the letters are in the same column, then the next letter in the column replaces the letter in the plain text. Otherwise, 
  </li><br><br>
  
  <li>
    The difference between a monoalphabetic cipher and a polyalphabetic cipher is that a monoalphabetic cipher has only one alphabet, meaning that each letter only maps to one other unique letter, whereas a polyalphabetic cipher may have multiple alphabets, where a letter might not uniquely map to another letter, and instead map to multiple letters.
  </li><br><br>
  
  <li>
    A one-time pad is a cipher for which a key that is the length of the cipher text is used and discarded after the key is used once. Two problems with this method is that a key must be generated for every message and it is difficult to give the key to the receiver to decode without additional measures of security.
  </li><br><br>
  
  <li>
    A transposition cipher is any cipher in which the characters of plain text are reorganized to form a cipher text.
  </li><br><br>
  
  <li>
    Steganography is the method of concealing plaintext withing a broader message or media. For instance, you could conceal the message in an image, using the least significant bit for the color as the bit to store the message in. It is not necessarily considered encryption.
  </li><br><br>
  
</ol><br><br>
<h3 id="problems">Problems</h3><br>
<ol>
  <li>
    Affine Cipher
    <ol>
      <li>
        There are no limitations on <i>b</i> for an affine cipher. The reason is there exists a one to one relationship between plain text characters and cipher text characters when shifting by a constant number of characters. 
      </li>
      <li>
        This is unlike the constant <i>a</i>, which multiplies the plain text character by a value. Multiple inputs may have the same result with the same multiplicative constant, therefore, the function is not one to one. Some values of <i>a</i> work and others don't. We must have <i>a</i> be relatively prime to the modulus base, in this case 26. 
      </li>
      <li>
        Therefore, the values of <i>a</i> that are allowed are 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, and 25.
      </li>
    </ol>
  </li><br><br>
  <li>
    Limiting <i>b</i> to values less than 26, we find there are 26 * 12 = 312 possible one to one Affine ciphers. Out of the 312, 26 of them are Caesar ciphers (with <i>a</i> = 1)
  </li><br><br>
  <li>
    In order to solve the problem we assume that 'B' (<i>n</i>=1) corresponds to 'E' (<i>n</i>=4) and that 'U' (<i>n</i>=20) corresponds to 'T' (<i>n</i>=19), based upon general letter frequencies. We then have a linear system of equations: <br><br> 
    4<i>a</i> + <i>b</i> = 1 <i>mod</i> 26<br>
    19<i>a</i> + <i>b</i> = 20 <i>mod</i> 26<br><br>
    It is very easy to solve for <i>a</i>, since we first obtain 15<i>a</i> = 19 <i>mod</i> 26 = 26 + 19 = 45. Therefore <i>a</i> = 3. Thereafter, we use the first equation to find that <i>b</i> = 15.
  </li><br><br>
  <li>
    I created a script to help analyze the encoded text. First, as suggested, I looked at letter frequencies and ngram frequencies. We expect the word "the" the most times for trigrams and 'e' and 't' for individual letters. The most frequent characters were '8' and ';' respectively and the most frequent trigram was ';48'. This obviously fits with '8' corresponding to 'e' and ';' corresponding to 't'. We also guess that '4' is 'h'. Below is the resultant text from these assumptions (d is double dagger, s is single dagger, p is new paragraph symbol):<br><br>
    
  ```
   53dds305))6*THE26)Hd.)Hd)TE06*THEsEp60))E5TT]E*T:d*EsE3
  (EE)5*sTH6(TEE*96*?TE)*d(THE5)T5*s2:*d(TH956*2(5*-H)EE*
  TH0692E5)T)6sE)HddT1(d9THE0E1TE:Ed1THEsE5TH)
  HE5s52EE06*E1
  (d9THET(EETH(d?3HTHE)HdT161T:1EETd?T
  ```
   <br><br>In the last line, we see 'T(EETH', but really we expect 'T(EE' to be 'TREE', so we try '(' as 'R'. Then a 'THR' appears and we expect the next letter to be 'O', therefore 'd' goes to 'O'. There is also an 'H' near after, so we might expect the word 'THROUGH'. We also try '?' going to 'U' and '3' going to 'G'. We then have:<br><br>
```  
5GOOsG05))6*THE26)HO.)HO)TE06*THEsEp60))E5TT]E*T:O*EsEG
REE)5*sTH6RTEE*96*UTE)*ORTHE5)T5*s2:*ORTH956*2R5*-H)EE*
TH0692E5)T)6sE)HOOT1RO9THE0E1TE:EO1THEsE5TH)
HE5s52EE06*E1
RO9THETREETHROUGHTHE)HOT161T:1EETOUT
```
  <br><br>We see the word in the last line ')HOT', and '\*ORTH' in the second line. We expect ')' to be 'S' and '\*' to be 'N'. From this, the second line reveals the word 'THIRTEEN', if we replace '6' with 'I' and subsequentely 'MINUTES' if we replace '9' with 'M'. We also realize one of the NORTH's in the second line should be 'NORTHEAST', and we get '5' is 'A'. The new text is:<br><br>
  
```
AGOOsG0ASSINTHE2ISHO.SHOSTE0INTHEsEpI0SSEATT]ENT:ONEsEG
REESANsTHIRTEENMINUTESNORTHEASTANs2:NORTHMAIN2RAN-HSEEN
TH0IM2EASTSIsESHOOT1ROMTHE0E1TE:EO1THEsEATHS
HEAsA2EE0INE1
ROMTHETREETHROUGHTHESHOT1I1T:1EETOUT
```
  <br><br>The next obvious transformation is 's' to 'D', as the text is talking about directions and we want the word 'DEGREES'. By changing '0' to 'L', we find the word 'GLASS', and by changing '1' to 'F' we find several 'FROM's and a 'LEFT'. We guess '2' is 'B' and ':' is 'Y' to get the word 'BY' a couple times. Each other letter is used once, so we deduce them by forming words with the letters around them, and we get to our final result (A 'V' was missing in the 2nd line, presumably because the PDF couldn't print the symbol used for it):<br><br>
  A good glass in the bishop's shostel in the devils seat twenty-one degrees and thirteen minutes northeast by north main branch seventh limb east side, shoot from the left eye of the deaths head a beeline from the tree through the shot fifty feet out.
  </li><br><br>
</ol>
  
<h3 id="coding">Coding Problems</h3><br>
