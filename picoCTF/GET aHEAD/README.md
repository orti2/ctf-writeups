# GET aHEAD

### Links

- Challenge in [picoCTF](play.picoctf.org/practice/challenge/132)

### Additional Resources
- [Burpsuite Community Edition](https://portswigger.net/burp/communitydownload)

### Steps
---
#### Challenge Description & Hints

The descriptions does not hint a lot but the hints suggest to use a tool like BurpSuite and that there may be more than two choices.

#### Page Source

After reviewing the page source we can see that there are two submit forms, each of these use methods "GET" and "POST" with red and blue as their corresponding colors.

#### BurpSuite

After analyzing both requests with BurpSuite nothing special can be found in their respective responses. However, based on the description and hints, it might be worth the while to modify the request and use another HTTP method like "HEAD", as suggested by the challenge name and description.

```
POST /index.php HTTP/1.1
```
Change the method to something like:
```
HEAD /index.php HTTP/1.1
```
Success! Now we can see the flag in the response.
***picoCTF{th3_c0nsp1r4cy_l1v3s_0c98aacc}***