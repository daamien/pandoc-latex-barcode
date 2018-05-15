pandoc-latex-barcode
===============================================================================

[![Build Status](https://travis-ci.org/daamien/pandoc-latex-barcode.svg?branch=master)](https://travis-ci.org/daamien/pandoc-latex-barcode)
[![Docker Automated Build](https://img.shields.io/docker/automated/daamien/pandoc-latex-barcode.svg)](https://hub.docker.com/r/daamien/pandoc-latex-barcode/)
[![PyPI version](https://badge.fury.io/py/pandoc-latex-barcode.svg)](https://badge.fury.io/py/pandoc-latex-barcode)

A pandoc filter to insert barcodes and QR codes in a latex/pdf document

The filter is written in Python with [panflute](http://scorreia.com/software/panflute/)
which I recommend if you want to create your own pandoc filters.


Install
-------------------------------------------------------------------------------

```
sudo pip install pandoc-latex-barcode
```

or

```
docker run -d daamien/pandoc-latex-barcode
```

Quick Start
-------------------------------------------------------------------------------

### 1- Add a barcode tag to your markdown file

To generate a generic barcode:

```
<div class="barcode">Hello World !</div>
```

To generate an ISBN barcode:

```
<div class="barcode isbn">978-3-86541-114</div>
```

To generate a QR code:

```
<div class="qrcode">http://www.pandoc.org</div>
```


### 2- Enjoy !

```
pandoc --filter pandoc-latex-barcode \
       --latex-engine xelatex \
       ./pandoc_latex_barcode.sample.md \
       -o ./pandoc_latex_barcode.sample.pdf
```

Note : The xelatex engine is mandatory because of pstricks.


Configuration
-------------------------------------------------------------------------------



There's also few parameters you can setup in the document front matter :

```yaml
barcode: {
  barcode_width: '50mm',
  barcode_height: '30mm',
  qrcode_width: '25mm',
  qrcode_height: '25mm' ,
  isbn: '123-4-56789-111',
}

```

- **barcode_width** and **barcode_height** defines the size of the barcode.
  _Default_ : 50mmx30mm

- **qrcode_width** and **qrcode_height** defines the size of the QR code.
  _Default_ : 25mmx25mm

- **isbn** : overides the value inside the ``<div>``
  __Default__ : ``None``

For more details, please refer to the _pst-barcode_ documentation :

http://texdoc.net/texmf-dist/doc/generic/pst-barcode/pst-barcode-doc.pdf

Example
-------------------------------------------------------------------------------

See [pandoc_latex_barcode.sample.md](pandoc_latex_barcode.sample.md)

and [pandoc_latex_barcode.sample.pdf](pandoc_latex_barcode.sample.pdf)

Contributing & Getting Help
-------------------------------------------------------------------------------

If you have any difficulties with this software, please file an issue here :

https://github.com/daamien/pandoc-latex-barcode/issues

License
-------------------------------------------------------------------------------

This software is available under the BSD 3-Clause Licence.

see [LICENSE](LICENSE)
