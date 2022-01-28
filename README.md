# FriedmanMethod
Friedman's Method in Python, including graphical display of frequencies. In this case, I'll be using the simpler Vigenere variant, where reetition of the key is possible because the key is a smaller length than the plaintext message itself.


## Simple Vigenere Cipher

The method uses a Vigenere table which consists of a 26 by 26 square of alphabets, each alphabet shifted to the left and this corresponds to the 26 possible Ceaser chipers (we know that the Vigenre cipher is based on interwoven Caeser ciphers.

![Vigenere Table](https://user-images.githubusercontent.com/78870995/151580827-e977891f-c536-4032-b992-97f56d08dc2f.png)

During the encryption process, the cipher uses different alphabets from one of the rows, which one depends on the repeating keyword.

For key generation, the user-chosen keyword is repeated until it matches the plaintext length. The program has a clear UI that explains the process to the user.

### Vigenere Encryption Example

| Input | Keyword | Key | Output
| ------------- | ------------- | ------------- | ------------- |
| hello  | ab  | ababa | hflmo |

The first letter of the input (plaintext), ```h``` is paired with ```a```, the first letter of the key. So you use row ```h```, column ```a``` of the Vigenere Table, which is ```h```.

The second letter of the input, ```e``` is paired with ```b```. This corresponds to row ```e```, column ```b```, which is ```f```. 

This is repeated for each letter of the plaintext.

### Vigenere Decryption Example

Decryption is carried out by going to the row corresponding to the key, finding the position of the ciphertext letter in that row, and using the column's label as the plaintext letter.

So, in row ```a```, the ciphertext ```h``` appears in the ```h``` column. So the plaintext is ```h```. This is repeated.

### Encryption and Decryption in the Context of Code

For the purposes of programming the Vigenere Cipher, we use algebra where the letters A to Z correspond to numbers 0 to 25.

#### Encryption

PLaintext input (P) and key (K) are added modulo 26.
Ei = (Pi + Ki) mod 26

#### Decryption

Di = (Ei - Ki + 26) mod 26.



