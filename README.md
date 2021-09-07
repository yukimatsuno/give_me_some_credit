# Part 1 - Data Ingestion

Files location: give_me_some_credit/notebooks/
Files name: 
* cron_job.ipynb
* cronjob.txt

Steps:
1. Open Terminal
2. Write crontab -e to create crontab
3. Write the schedule command * 2 * * * /usr/bin/python /path/to/file/cron_job.ipynb to run the python script every day at 2 am.
    (For Demo, the schedule command is '0 2 * * * /usr/bin/python /home/yuki/code/yukimatsuno/give_me_some_credit/notebooks/cron_job.ipynb' as written in 'cronjob.txt')
4. Exit edit mode

Python script ('cron_job.ipynb'):
1. Take csv files in '../raw_data/input_folder', data source folder, and create a dataframe
2. Add rows from the csv files on the current dataframe
3. Delete csv files in '../raw_data/input_folder', data source folder.
4. Save the dataframe in '../raw_data' as a 'sample_data.csv'

Database:
For the newly retrieved csv files, the contents of these files will be uploaded to GCP SQL server following steps in this link below,
so that the data is accessible/readable by multiple data scientists in parallel.
https://cloud.google.com/sql/docs/mysql/quickstart



# Part 2 - Understanding the Data

Link for presentation:
https://docs.google.com/presentation/d/1-GGzOW6ZuIzJ7VYZbPh5p0Q8gFSJQqsPzrBitE-rs6Y/edit?usp=sharing

Link for analysis notebook:
https://github.com/yukimatsuno/give_me_some_credit
    (folder: '../notebooks/basic visualization.ipynb')

