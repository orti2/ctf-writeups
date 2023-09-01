# Bandit 4

### Links

- [Bandit Level](https://overthewire.org/wargames/bandit/bandit5.html)
#### Level Description
The password for the next level is stored in the only human-readable file in the inhere directory.
### Steps
---
Similar to the previous level, we have a folder of interest called ***inhere***.
```
bandit4@bandit:~$ ls
inhere
```
Now we can see ten different file named similarly:
```
bandit4@bandit:~/inhere$ ls
-file00  -file02  -file04  -file06  -file08
-file01  -file03  -file05  -file07  -file09
```
We have the same issue where we can't simply use the exact name of the file so that needs to be worked around. I did a simple yet effective trick with the ***file*** command.
```
bandit4@bandit:~/inhere$ file ./*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: Non-ISO extended-ASCII text, with no line terminators
```
-file07 sticks out.

```
bandit4@bandit:~/inhere$ cat ./-file07 
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

```
And there we have the flag!

***lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR/***