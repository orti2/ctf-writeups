# Enhance!

### Links

- Challenge in [picoCTF](https://play.picoctf.org/practice/challenge/265)

### Steps

---
#### Challenge Description & Hints

Download this [image](https://artifacts.picoctf.net/c/100/drawing.flag.svg) file and find the flag.

#### Files

We are provided a SVG (Scalable Vector Graphics) file called *drawing.flag.svg* 

#### File Analysis

I went through superficial file inspection with *file* and *exiftool* utilities but did not find anything unsual or of value:

```
file drawing.flag.svg 
drawing.flag.svg: SVG Scalable Vector Graphics image
                                                                                       
┌──(parallels㉿libertad)-[~/ctf/picoCTF/Enchance]
└─$ exiftool drawing.flag.svg
ExifTool Version Number         : 12.65
File Name                       : drawing.flag.svg
Directory                       : .
File Size                       : 4.1 kB
File Modification Date/Time     : 2023:09:28 13:31:58-04:00
File Access Date/Time           : 2023:10:02 16:51:25-04:00
File Inode Change Date/Time     : 2023:09:28 13:32:05-04:00
File Permissions                : -rw-r--r--
File Type                       : SVG
File Type Extension             : svg
MIME Type                       : image/svg+xml
Xmlns                           : http://www.w3.org/2000/svg
Image Width                     : 210mm
Image Height                    : 297mm
View Box                        : 0 0 210 297
SVG Version                     : 1.1
ID                              : svg8
Version                         : 0.92.5 (2060ec1f9f, 2020-04-08)
Docname                         : drawing.svg
Metadata ID                     : metadata5
Work Format                     : image/svg+xml
Work Type                       : http://purl.org/dc/dcmitype/StillImage
Work Title                      : 

```

#### File in Text Editor

I opened the file in a text editor and noticed something unusual here, I am not too familiar with SVG files in general but know that is has a structure similar to that of html. There is a text section at the end of the file which looks like this:

```
<text
    xml:space="preserve"
    style="font-style:normal;font-weight:normal;font-size:0.00352781px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.26458332;"
    x="107.43014"
    y="132.08501"
    id="text3723"><tspan
     sodipodi:role="line"
     x="107.43014"
     y="132.08501"
     style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
     id="tspan3748">p </tspan><tspan
     sodipodi:role="line"
     x="107.43014"
     y="132.08942"
     style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
     id="tspan3754">i </tspan><tspan
     sodipodi:role="line"
     x="107.43014"
     y="132.09383"
     style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
     id="tspan3756">c </tspan><tspan
     sodipodi:role="line"
     x="107.43014"
     y="132.09824"
     style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
     id="tspan3758">o </tspan><tspan
     sodipodi:role="line"
     x="107.43014"
     y="132.10265"
     style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
     id="tspan3760">C </tspan><tspan
     sodipodi:role="line"
     x="107.43014"
     y="132.10706"
     style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
     id="tspan3762">T </tspan><tspan
     sodipodi:role="line"
     x="107.43014"
     y="132.11147"
     style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
     id="tspan3764">F { 3 n h 4 n </tspan><tspan
     sodipodi:role="line"
     x="107.43014"
     y="132.11588"
     style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
     id="tspan3752">c 3 d _ a a b 7 2 9 d d }</tspan>
</text>
```

If you look closely you'll notice that the flag is present and spread out within the *tspan* elements or tag.  

***picoCTF{3nh4nc3d_aab729dd}***
