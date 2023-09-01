# Bandit 10

### Links

- [Bandit Level](https://overthewire.org/wargames/bandit/bandit11.html)
#### Level Description
The password for the next level is stored in the file data.txt, which contains base64 encoded data

### Steps
---
In this level the *data.txt* is base64 encoded:
```
bandit10@bandit:~$ cat data.txt 
VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==
```
We can easily decode this using the *base64* utility:
```
bandit10@bandit:~$ base64 -d data.txt 
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
```

And there we have the password!

***6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM***

