ASSIGNMENT No 8
Problem statement: Write a PL/SQL block of code for Database Trigger for different applications

SQL> create table library1(BOOK_ISBN numeric,Title varchar(30),Publisher_Name varchar(30),Price numeric,Date_of_Publication date,Book_Copy numeric);
Table created.
SQL> insert into library1 values(1,'DSA','Amar',500,'02-jan-2015',35);
1 row created.
SQL> ed
Wrote file afiedt.buf
67
q
  1* insert into library1 values(2,'DAA','Saurabh',600,'03-jan-2017',37)
SQL> /
1 row created.
SQL> ed
Wrote file afiedt.buf
70
q
  1* insert into library1 values(3,'DBMS','Kunal',700,'05-mar-2017',37)
SQL> /

1 row created.
SQL> ed
Wrote file afiedt.buf
69
q
  1* insert into library1 values(4,'Java','Dipak',800,'07-mar-2016',45)
SQL> /
1 row created.
SQL> ed
Wrote file afiedt.buf
69
q
  1* insert into library1 values(5,'ADS','Akash',900,'10-may-2016',55)
SQL> 
1 row created.
SQL> ed
Wrote file afiedt.buf
68

  1* create table lib_audit1(BOOK_ISBN numeric,Title varchar(30),Publisher_Name varchar(30),Price numeric,Date_of_Publication date,Book_Copy numeric)
SQL> 
Table created.
SQL> select * from library1;

 BOOK_ISBN TITLE              PUBLISHER_NAME
---------- ------------------------------ ------------------------------
     PRICE DATE_OF_PUBLICATIO  BOOK_COPY
---------- ------------------ ----------
     1 DSA                  Amar
       500 02-JAN-15              35

     2 DAA                  Saurabh
       600 03-JAN-17              37

     3 DBMS               Kunal
       700 05-MAR-17              37


 BOOK_ISBN TITLE              PUBLISHER_NAME
---------- ------------------------------ ------------------------------
     PRICE DATE_OF_PUBLICATIO  BOOK_COPY
---------- ------------------ ----------
     4 Java               Dipak
       800 07-MAR-16              45

     5 ADS                  Akash
       900 10-MAY-16              55

     5 ADS                  Akash
       900 10-MAY-16              55
6 rows selected.
SQL> select * from lib_audit1;
no rows selected
SQL> alter table lib_audit1 add(operation varchar(20));
Table altered.
SQL> ed
Wrote file afiedt.buf
52
q
  1  create or replace trigger t3 after delete or update or insert on library1 for each row
  2  declare
  3  operation varchar(20);
  4  begin
  5  if updating then
  6  operation:='update';
  7  end if;
  8  if deleting then
  9  operation:='delete';
 10  end if;
 11  if inserting then
 12  operation:='insert';
 13  end if;
 14  if operation='update' or operation='delete' then
 15  insert into lib_audit1 values(:old.BOOK_ISBN,:old.TITLE,:old.PUBLISHER_NAME,:old.PRICE,:old.DATE_OF_PUBLICATION,:old.BOOK_COPY,operation);
 16  end if;
 17  if operation='insert' then
 18  insert into lib_audit1 values(:new.BOOK_ISBN,:new.TITLE,:new.PUBLISHER_NAME,:new.PRICE,:new.DATE_OF_PUBLICATION,:new.BOOK_COPY,operation);
 19  end if;
 20* end;
SQL> /
Trigger created.
SQL> update library1 set BOOK_COPY=65 where BOOK_ISBN=102;

0 rows updated.

SQL> select * from library1;

 BOOK_ISBN TITLE              PUBLISHER_NAME
---------- ------------------------------ ------------------------------
     PRICE DATE_OF_PUBLICATIO  BOOK_COPY
---------- ------------------ ----------
     1 DSA                  Amar
       500 02-JAN-15              35

     2 DAA                  Saurabh
       600 03-JAN-17              37

     3 DBMS               Kunal
       700 05-MAR-17              37

 BOOK_ISBN TITLE              PUBLISHER_NAME
---------- ------------------------------ ------------------------------
     PRICE DATE_OF_PUBLICATIO  BOOK_COPY
---------- ------------------ ----------
     4 Java               Dipak
       800 07-MAR-16              45
     5 ADS                  Akash
       900 10-MAY-16              55
     5 ADS                  Akash
       900 10-MAY-16              55
6 rows selected.

SQL> update library1 set BOOK_COPY=65 where BOOK_ISBN=2;
1 row updated.
SQL> select * from lib_audit1;

 BOOK_ISBN TITLE              PUBLISHER_NAME
---------- ------------------------------ ------------------------------
     PRICE DATE_OF_PUBLICATIO  BOOK_COPY OPERATION
---------- ------------------ ---------- --------------------
     2 DAA                  Saurabh
       600 03-JAN-17              37 update

