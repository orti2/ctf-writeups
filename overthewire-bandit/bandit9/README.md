# Bandit 9

### Links

- [Bandit Level](https://overthewire.org/wargames/bandit/bandit10.html)
#### Level Description
The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.

### Steps
---
In this level the *data.txt* file is not completely human-readable. It is also preceded by (=) characters. The ***strings*** utility has a good use here. By default this command outputs sequences bytes that are printable and have a minimum length of four characters. 
```
bandit9@bandit:~$ strings data.txt 
B4Qle
x<9s
f`      W0
?`YOd45
Iiuv
|S5j
hZOh|
Q~4     py
1Jec
EA      k
HZpEm
hI! 
7wzP
4========== the#
```
We can see there is a lot of output and I did not include all of it. However, the last line from what I included could be a good indicator. We can also use the *grep* command to find all the lines that include a (=) character. In combination it looks like this:
```
bandit9@bandit:~$ strings data.txt | grep "="
4========== the#
5P=GnFE
========== password
'DN9=5
========== is
$Z=_
=TU%
=^,T,?
W=y 
q=W 
X=K,
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
```

We have found the password!

***G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s***