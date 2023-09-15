# Capybara

### Additional Resources

- [Morse Code](https://www.britannica.com/topic/Morse-Code)


### Steps

---

#### Capybara image

The challenge provides us with a jpeg file of a capybara and some lemons:

```
file capybara.jpeg                
capybara.jpeg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 96x96, segment length 16, comment: "CREATOR: gd-jpeg v1.0 (using IJG JPEG v80), quality = 82", baseline, precision 8, 1200x630, components 3
```

#### File Analysis

I looked at the metadata using *exiftool* but I didn't see anything out of the ordinary:

```
exiftool capybara.jpeg  
ExifTool Version Number         : 12.65
File Name                       : capybara.jpeg
Directory                       : .
File Size                       : 158 kB
File Modification Date/Time     : 2023:09:09 12:51:33-04:00
File Access Date/Time           : 2023:09:15 10:02:01-04:00
File Inode Change Date/Time     : 2023:09:09 12:51:42-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 96
Y Resolution                    : 96
Comment                         : CREATOR: gd-jpeg v1.0 (using IJG JPEG v80), quality = 82.
Image Width                     : 1200
Image Height                    : 630
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1200x630
Megapixels                      : 0.756
```

However, I found something interesting with the *strings* utility:

```
strings capybara.jpeg | tail -n 43
audio.wav
-/m|z
}om_
Z\{u
eKO?
l<"`
x       <o
4^TW
4^TW
o.|sA
G>4^
x       <o
o.|sA
x       <o
:e5/
&'}R.
prA>4
sAd4
+3"`
x       <o
l<"`
EP"`
PbN.
l<"`
x       <o
x       <o
o.|s
G>4^
G>4^
&'}R.
.l8_
}<"`
x       <o
x       <o
G>4^
.l8g
Eua0
x       <o
G>4^
$}n$
x       <o
.]#W?
audio.wavPK
```

Here, ***audio.wav*** and ***audio.wavPK*** stood out to me, I tried to retrieve them using the *binwalk* tool and it worked!

```
binwalk -e capybara.jpeg && ls    

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
151174        0x24E86         Zip archive data, at least v2.0 to extract, compressed size: 6902, uncompressed size: 919160, name: audio.wav
158170        0x269DA         End of Zip archive, footer length: 22

capybara.jpeg  _capybara.jpeg.extracted
```

#### Audio Files

I opened the audio file in a [spectogram](https://www.sonicvisualiser.org/) but nothing stood out to me. Because of that, I decided to listen to the file and with some experience with morse code I inclined towards that, the audio patterns suggested to me a behavior similar to morse code.

#### Morse Code

I used a morse code [audio decoder](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) to further investigate and I obtained the following string (which looks like its in hexadecimal) and saved it to *output* file:
```
5 0 4 3 5 4 4 6 7 B 6 4 3 0 5 F 7 9 3 0 5 5 5 F 6 B 4 E 3 0 5 7 5 F 6 8 3 0 5 7 5 F 7 4 3 0 5 F 5 2 3 3 3 4 4 4 5 F 6 D 3 0 7 2 3 5 3 3 5 F 4 3 3 0 6 4 3 3 3 F 7 D
```

I removed the spaces using the *tr* utility:

```
tr -d " " < output > hex
```

And finally, I used the *xxd* tool to revert the hexadecimal values to binary and output them as ASCII text to obtain the flag!

```
xxd -r -p hex
PCTF{d0_y0U_kN0W_h0W_t0_R34D_m0r53_C0d3?}
```

And there is the flag!

***PCTF{d0_y0U_kN0W_h0W_t0_R34D_m0r53_C0d3?}***