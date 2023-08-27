# logon

### Links

- Challenge in [picoCTF](https://play.picoctf.org/practice/challenge/46)

### Additional Resources
- [Burpsuite Community Edition](https://portswigger.net/burp/communitydownload)

### Steps
---
#### Challenge Description

The descriptions basically tells us to attempt to log in as the user "Joe".

#### Page Source

After reviewing the page source we can see that the login form uses the post method for authentication. We can further analyze this using BurpSuite.

#### BurpSuite

What seemed most interesting to me within the request are the following:

```
user=Joe&password=Hello
```
I thought I could modify the password input to work around the login but that was not the case.
```
password=; username=x; admin=False;
```
These values from the cookie section from the post request could mean something. After changing the "username" value and following the redirect we that it prompts the following above the login form:  "*I'm sorry Joe's password is super secure. You're not getting in that way.*", this could possibly mean we are on the right track. Additionally, we can see a new GET request appear on the proxy history from the "/flag" url. After seeing this request can notice the same values in the cookie section. 

Now, what if we change the admin value in this new request?
```
admin=True;
```
Success! Now we can see the flag in the response.

***picoCTF{th3_c0nsp1r4cy_l1v3s_0c98aacc}***

