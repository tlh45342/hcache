# hcache

This will be my tool manage/cache hstorical data

# NOTE:

## INSTALLATION

```bash
git clone https://github.com/tlh45342/hcache.git
```

To make sure you have all the python modules installed.

```bash
pip install -r requirements.txt
```

## SIDEBAR: Notes for creating a service for Linux based distributions

I am putting my notes here now -

## STRUCTURE

    ├── CHANGES                     Change logs
    ├── requirements.txt            3rd libraries
    ├── hcache.py                   main file
    ├── process-listings.py         Used to import data from NASDAQ file (optional)

## How to enumerate all stocks

How to list all the stocks is a question that often comes up.  If you ftp://ftp.nasdaqtrader.com/Symboldirectory/ you will see a number of files.
One of which is "nasdaqlisted.txt".  Place this in the directory with this and run "process-listings.py" to import the data.  As a bonus there is a field to indicate
if a  symbol is an ETF or not.

## CHANGES

     - 09/12/2021 - v0.0.0 Initial code a lot of stubs.

## LICENSE

pinetrace is licensed under the Apache License, Version 2.0. See LICENSE for the full license text.
