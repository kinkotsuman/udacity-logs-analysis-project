# Extract Data From NewsData.sql
##### (Answering to 3 questions from [Udacity])
#
*news.py* file returns list of data extracted PostgreSQL named "news".
The list of data is answers of 3 questions provided by [Udacity] Full Stack Web Developer Nanodegree Course (Assignment: **Log Analysis Project** in Curriculum 4). They are...

  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

### Three Functions in News.py

  - get_titles()
  - get_authors()
  --- **View: topfive** - removes unnecessary string from the column labeled 'path' from the table 'log' so that the column can be matched to the column labaled 'slug' in the table 'articles'.
  - get_errors()
  --- **View: step1** - counts all rows grouped by *time::date*.
  --- **View: step2** - counts all *404 NOT FOUND* from column labeled 'status' in the table 'log' grouped by *time::Date*.

### Set-up Instructions
1. Download and install [VirtualBox].
2. Download and install [Vagrant].
3. Open **Terminal** and type: ```cd your_directory_to_vagrant_folder```
4. Type ```vagrant up``` to start virtual machine.
5. Create the news database in PostgreSQL.
-- From the command line, launch the psql console by typing: ```psql```
-- Check to see if a news database already exists by listing all databases with the command: ```\l```
-- If a news database already exists, drop it with the command: ```DROP DATABASE news;```
-- Create the news database with the command: ```CREATE DATABASE news;```
-- exit the console by typing: ```\q```
6. Download the schema and data for the news database:
-- Click here to download [newsdata.sql].
7. Unzip the downloaded file. You should now have an sql script called *newsdata.sql*.
8. From the command line, navigate to the directory containing *newsdata.sql*.
9. Import the schema and data in *newsdata.sql* to the news database by typing: ```psql -d news -f newsdata.sql```.
10. Connect to the *news* database by typing: ```psql -d news``` and check the schema and data.
-- (press *control + D* to exit database)

### Run News.py
1. Open **terminal**.
2. Make sure to start [Vagrant] and ```cd /to_the_folder_that_contains_news.py_file/```.
3. Run *News.py* by tying: ```python news.py```.

[Udacity]: <https://udacity.com>
[Vagrant]: <https://www.vagrantup.com/downloads.html>
[VirtualBox]: <https://www.virtualbox.org/wiki/Downloads>
[newsdata.sql]: <https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip>
