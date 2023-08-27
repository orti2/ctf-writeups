# where are the robots

### Links

- Challenge in [picoCTF](play.picoctf.org/practice/challenge/4)

### Additional Resources

- [robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro)

### Steps

---

#### Challenge Description & Hints

The descriptions asks us if we can find the "robots".

#### Directories & Files

After doing a quick search based on the the hints I stumbled upon *robots.txt* file. Which is present in this case.

In the *Disallow* section of the file we can see the following file:
```
Disallow: /1bb4c.html
```

Lets see what is in here.

Success! We can see the flag in this page.

```
Guess you found the robots
picoCTF{ca1cu1at1ng_Mach1n3s_1bb4c}
```

***picoCTF{ca1cu1at1ng_Mach1n3s_1bb4c}***

