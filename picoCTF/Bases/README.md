# Bases

### Links

- Challenge in [picoCTF](play.picoctf.org/practice/challenge/67)

### Additional Resources

- [base64](https://base64.guru/learn/what-is-base64)

### Steps

---

#### Challenge Description & Hints

The description asks us what *bDNhcm5fdGgzX3IwcDM1* means and hints that it might have something to do with bases.

#### Encoding

Based on the description and hints it might look like the string *bDNhcm5fdGgzX3IwcDM1* is base64 encoded. 

#### Decoding

Test to see if the string is indeed encoded in base64:

```
echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d
l3arn_th3_r0p35
```

It is! Now it has to be wrapped by the picoCTF flag.

Success! Now we have the flag

***picoCTF{l3arn_th3_r0p35c}***