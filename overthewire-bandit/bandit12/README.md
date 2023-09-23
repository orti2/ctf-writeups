# Bandit 12

### Links

- [Bandit Level](https://overthewire.org/wargames/bandit/bandit13.html)
#### Level Description
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)
### Steps
---

We are hinted that *data.txt* is a hexdump of multipple file compressions, it is also suggested to make a temporary directory under */tmp/* directory to be able to decompress the files. I decided to copy the file to my local system and do everything from there.
```

First we have to reverse the hex to obtain the file in binary and properly observe it:

```
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ xxd -r data.txt > binary
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ file binary 
binary: gzip compressed data, was "data2.bin", last modified: Sun Apr 23 18:04:23 2023, max compression, from Unix, original size modulo 2^32 581
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ 


Now we can see that what we obtained from reversing the hexdump is a gzip compressed file. We can use the gzip tool to decompress that, but first, we need to add the extension *gzip*, as it will not work otherwise:

```
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ mv binary binary.gz
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ gzip -d binary.gz  
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ ls
binary  data.txt
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ file binary 
binary: bzip2 compressed data, block size = 900k

```
Now we have a *bzip* compressed file, this can be decompressed by using the bzip2 tool, like such:

```
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ bzip2 -d binary 
bzip2: Can't guess original name for binary -- using binary.out
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ ls
binary.out  data.txt
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ file binary.out 
binary.out: gzip compressed data, was "data4.bin", last modified: Sun Apr 23 18:04:23 2023, max compression, from Unix, original size modulo 2^32 20480
```

Again, now we have a gzip compressed file, we can use the same command as before to decompress it:

```
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 2$ mv binary.out binary.gz
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ gzip -d binary.gz      
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ ls
binary  data.txt
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ file binary 
binary: POSIX tar archive (GNU)
```

Now we have a new compressed file which have not seen earlier, and in my case, never before. After a quick lookup I found out that it can be decompressed like a regular tar compressed file:

```
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ tar -xvf binary 
data5.bin
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ file data5.bin 
data5.bin: POSIX tar archive (GNU)
 
```

Similar to before, this can be decompressed the *tar* utility: 

```
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ tar -xvf data6.bin 
data8.bin
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ file data8.bin 
data8.bin: gzip compressed data, was "data9.bin", last modified: Sun Apr 23 18:04:23 2023, max compression, from Unix, original size modulo 2^32 49
```

Now we have another gzip file, after decompressing it we get a text file!
```
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ gzip -d data8.gz 
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ ls
binary  data5.bin  data6.bin  data8  data.txt
file data8
data8: ASCII text
oly@libertad:~/ctfs/ctf-writeups/overthewire-bandit/bandit12 -$ cat data8
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
```

And there is the password!

*** wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw***

