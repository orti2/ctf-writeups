# dont-use-client-side

### Links

- Challenge in [picoCTF](https://play.picoctf.org/practice/challenge/66)

### Steps

---

#### Challenge Description & Hints

The description asks us if we can break into a super secure portal.

#### Page Source

After viewing the page source we can see that the flag is visible in *verify* JavaScript function. However, it is split into 8 piec

```
function verify() {
checkpass = document.getElementById("pass").value;
split = 4;
if (checkpass.substring(0, split) == 'pico') {
  if (checkpass.substring(split*6, split*7) == '706c') {
    if (checkpass.substring(split, split*2) == 'CTF{') {
     if (checkpass.substring(split*4, split*5) == 'ts_p') {
      if (checkpass.substring(split*3, split*4) == 'lien') {
        if (checkpass.substring(split*5, split*6) == 'lz_b') {
          if (checkpass.substring(split*2, split*3) == 'no_c') {
            if (checkpass.substring(split*7, split*8) == '5}') {
              alert("Password Verified")
              }
            }
          }
  
        }
      }
    }
  }
}
else {
  alert("Incorrect password");
}

```

#### Rearranging the flag

The order of the different pieces of the flag are given by *y* in the *substring* function:

```
checkpass.substring(split*x, split*y) == 'CTF{'
```

Now we can rearrange the flag and obtain it!

***picoCTF{no_clients_plz_b706c5}***
