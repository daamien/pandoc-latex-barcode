FROM python:3

COPY . /tmp

WORKDIR /tmp 

# install latex packages
RUN apt-get update -y \
  && apt-get install -y --no-install-recommends \
    texlive-latex-base \
    texlive-xetex latex-xcolor \
    texlive-math-extra \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-bibtex-extra \
    fontconfig \
    pandoc

RUN pip install pandoc-latex-barcode

RUN pandoc --filter ./pandoc_latex_barcode.py --template ./pandoc_latex_barcode.template.tex --latex-engine xelatex ./pandoc_latex_barcode.sample.md -o ./pandoc_latex_barcode.sample.pdf
