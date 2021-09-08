# Part 1 - Data Ingestion

Files location: `give_me_some_credit/notebooks/`  
File_name: `cron_job.ipynb`: Does the following:
1. Take csv files in `../data/input_folder`, data source folder, and create a dataframe
2. Add rows from the csv files on the current dataframe
3. Delete csv files in `../data/input_folder`, data source folder.
4. Save the dataframe in `../data` as a `sample_data.csv`

`cronjob.txt`: 

Steps:
1. Open Terminal
2. Write crontab -e to create crontab
3. Write the schedule command * 2 * * * /usr/bin/python /path/to/file/cron_job.ipynb to run the python script every day at 2 am.
    (For Demo, the schedule command is `0 2 * * * /usr/bin/python /home/yuki/code/yukimatsuno/give_me_some_credit/notebooks/cron_job.ipynb` as written in `cronjob.txt`)
4. Exit edit mode

Python script (`cron_job.ipynb`):

Database:
For the newly retrieved csv files, the contents of these files will be uploaded to GCP SQL server following steps in this link below,
so that the data is accessible/readable by multiple data scientists in parallel.
https://cloud.google.com/sql/docs/mysql/quickstart



# Part 2 - Understanding the Data

* Analysis notebook: `/give_me_some_credit/notebooks/basic visualization.ipynb`  
Contents
1. Import csv files 
2. Initial exploration/ Data dictionary: Explanation about data
3. Rename columns with a simbol, `-` to avoid conflict with code
4. Drop unnecessary columns: Drop `Unnamed: 0`
5. Data inspection: Check columns name, data shape, non-null count and data type.
6. Duplicates check
7. Exploring corelations with heatmap
8. Check balanced/imbalanced of ,SeriousDlqin2yrs, the outcome variable
9. Analysis of each features
    - MonthlyIncome: Fill NA with median, replace outlier with median
    - NumberOfDependents: Fill NA with median, replace outlier with median
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
13. Exploring corelations of rebalanced data with heatmap

* Link for presentation:
[presentation](https://docs.google.com/presentation/d/1-GGzOW6ZuIzJ7VYZbPh5p0Q8gFSJQqsPzrBitE-rs6Y/edit?usp=sharing)



