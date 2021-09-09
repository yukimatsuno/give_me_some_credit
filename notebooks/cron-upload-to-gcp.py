import glob
import os
import pandas as pd
import shutil

df = pd.DataFrame(columns=[])
# get all csv file names in 'input_folder' folder
files = glob.glob(f"../raw_data/input_folder/*.csv") # a list of csv file names

# to avoid error when csv file is empty, return strings
# if file is not empty, concatinate csv files on df
for file in files:
    if os.stat(file).st_size == 0:
        print('File is empty')
    else:
        tmp = pd.read_csv(file)
        df = pd.concat([df, tmp])

#df
df.to_csv('../raw_data/sample_data.csv', header=True, index=True)

# For the newly retrieved csv files, the contents of these files will be merged into a single CSV file called `sample_data.csv`
# The contents of this CSV file will then be uploaded to a cloud SQL server running on Google cloud using the following steps in this link below, so that the data is accessible/readable by multiple data scientists in parallel: 
# https://cloud.google.com/sql/docs/mysql/quickstart

# After the upload to GCP SQL server is over, delete folder and re-make a empty folder
shutil.rmtree('../raw_data/input_folder')
os.mkdir('../raw_data/input_folder')