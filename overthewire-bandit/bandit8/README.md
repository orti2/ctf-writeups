# Bandit 7

### Links

- [Bandit Level](https://overthewire.org/wargames/bandit/bandit8.html)
#### Level Description
The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once.

### Steps
---
Similarly to the previous level, we have a file called ***data.txt*** in our home directory. 
```
bandit7@bandit:~$ ls
data.txt
```
We can use the ***uniq*** command to display the line that only occurs once with a specific flag, however, this command expects to receive its input in a sorted sequence. For this we can use the ***sort*** command and pipe the output to the ***uniq*** command. The ***-u*** flag is used to print unique lines:
```
bandit8@bandit:~$ uniq --help
...
-u, --unique          only print unique lines
```
Now to use the combination of both commands:

```
bandit8@bandit:~$ sort data.txt | uniq -u
EN632PlfYiZbn3PhVK3XOGSlNInNE00t
```

We have found the flag!

***EN632PlfYiZbn3PhVK3XOGSlNInNE00t***