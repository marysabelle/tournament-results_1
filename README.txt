Full Stack Web Developer Nanodegree
Tournament Planner
Project 2


What is this?
------------

This is the code for the study of the "Full Stack Web Developer Nanodegree" on Udacity.
This project requires defining the database schema (SQL table definitions) for a Swiss tournament system and writing a Python module that uses the PostgreSQL database to keep track of athletes and matches in a game tournament.

The game tournament uses the Swiss system for pairing up athletes in each round: athletes are not eliminated, and each athlete is paired with another athlete with the same number of wins, or as close as possible.


In this project:
---------------

Database scheme was desinged at first to fulfill Swiss tournament system; PostgreSQL database was used to implement this scheme;
Python module was wrote to interact with the database and rank the athletes in the tournament.



Dependencies
------------

 - Python 2.7.9
 - PostgreSQL
 - psycopg2
 - Ubuntu 14.10 on x86_64
 - psql 9.4.1 


File content
------------

1) tournament.sql: The schema file is located in here; this file contains SQL code that sets up the tournament database for a single tournament.


2) tournament.py: The API to the PostgreSQL instance; includes functions for removing, adding, and editing athletes in the database, and finding Swiss-style parings. 

3) tournament_test.py: Contains unit tests that will test the functions written in tournament.py. Tests can be run from the command line, using the command python tournament_test.py.

4) README.txt: File that includes detail steps required to succesfully run the application.



How to Run:
----------

Import the database scheme into PostgreSQL database. Type the following commands on you terminal:

psql  -> create database tournament;  -> \c tournament  -> \i tournament.sql  -> \q

Make sure that the directory of your terminal is the same with the directory your codes under. 
Run the tests of this project by typing: -> python tournament_test.py

And you should be able to see the following output once all tests have passed:

vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
1. Old matches can be deleted.
2. Athletes records can be deleted.
3. After deleting, countAthletes() returns zero.
4. After registering an athlete, countAthletes() returns 1.
5. Athletes can be registered and deleted.
6. Newly registered athletes appear in the standings with no matches.
7. After a match, athletes have updated standings.
8. After one match, athletes with one win are paired.
Success!  All tests pass!
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$