-- Creating sample bank accounts
CREATE TABLE accounts (id numeric, balance numeric);

-- Inserting data into bank accounts
INSERT INTO accounts (id, balance)
VALUES
   	(1,10000),
	(2,20000);

-- Viewing data
SELECT * FROM accounts;

-- Creating a stored procedure to do bank updates
CREATE OR REPLACE PROCEDURE transfers(
   sender int,
   receiver int, 
   amount dec
)
language plpgsql    
as $$
begin
    -- subtracting the amount from the sender's account 
    update accounts 
    set balance = balance - amount
    where id = sender;

    -- adding the amount to the receiver's account
    update accounts 
    set balance = balance + amount
    where id = receiver;

    commit;
end;$$

-- Inputing transaction data
CALL transfers(1,2,5000);

-- Viewing balance after transaction
SELECT * FROM accounts;