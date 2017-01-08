#!/usr/bin/env python

"""
pandoc-latex-barcode
A pandoc filter to insert barcodes and QR codes in a latex/pdf document
https://github.com/daamien/pandoc-latex-barcode
"""

import panflute as pf

BARCODE="barcode"
QRCODE="qrcode"


def latex(s):
    return pf.RawBlock(s,"latex")

def barcode(doc, data, opt,size):
    barcode=doc.barcode_begin+size+"\\psbarcode{"+data+"}"+opt+doc.barcode_end
    return [latex(barcode)]

def prepare(doc):
    doc.barcode_barcode_width=doc.get_metadata('barcode.barcode_width', default='50mm') 
    doc.barcode_barcode_height=doc.get_metadata('barcode.barcode_height',default="30mm")
    doc.barcode_qrcode_width=doc.get_metadata('barcode.qrcode_width', default="25mm")
    doc.barcode_qrcode_height=doc.get_metadata('barcode.qrcode_height', default="25mm")
    doc.barcode_isbn=doc.get_metadata('isbn', default=None)
    doc.barcode_begin="\\begin{pspicture}"
    doc.barcode_end="\\end{pspicture}"

def action(elem, doc):
    if isinstance(elem, pf.Div) and doc.format == 'latex':
        if BARCODE in elem.classes:
            opt="{includetext}"
            size="("+doc.barcode_barcode_width+","+doc.barcode_barcode_height+")"
            if  "isbn" in elem.classes:
                opt+="{isbn}"
                if doc.barcode_isbn is not None:
                   data=doc.barcode_isbn
                else:
                   data=pf.stringify(elem)
            else:
                   opt+="{code128}"
                   data=pf.stringify(elem)
            return barcode(doc,data,opt,size)

        if QRCODE in elem.classes:
            opt="{eclevel=H width=1.0 height=1.0}"
            opt+="{qrcode}"
            size="("+doc.barcode_qrcode_width+","+doc.barcode_qrcode_height+")"
            data=pf.stringify(elem)
            return barcode(doc,data,opt,size)

def finalize(doc):
    pass


def main(doc=None):
    return pf.run_filter(action,
                         prepare=prepare,
                         finalize=finalize,
                         doc=doc) 


if __name__ == '__main__':
    main()

