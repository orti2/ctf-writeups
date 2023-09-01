# Bandit 7

### Links

- [Bandit Level](https://overthewire.org/wargames/bandit/bandit8.html)
#### Level Description
The password for the next level is stored in the file **data.txt** next to the word **millionth**.

### Steps
---
In this level we have a file called ***data.txt*** in our home directory. 
```
bandit7@bandit:~$ ls
data.txt
```
Since the password is next to the word *millionth* we can use a simple grep to output the whole line:
```
bandit7@bandit:~$ cat data.txt | grep "millionth"
millionth	TESKZC0XvTetK0S9xNwm25STk5iWrBvP
```
And there is our flag!

***TESKZC0XvTetK0S9xNwm25STk5iWrBvP***