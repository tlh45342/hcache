# hcache

This will be my tool to manage/cache hstorical data.

## INSTALLATION

```bash
git clone https://github.com/tlh45342/hcache.git
```

To make sure you have all the python modules installed.

```bash
pip install -r requirements.txt
```

## STRUCTURE

    ├── CHANGES                     Change logs
    ├── requirements.txt            3rd libraries
    ├── hcache.py                   main module
    ├── init.py                     stub to initialize database
    └── process-listings.py         Used to import data from NASDAQ file (optional)

## How to enumerate all stocks

How to list all the stocks is a question that often comes up.  If you ftp://ftp.nasdaqtrader.com/Symboldirectory/ you will see a number of files.
One of which is "nasdaqlisted.txt".  Place this in the directory with this and run "process-listings.py" to import the data.  As a bonus there is a field to indicate
if a  symbol is an ETF or not.


## NOTE:

requests-cache might be interarsting to look into.  hcache is semi based on the concept that ziptrader could process "bundles" of data. One of the bundles apparently was a CSV collection where you could place data as a packet of CSVs for ziptrader to pull from.

## CHANGES

     - 09/12/2021 - v0.0.0 Initial code a lot of stubs.

## LICENSE

hcache is licensed under the Apache License, Version 2.0. See LICENSE for the full license text.
