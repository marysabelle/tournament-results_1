-- Table definitions for the tournament project.
--
-- This is the file to create ATHLETES table and to populate it with 6 records.
--



CREATE TABLE Athletes(
AthleteID serial primary key,
Name varchar(60)
);

CREATE TABLE Matches(
AthleteID serial references Athletes,
Result varchar(4)
);

