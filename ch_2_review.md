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
  
  <li> A monoalphabetic cipher is a simple substitution cipher in which each letter is mapped uniquely to another. Therefore there are 26! possible keys.
  </li><br><br>
  
  <li> The Playfair cipher is a substitution cipher that is not monoalphabetic. The key is formed using a 5x5 grid, one space for each letter except for i/j, which share a space. The plain text is encoded two letters at a time. If the letters are in the same row of the key square, the next letter in the same row replaces the letter in the plain text. If the letters are in the same column, then the next letter in the column replaces the letter in the plain text. Otherwise, 
  </li>
  
</ol>
<h3 id="problems">Problems</h3><br>
<h3 id="coding">Coding Problems</h3><br>
