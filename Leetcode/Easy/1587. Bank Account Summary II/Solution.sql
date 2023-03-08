WITH accounts_balance as (
SELECT
    Usr.account
    ,SUM(Tr.amount) AS  balance
FROM Users Usr
INNER JOIN Transactions Tr
        ON Usr.account = Tr.account
GROUP BY  Usr.account
HAVING SUM(Tr.amount) > 10000
)
SELECT
    Usr.name
    ,accb.balance
FROM Users Usr
INNER JOIN accounts_balance accb
        ON Usr.account = accb.account
