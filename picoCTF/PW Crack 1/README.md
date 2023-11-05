# PW Crack 1

### Links

- Challenge in [picoCTF](https://play.picoctf.org/practice/challenge/245)

### Additional Resources

- [robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro)

### Steps

---

#### Challenge Description & Hints

Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag in the same directory too.

#### Files

We are given two files, one is a supposed encrypted flag and the other one is a python file.

When inspecting the python file, I found there was a *xor* encryption function, however, the hints and a comment specify that modifying this function will not be beneficial to us. So I looked at the rest of the code.

#### pw_check function

```
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "691d"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```

We can see here that this function first asks us for an input but its not formatted so we can enter whatever we want, however, in the following line we see an *if* statement checking if what we entered is specifically *691d*, followed by a message welcoming us. So I tried using that as my input:

```
python3 level1.py 
Please enter correct password for flag: 691d
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_56891419}
```
And there is our flag!

***picoCTF{545h_r1ng1ng_56891419}***
