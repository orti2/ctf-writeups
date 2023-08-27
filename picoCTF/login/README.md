# login

### Links

- Challenge in [picoCTF](play.picoctf.org/practice/challenge/200)

### Additional Resources
- [base64](https://base64.guru/learn/what-is-base64)

### Steps
---
#### Challenge Description

No hints or suggestions come from the description and no additional hints are provided.

#### Page Source

After reviewing the page source we can see that there is an *index.js* file which we can access through the browser.
```
    <head>
        <link rel="stylesheet" href="styles.css">
        <script src="index.js"></script>
    </head>
```
#### index.js
```
(async()=>{await new Promise((e=>window.addEventListener("load",e))),document.querySelector("form").addEventListener("submit",(e=>{e.preventDefault();const r={u:"input[name=username]",p:"input[name=password]"},t={};for(const e in r)t[e]=btoa(document.querySelector(r[e]).value).replace(/=/g,"");return"YWRtaW4"!==t.u?alert("Incorrect Username"):"cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ"!==t.p?alert("Incorrect Password"):void alert(`Correct Password! Your flag is ${atob(t.p)}.`)}))})();
```
Something stands out from here and its this:
```
cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ
```
It looks like it base64 encoded.
```
echo "cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ" | base64 -d
picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}base64: invalid input
```

Success! Now we can see the flag in the output.

***picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}***