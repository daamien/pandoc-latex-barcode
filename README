pandoc-latex-barcode
===============================================================================

A pandoc filter to insert barcodes and QR codes in a latex/pdf document


Install
-------------------------------------------------------------------------------

```
sudo pip install pandoc-latex-barcode
```

How-to
-------------------------------------------------------------------------------

### Create a specific pandoc template

First you need to the following packages to the latex template :

```latex
\usepackage{pstricks}
\usepackage{pst-barcode}
```
For your convenience, here's a complete template based on pandoc default latex
template :

[pandoc-latex-barcode.template.tex](pandoc-latex-barcode.template.tex)


### Add a barcode tag to your markdown file

```
<div class="barcode isbn">978-3-86541-114</div>
```

### Compile

```
pandoc --filter pandoc-latex-barcode \
       --template ./pandoc_latex_barcode.template.tex \
       --latex-engine xelatex \
       ./pandoc_latex_barcode.sample.md \ 
       -o ./pandoc_latex_barcode.sample.pdf
```

Note : The xelatex engine is mandatory because of pstricks.


Configuration
-------------------------------------------------------------------------------

There's a few parameters you can setup in the document front matter :

```yaml
barcode: {                                                                      
  barcode_width: '150mm',                                                       
  barcode_height: '30mm',                                                       
  qrcode_width: '75mm',                                                         
  qrcode_height: '25mm' ,                                                       
  isbn: '123-4-56789-111',                                                      
}                                                                               
                                                                                
```


Example
-------------------------------------------------------------------------------

See [pandoc-latex-barcode.sample.md](pandoc-latex-barcode.sample.md)

and [pandoc-latex-barcode.sample.pdf](pandoc-latex-barcode.sample.pdf)

Contributing & Getting Help
-------------------------------------------------------------------------------

If you have any difficulties with this software, please file an issue here :

https://github.com/daamien/pandoc-latex-barcode/issues

License
-------------------------------------------------------------------------------

This software is available under the BSD 3-Clause Licence.

see [LICENSE](LICENSE)
