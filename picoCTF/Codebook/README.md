# Codebook

### Links

- Challenge in [picoCTF](play.picoctf.org/practice/challenge/238)

### Steps
---
#### Challenge Description & Hints

This description is relatively straightforward and the hints state that the *str_xor* function does not need to be modified.

#### Files

We need to use the given files :*code.py* and *codebook.txt*.

#### Python

In the *code.py* file we can see the *str_xor* function from the hints. However, we are not supposed to modify that. The *main* function only calls the *print_flag* function, which reads a file called *codebook.txt*. There is an exception in this function for when the file is not found. 

```
def print_flag():
  try:
    codebook = open('codebook.txt', 'r').read()

    password = codebook[4] + codebook[14] + codebook[13] + codebook[14] +\
               codebook[23]+ codebook[25] + codebook[16] + codebook[0]  +\
               codebook[25]

    flag = str_xor(flag_enc, password)
    print(flag)
  except FileNotFoundError:
    print('Couldn\'t find codebook.txt. Did you download that file into the same directory as this script?')

```
So the *codebook.txt* file should be located in the same directory as this file.
After having both files in the same directory, we can run the main one.

```
python3 code.py 
picoCTF{c0d3b00k_455157_197a982c}
```

Success! Now we can see the flag in output.
***picoCTF{c0d3b00k_455157_197a982c}***