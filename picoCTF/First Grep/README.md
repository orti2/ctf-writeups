# First Grep

### Links

- Challenge in [picoCTF](play.picoctf.org/practice/challenge/85)

### Additional Resources
- [Grep and Regular Expressions](https://ryanstutorials.net/linuxtutorial/grep.php)

### Steps
---
#### Challenge Description

The descriptions asks us if we can find the flag in a certain file given to us. 

#### Files

A file is given to us which contains 6 very long lines of text

```
wc -l file 
6 file
```

#### Grep Command

Based on the format of the picoCTF flags we can attempt to use the grep command in a simple way to find the pattern within the text file or match it with a regular expression.
```
cat file | grep picoCTF
```
Success! Now we can see the flag displayed in the output.

***picoCTF{grep_is_good_to_find_things_5af9d829}***