# Project: Log-Analysis

### Project Overview

> You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.


> In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

### Getting Started.

#### PreRequisites:
  * [Python](https://www.python.org/)
  * [VirtualBox](https://www.virtualbox.org/)
  * [Vagrant](https://www.vagrantup.com/)
  

#### Prepare Software & Data:
  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here. Unzip this file after downloading it. The file inside is called newsdata.sql.
  5. Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from
  [Here](https://github.com/sagarchoudhary96/Log-Analysis)
  
#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository:
  
  ```
    $ vagrant up
  ```
  2. Log into virtual machine:
  
  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant. Play around with dir and ls to see the structure.
  
  ```
  Note: If vagrant ssh does not work, use the following instructions to login using Putty.
  https://github.com/Varying-Vagrant-Vagrants/VVV/wiki/Connect-to-Your-Vagrant-Virtual-Machine-with-PuTTY
  ```
  
#### Setting up the database:

  1. Load the data in local database using the command:
  
  ```
    psql -d news -f newsdata.sql
  ```
  
  The database comprises of three tables:
  * The log table includes one entry for each time a user has accessed the site.
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  
  2. Use `psql -d news` to connect to database.
 
#### Create Views
  1. articles_view:
  ```
    create view articles_view as select title, author, count(*) as Hits from articles as a, log as l where l.path like concat('%', a.slug) group by a.title, a.author order by Hits desc;
  ```
  | Column  | Type    |
  | :-------| :-------|
  | title   | text    |
  | author  | text    |
  | Hits    | Integer |
  
  2. error_log_view:
  ```
    create view error_log_view as select date(time) as Date, round(100.0 * sum(case log.status when '200 OK' then 0 else 1 end)/count(log.status),3) as Percent_Error from log group by Date order by Percent_Error desc;
  ```
  | Column        | Type    |
  | :-------      | :-------|
  | date          | date    |
  | Percent_Error | float   |
  
#### Run queries via Python file:
  1. cd /forum/ -> run the python file now.
  ```
    $ python logs.py
  ```
  
#### FAQ's: [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/b2ff9cba-210e-463e-9321-2605f65491a9)
