# Part 1 - Data Ingestion

## File location
`give_me_some_credit/notebooks/`

## Part 1
There are two files related to managing and uploading data. 

### Proposed flow:
- Cron job runs everyday on a Virtual Machine (VM) at 2AM and checks for new files in folder `../raw_data/input_folder`. The incoming files are dumped into this folder.
- The code for crontab file is written in `cronjob.txt` file in `notebooks` folder. 
- Cronjob python script does the following:
1. Take csv files in `../raw_data/input_folder`, data source folder, and create a dataframe
2. Add rows from the csv files on the current dataframe
3. Save the dataframe in `../raw_data/input_folder` as `sample_data.csv`
4. Uploads contents from `sample_data.csv` to GCP SQL server
5. Delete folder `../raw_data/input_folder`, data source folder (please note that this also deletes the `sample_data.csv` file created everytime the cron job runs)
6. Create folder `../raw_data/input_folder` to prepare the environment for next cron job run.

### Steps to run cron job:
1. Open Terminal
2. Write crontab -e to create crontab
3. Write the schedule command mentioned in `notebooks/cronjob.txt` file and copy paste it. It runs the python script every day at 2 am.
    (For Demo, the schedule command is `0 2 * * * /usr/bin/python /home/yuki/code/yukimatsuno/give_me_some_credit/notebooks/cron_job.ipynb` as written in `cronjob.txt`)
4. Exit edit mode


# Part 2 - Understanding the Data

### How to run the script
The part about visualizing data is written in `/give_me_some_credit/notebooks/basic visualization.ipynb`. Data scientists can run it on their local machines by running `jupyter notebook` command on terminal.

### Contents of the script
1. Import csv files 
2. Initial exploration/ Data dictionary: Explanation about data
3. Rename columns with a symbol, `-` to avoid conflict with code
4. Drop unnecessary columns: Drop `Unnamed: 0` because it's unnecessary (has no information)
5. Data inspection: Check columns name, data shape, non-null count and data type.
6. Duplicates check
7. Exploring corelations with heatmap
8. Check balanced/imbalanced of `SeriousDlqin2yrs` the outcome variable
9. Analysis of each feature:
    - MonthlyIncome: Fill `NaN` with median, replace outlier with median
    - NumberOfDependents: Fill `NaN` with median, replace outlier with median
    - Age: Replace age `below 22` with `22`
    - RevolvingUtilizationOfUnsecuredLines: Replace number `above 1` with `1`
    - NumberOfTime30to59DaysPastDueNotWorse: Replace `98` and `96` with median
    - DebtRatio: Replace number `above 1` with `1`
    - NumberOfOpenCreditLinesAndLoans: Replace number `above 20` with `20`
    - NumberOfTimes90DaysLate: Replace `98` and `96` with median
    - NumberRealEstateLoansOrLines: Replace outlier with median
    - NumberOfTime60to89DaysPastDueNotWorse: Replace `98` and `96 with median
10. Visualize all features without outliers
11. Rebalance the outcome variable
12. Visualize rebalanced data
13. Explore corelations of rebalanced data with heatmap

* Link to presentation:
[presentation](https://docs.google.com/presentation/d/1-GGzOW6ZuIzJ7VYZbPh5p0Q8gFSJQqsPzrBitE-rs6Y/edit?usp=sharing)
