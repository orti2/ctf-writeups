# basic-mod2

### Links

- Challenge in [picoCTF](https://play.picoctf.org/practice/challenge/254)

### Steps

### Additional Resources

- [Modulo](https://www.geeksforgeeks.org/modular-division/)
- [Modular Multiplicative Inverse](https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/)
---
#### Challenge Description & Hints

A new modular challenge! Download the message here. Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. Wrap your decrypted message in the picoCTF flag format 

#### Files

Similar to *basic-mod1* We are provided a text file called *message.txt*.

#### Python

I used the same python script I made for *basic-mod2* but made some modifications. I added the modular inverse function found in the resources listed and changes the input numbers as well. Additionally, the value for the modular division changes from 37 to 41, and we want the inverse instead.

```
import string

def modInverse(A, M):
 
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

numbers = [104, 372, 110, 436, 262, 173, 354, 393, 351, 297, 241, 86, 262, 359, 256, 441, 124, 154, 165, 165, 219, 288, 42] 

word = []
mod = [modInverse(n, 41) for n in numbers]
upper = list(string.ascii_uppercase)
special = [n for n in range(10)]

dictionary = upper + special + ['_']

for i in mod:
    word.append(dictionary[i-1])

word = ''.join([str(n) for n in word])

print("picoCTF{" + word + "}")
```

The write-up for the previous challenge *basic-mod1* goes further into detail regarding this script, with that said, in this version the inverse modulo is included from the function. 
```
python script.py
picoCTF{1NV3R53LY_H4RD_DADAACAA}
```

And there is the flag!

***picoCTF{1NV3R53LY_H4RD_DADAACAA}***
