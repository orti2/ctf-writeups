# Scavenger Hunt

### Links

- Challenge in [picoCTF](https://play.picoctf.org/practice/challenge/161)

### Steps

---

#### Challenge Description & Hints

The descriptions mentions that there is interesting information hidden around the referenced site.

#### Page Source

After reviewing the page source we can see there are at least two other files within the site that we can access through the browser these are *mycss.css* stylesheet and *myjs.js*. The first part of the flag is commented here at the bottom too! 

```
<!-- Here's the first part of the flag: picoCTF{t -->
```

#### mycss.css

At the bottom of the file the second part of the flag can also be found as a comment!

```
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```

Change the method to something like:

```
HEAD /index.php HTTP/1.1
```
#### myjs.js

A piece of the flag can't be found in here but we can find this hint in a comment at the bottom of the script.

```
/* How can I keep Google from indexing my website? */
```
This points towards a robots.txt file.

#### robots.txt

The file is present and the third part of the flag is here too.

```
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```

#### Common files in apache servers

I had assistance from a peer on this step since I could not figure it out nor was familiar with the [.htaccess](https://httpd.apache.org/docs/2.4/howto/htaccess.html) file. This file is a configuration file commonly found on Apache web servers. It is used to override specific settings from the main Apache configuration files when configured.
```
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```
#### Mac file hint

The last hint points towards a certain file that can store information on Mac Operating Systems. This file is [.DS_Store](https://buildthis.com/ds_store-files-and-why-you-should-know-about-them/) and it can be found in the site!

```
Congrats! You completed the scavenger hunt. Part 5: _a69684fd}
```
Now we can piece together the flag to obtain it!

***picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_a69684fd}***
