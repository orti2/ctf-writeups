# Bandit 5

### Links

- [Bandit Level](https://overthewire.org/wargames/bandit/bandit6.html)
- [Find Command](https://www.geeksforgeeks.org/find-command-in-linux-with-examples/)
#### Level Description
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:


- human-readable
- 1033 bytes in size
- not executable

### Steps
---
Similar to the previous level, we have a folder of interest called ***inhere***.
```
bandit4@bandit:~$ ls
inhere
```
Indide this directory there a a total of 20 directories:
```
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere04  maybehere08  maybehere12  maybehere16
maybehere01  maybehere05  maybehere09  maybehere13  maybehere17
maybehere02  maybehere06  maybehere10  maybehere14  maybehere18
maybehere03  maybehere07  maybehere11  maybehere15  maybehere19
```
In the list of suggested commands we can find the ***find*** command. If we see the command's help page we can see three flags that can be used to find exactly what we want:
```
PATTERN
      -links N -lname PATTERN -mmin N -mtime N -name PATTERN -newer FILE
      -nouser -nogroup -path PATTERN -perm [-/]MODE -regex PATTERN
      -readable -writable -executable
      -wholename PATTERN -size N[bcwkMG]
```
We can use the following flags or switches: ***-readable***, ***-size***, ***-executable***. There is a catch with the executable option. If we you see the resource attached for the ***find*** command you'll see that these options are *expressions*, and expressions can be negated using the ***!*** operator. With that said, the command should look like this:

```
bandit5@bandit:~/inhere$ find -readable -size 1033c ! -executable
./maybehere07/.file2
```
That file stands out, it matches with all of the conditions specified.
```
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
```

Now we have the flag!

***P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU***