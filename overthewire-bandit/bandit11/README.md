# Bandit 11

### Links

- [Bandit Level](https://overthewire.org/wargames/bandit/bandit12.html)
#### iLevel Description
The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions. 
### Steps
---
Similarly to the previous levelIn this level the *data.txt* is encoded, with rot13 in this case. It is similar to this challenge from [picoCTF](https://play.picoctf.org/practice/challenge/62). Where we have a piece of string encoded using [rot13](https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_rot13_algorithm.htm) algorithm. There are no standard GNU tools for decoding this so I resorted to an [online converter](https://rot13.com/) instead of decoding it manually. 
```
bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt 
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
```
Using the online converter we obtain the following string:
```
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
```

And now we have the password!

*** JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv***

