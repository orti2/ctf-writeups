# Bandit 3

### Links

- [Bandit Level](https://overthewire.org/wargames/bandit/bandit4.html)
#### Level Description
The password for the next level is stored in a file called spaces in this filename located in the home directory
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
We have the same issue where we can't simply refer to any of these files 
```
bandit2@bandit:~$ cat spaces\ in\ this\ filename 
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
```
And now we have the flag!

***aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG***