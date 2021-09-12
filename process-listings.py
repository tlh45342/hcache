import hcache as hc

# assumes file "nasdaqlisted.txt" has been FTP from NASDAQ

def import_listings():
  fname = r"nasdaqlisted.txt"
  with open(fname) as f:
      lines = f.readlines()
      count = 0
      for line in lines[1:-1]:  #discard first and last line
        count += 1
        elements = line.split("|")  #we want 0,1,6(ETF)
        hc.insert_into_listings(elements[0],elements[1],elements[6])
  print("Count:", count, "listings.")
  
# ------------------------------

#hc.create_listings()

# expectation: around 4984 entries.  This will take a few minutes to import

# select count(*) from listings where etf="N"; ~= 4555
# select symbol from listings where symbol="AAPL";

import_listings()