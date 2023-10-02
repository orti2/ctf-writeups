# basic-mod1

### Links

- Challenge in [picoCTF](https://play.picoctf.org/practice/challenge/253)

### Steps

### Additional Resources

- [Modulo](https://www.geeksforgeeks.org/modular-division/)

---
#### Challenge Description & Hints

We found this weird message being passed around on the servers, we think we have a working decryption scheme. Download the message [here](https://artifacts.picoctf.net/c/129/message.txt). Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format 

#### Files

We are provided a text file called *message.txt*.

#### Python

I made the following python script based on the challenge description to decode the message:

```
import string

numbers = [350, 63, 353, 198, 114, 369, 346, 184, 202, 322, 94, 235, 114, 110, 185, 188, 225, 212, 366, 374, 261, 213] 
word = []
mod = []
upper = list(string.ascii_uppercase)
special = [n for n in range(10)]
dictionary = upper + special + ['_']

for i in numbers:
    a = i%37
    word.append(dictionary[a])

word = ''.join([str(n) for n in word])

print("picoCTF{" + word + "}")

```

I defined a python list to represent the numbers privided in the message:

```
numbers = [350, 63, 353, 198, 114, 369, 346, 184, 202, 322, 94, 235, 114, 110, 185, 188, 225, 212, 366, 374, 261, 213] 
```

I found the *list(string.ascii_uppercase)* from the *string* module very handy to quickly define a list with ascii uppercase characters:

```
upper = list(string.ascii_uppercase)
```
Another list for the special characters (which are just numbers from 0 to 10):

```
special = list(range(10)
```

And then I defined a list called *dictionary* which contains all the specified items for mapping/decrypting the message. "*map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format*":

```
dictionary = upper + special + ['_']
```

And finally, the algorithm (for loop) for decrypting the message:

```
for i in numbers:
    a = i%37
    word.append(dictionary[a])
```

This iterates through the list to find the modular division by 37 of each item and the the result is used as the index of the dictionary to select the character from. 

```
python script.py
picoCTF{R0UND_N_R0UND_ADD17EC2}
```

And there is the flag!

***picoCTF{R0UND_N_R0UND_ADD17EC2}***
