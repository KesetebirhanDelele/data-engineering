-- Creating a temporary table and inserting data using Recursion
WITH table1 (x, y)
AS (VALUES (1,'2'),(3,'4'))
SELECT * FROM table1;

-- Creating a table and inserting data using VIEW
CREATE OR REPLACE VIEW table2 (x,y)
AS (VALUES(1,2),(3,4));
SELECT * FROM table2;
