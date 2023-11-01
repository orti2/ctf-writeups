# Glitch Cat

### Links

- Challenge in [picoCTF](https://play.picoctf.org/practice/challenge/242)

### Steps

---
#### Challenge Description & Hints

Our flag printing service has started glitching!

#### nc

```
nc saturn.picoctf.net 52682
'picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}'
```

The flag is given to us but not in a readable format, it even looks like it can be directly plugged into python.

#### Python

```
>>> flag = 'picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}'
>>> flag
'picoCTF{gl17ch_m3_n07_bda68f75}'
```
And there is our flag!

***picoCTF{gl17ch_m3_n07_bda68f75}***
