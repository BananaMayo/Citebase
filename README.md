# Citebase

![GHA workflow badge](https://github.com/BananaMayo/Citebase/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/BananaMayo/Citebase/branch/main/graph/badge.svg?token=B2EWB0O9WQ)](https://codecov.io/gh/BananaMayo/Citebase)

This project is licensed under the terms of the MIT license.

## Product Backlog
[Product Backlog](https://docs.google.com/spreadsheets/d/1Vgykm0RkudteIoG1uGLySVpMnRyPw8JiHMKXIQHLDTE/edit?usp=sharing)

## Asennus
1. Riippuvuuksien asennus komennolla:
```
$ poetry install
```
2. Siirry virtuaalitilaan komennolla:
```
$ poetry shell
```
## Toiminnot komentorivillä
### Ohjelman suorittaminen
Ohjelman pystyy suorittamaan komennolla:

* Jos olet juurihakemistossa:
```
$ python3 src/index.py
```
* Jos olet src:n sisällä
```
$ python3 index.py
```

### Linkki CI-palveluun: 
#### [CI-palvelu](https://github.com/BananaMayo/Citebase/actions)

### **Definition of done**

Task on ohjelmoitu, testaus automatisoitu, dokumentoitu backlogille ja integroitu muuhun ohjelmistoon. Task on valmis, kun sen testikattavuus on 70%. Taskit on yksikkötestattu ja koodi ei sisällä Pylint-virheitä.


