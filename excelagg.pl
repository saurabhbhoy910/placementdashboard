import pandas as pd
import glob, os
 
os.chdir("/Users/saurabhbhoy/Downloads")
results = pd.DataFrame([])
 
for counter, file in enumerate(glob.glob("Placement_Detail*")):
    namedf = pd.read_csv(file, skiprows=0, usecols=[0,1,2,3])
    results = results.append(namedf)
 
results.to_csv('/Users/saurabhbhoy/Downloads/combinedfile.csv')
