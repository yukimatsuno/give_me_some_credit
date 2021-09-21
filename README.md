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
    (For Demo, the schedule command is `0 2 * * * /usr/bin/python /home/yuki/code/yukimatsuno/give_me_some_credit/notebooks/cron-upload-to-gcp.py` as written in `cronjob.txt`)
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
7. Exploring correlations with heatmap  
![image](https://user-images.githubusercontent.com/79320522/132685393-5f215ce4-1ccc-4e5f-925a-a201d22c54cf.png)

8. Visualize data  
`Yes`: Person experienced 90 days past due delinquency or worse  
`No`: Person did not experience 90 days past due delinquency or worse
![image](https://user-images.githubusercontent.com/79320522/132704318-28202d22-3ed0-41e1-8e5d-203052268958.png)
![image](https://user-images.githubusercontent.com/79320522/132704402-422e24cf-3221-45e4-ad46-c32d5458b9b0.png)
![image](https://user-images.githubusercontent.com/79320522/132704467-8a7c5bf3-402e-4180-b7f4-7231edffed67.png)

9. Check balanced/imbalanced of `SeriousDlqin2yrs`, the outcome variable
![image](https://user-images.githubusercontent.com/79320522/132685693-bb4e0f3c-0215-460e-8242-dbb5d0bb6d5b.png)
10. Analysis of each feature:
    - MonthlyIncome: Fill `NaN` with median, replace outlier with median because there are big outliers. Mean is affected by outliers and tend to higher than median.
    - NumberOfDependents: Fill `NaN` with median, replace outlier to reduce noise.
    - Age: Replace age `below 22` with `22` because there is one `0` input outlier and except this outlier, the youngest age is `22`.
    - RevolvingUtilizationOfUnsecuredLines: Replace number `above 1` with `1` because generally input should be between `0` and `1`.
    - NumberOfTime30to59DaysPastDueNotWorse: Replace outliers. `98` and `96`, with median. The other data points are between `0` and `13`.
    - DebtRatio: Replace number `above 1` with `1` to group `above 1` as people who have more debt than income. Most data points are under `1`. 
    - NumberOfOpenCreditLinesAndLoans: Replace number `above 20` with `20` to reduce noise though there is no limit for this feature. 
    - NumberOfTimes90DaysLate: Replace `98` and `96` with median because Data points are between `0` and `17`, and `98` and `96` are outliers.
    - NumberRealEstateLoansOrLines: Replace outlier with median to reduce noise. Mostly data points are between `0` and `2`.
    - NumberOfTime60to89DaysPastDueNotWorse: Replace `98` and `96` with median because most data points are between `0` and `11`, and `98` and `96` are outliers.
11. Visualize all features without outliers  
![image](https://user-images.githubusercontent.com/79320522/132684522-c57ee333-a4b5-4ad0-90b4-7bd64099e06a.png)  
![image](https://user-images.githubusercontent.com/79320522/132684565-67f88ded-2122-4529-8fdb-16f613ea61dd.png)

12. Rebalance the outcome variable to find the relation between `SeriousDlqin2yrs` the outcome variable and each feature.
13. Visualize rebalanced data![image](https://user-images.githubusercontent.com/79320522/132684950-66c7992e-ada6-451c-8aa9-a8242ededbdb.png)  
![image](https://user-images.githubusercontent.com/79320522/132685018-fcf1b518-af99-4b37-91cc-bcf0be472ea8.png)
14. Explore corelations of rebalanced data with heatmap  
![image](https://user-images.githubusercontent.com/79320522/132687367-3da79a4f-1eaa-4846-aa8a-fd82fa4a7fca.png)


* Link to presentation:
[presentation](https://docs.google.com/presentation/d/1-GGzOW6ZuIzJ7VYZbPh5p0Q8gFSJQqsPzrBitE-rs6Y/edit?usp=sharing)
