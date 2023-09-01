# Bandit 0

### Links
- [Bandit Level](https://overthewire.org/wargames/bandit/bandit1.html)
#### Level Description
The password for the next level is stored in a file *readme* located in the*** home*** directory.
### Steps
---
We can see the file that contains the password for the next level by using the **ls**  utility to see to see the contents of the current directory.
```
bandit1@bandit:~$ ls
readme
```

Using the ***cat*** utility is simple way of seeing what is inside the file. But how can we specify or make reference to the file we want? The file is named in a challenging way. We cant simply do the following
```
bandit1@bandit:~$ cat -
```
In the linux command line the hyphen (-) has its a whole different use when used a context like this one. In this case it changes the behaviour of  the ***cat*** utility to concattenate what is read in the standard input.
```
bandit1@bandit:~$ cat -
Hello World!
Hello World!
Goodbye!
Goodbye!

```
So we have to look for a way to work around this. Here simple way that came to my mind. Using the dot (.) and forward slash (/) to refer to a file within the current directory and then specifying the name of the file, like such:
```
bandit1@bandit:~$ cat ./-
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
```
And now we have the flag!

***rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi***