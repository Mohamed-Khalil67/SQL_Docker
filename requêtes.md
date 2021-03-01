Requêtes CLI MySQL : 

1 - Liste de Bureaux Trié par pays 

    - Answer :
    1 USA CA San Francisco
    2 USA MA Boston
    3 USA NY NYC
    4 France None Paris
    5 Japan Chiyoda-Ku Tokyo
    6 Australia None Sydney
    7 UK None London

2 - SELECT count(employeeNumber) FROM employees
    - Answer : 23


3 - SELECT COUNT(customerNumber) FROM payments;
+-----------------------+
| COUNT(customerNumber) |
+-----------------------+
|                   273 

4 - SELECT * FROM productlines WHERE productline LIKE '%Cars%';

    - | Classic Cars |
    - | Vintage Cars |

5 - SELECT * FROM payments WHERE paymentDate LIKE '%2004-10-28%';
+----------------+-------------+-------------+----------+
| customerNumber | checkNumber | paymentDate | amount   |
+----------------+-------------+-------------+----------+
|            286 | DR578578    | 2004-10-28  | 47411.33 |
+----------------+-------------+-------------+----------+

6 - SELECT * FROM payments WHERE amount > 100000;
+----------------+-------------+-------------+-----------+
| customerNumber | checkNumber | paymentDate | amount    |
+----------------+-------------+-------------+-----------+
|            124 | AE215433    | 2005-03-05  | 101244.59 |
|            124 | KI131716    | 2003-08-15  | 111654.40 |
|            141 | ID10962     | 2004-12-31  | 116208.40 |
|            141 | JE105477    | 2005-03-18  | 120166.58 |
|            148 | KM172879    | 2003-12-26  | 105743.00 |
+----------------+-------------+-------------+-----------+

7 - 

8 - SELECT count(productScale) FROM products WHERE productScale LIKE '%1:10%';
+---------------------+
| count(productScale) |
+---------------------+
|                   6 |

 - SELECT count(productScale) FROM products WHERE productScale LIKE '%1:12%';
+---------------------+
| count(productScale) |
+---------------------+
|                   9 |
+---------------------+

 - SELECT count(productScale) FROM products WHERE productScale LIKE '%1:18%';
+---------------------+
| count(productScale) |
+---------------------+
|                  42 |
+---------------------+

 - SELECT count(productScale) FROM products WHERE productScale LIKE '%1:24%';
+---------------------+
| count(productScale) |
+---------------------+
|                  27 |
+---------------------+
 - SELECT count(productScale) FROM products WHERE productScale LIKE '%1:32%';
+---------------------+
| count(productScale) |
+---------------------+
|                   8 |
+---------------------+
- SELECT count(productScale) FROM products WHERE productScale LIKE '%1:50%';
+---------------------+
| count(productScale) |
+---------------------+
|                   4 |
+---------------------+
- SELECT count(productScale) FROM products WHERE productScale LIKE '%1:700%';
+---------------------+
| count(productScale) |
+---------------------+
|                  10 |
+---------------------+
- SELECT count(productScale) FROM products WHERE productScale LIKE '%1:72%';
+---------------------+
| count(productScale) |
+---------------------+
|                   4 |
+---------------------+

9 - SELECT MIN(amount) FROM payments;
+-------------+
| MIN(amount) |
+-------------+
|      615.45 |
+-------------+

10 - SELECT AVG(amount) FROM payments;
+--------------+
| AVG(amount)  |
+--------------+
| 32431.645531 |
+--------------+

SELECT amount FROM payments WHERE amount > 2*32431.645531;
+-----------+
| amount    |
+-----------+
|  82261.22 |
| 101244.59 |
|  85410.87 |
|  83598.04 |
| 111654.40 |
| 116208.40 |
|  65071.26 |
| 120166.58 |
| 105743.00 |
|  85024.46 |
|  80375.24 |
|  85559.12 |
|  75020.13 |
+-----------+

11 - 

12 - SELECT distinct count(productName) FROM products; ( produits totale qui peuvent offrir )
+--------------------+
| count(productName) |
+--------------------+
|                110 |
+--------------------+

13 - SELECT count(customerName) FROM customers WHERE customerName LIKE '%Co';
+---------------------+
| count(customerName) |
+---------------------+
|                   7 |
+---------------------+

SELECT count(customerName) FROM customers WHERE customerName LIKE '%Co.';
+---------------------+
| count(customerName) |
+---------------------+
|                  26 |
+---------------------+

14 - SELECT CONCAT(firstName,' ',lastName) FROM employees WHERE jobTitle LIKE '%VP%' OR '%Manager%';
+--------------------------------+
| CONCAT(firstName,' ',lastName) |
+--------------------------------+
| Mary Patterson                 |
| Jeff Firrelli                  |
+--------------------------------+

15 -

16 - 

17 - 

18 - SELECT * FROM payments ORDER BY paymentdate ASC;

19 -