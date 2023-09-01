# Bandit 2

### Links

- [Bandit Level](https://overthewire.org/wargames/bandit/bandit3.html)
#### Level Description
The password for the next level is stored in the only human-readable file in the ***inhere directory***.
### Steps
---
We can see the file that contains the password for the next level by using the **ls**  to see to see the contents of the current directory.
```
bandit2@bandit:~$ ls
spaces in this filename
```
The easiest solution that came across my mind was to use tab comletion to address the file we want to use the **cat** utility on like this:
```
bandit2@bandit:~$ cat spaces\ in\ this\ filename 
```
Now we can see how to address or refer to spaces in file names in the linux command line. It is done with a backward slash and a space.
```
bandit2@bandit:~$ cat spaces\ in\ this\ filename 
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
```
And now we have the flag!

***aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG***