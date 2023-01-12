# imports
import os
import csv
import sys
from stout import  translate_reverse
import time

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

start = time.time()
def my_model(iupac_list):
    return {iupac:translate_reverse(iupac) for iupac in iupac_list}

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    iupac_list = [r[0] for r in reader]

# run model
smiles = my_model(iupac_list)

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["iupacs_names", "smiles"]) # header
    for i, o in smiles.items():
        writer.writerow([i, o])