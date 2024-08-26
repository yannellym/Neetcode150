-- Table: Products

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | product_id    | int     |
-- | new_price     | int     |
-- | change_date   | date    |
-- +---------------+---------+
-- (product_id, change_date) is the primary key (combination of columns with unique values) of this table.
-- Each row of this table indicates that the price of some product was changed to a new price at some date.
 

-- Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Products table:
-- +------------+-----------+-------------+
-- | product_id | new_price | change_date |
-- +------------+-----------+-------------+
-- | 1          | 20        | 2019-08-14  |
-- | 2          | 50        | 2019-08-14  |
-- | 1          | 30        | 2019-08-15  |
-- | 1          | 35        | 2019-08-16  |
-- | 2          | 65        | 2019-08-17  |
-- | 3          | 20        | 2019-08-18  |
-- +------------+-----------+-------------+
-- Output: 
-- +------------+-------+
-- | product_id | price |
-- +------------+-------+
-- | 2          | 50    |
-- | 1          | 35    |
-- | 3          | 10    |
-- +------------+-------+

# Write your MySQL query statement below
SELECT 
    product_id, 
    # SELECT THE MOST RECENT Price. In this case, closest date due to DES order
    FIRST_VALUE(new_price) 
    # over designates a window for what we will be looking at
    OVER(
        PARTITION BY product_id 
        # orders by date and the latest will be the first date in this order
        ORDER BY change_date DESC
        ) AS price
    # this orders all records partitioned by the product id and ordered by the change_data
    # it returns only the latest date and product id for each record 
FROM Products
# this is filtering to where the records are only before or on '2019-08-16'
WHERE change_date <= '2019-08-16'
# since the top will only filter records before or on '2019-08-16', we will be missing
# those records that didnt have a change prior to '2019-08-16'
# we need to tie it with another table so we also get ALL the records
UNION
# we select all distinct product, set the price as 10
SELECT DISTINCT product_id, 10 AS price
FROM Products
# when the product is not founf in the table that has all products before or on '2019-08-16'
WHERE product_id NOT IN 
    (
        SELECT product_id
        FROM Products 
        WHERE change_date <= '2019-08-16'
    )

-- SELECT 
--     product_id, 
--     FIRST_VALUE(new_price) 
--     OVER(
--         PARTITION BY product_id 
--         ORDER BY change_date DESC
--         ) AS price
-- FROM Products
-- WHERE change_date <= '2019-08-16'

-- What This Does:
-- It selects the most recent price (new_price) for each product_id as of 2019-08-16.
-- The FIRST_VALUE(new_price) function returns the price for the most recent change_date before or on 2019-08-16.
-- What It Misses:
-- Products Without Any Price Changes: If a product has no price changes recorded before or on 2019-08-16, this query will not return that product at all. This means such products won't appear in the result set.


-- SELECT 
--     product_id, 
--     FIRST_VALUE(new_price) 
--     OVER(
--         PARTITION BY product_id 
--         ORDER BY change_date DESC
--         ) AS price
-- FROM Products
-- WHERE change_date <= '2019-08-16'

-- UNION

-- SELECT DISTINCT product_id, 10 AS price
-- FROM Products
-- WHERE product_id NOT IN 
--     (
--         SELECT product_id
--         FROM Products 
--         WHERE change_date <= '2019-08-16'
--     )
-- What This Adds:

-- The UNION combines the results of two queries:
-- First Part: Returns the most recent price for each product that has a recorded price change before or on 2019-08-16.
-- Second Part: Ensures that products without any recorded price changes up to 2019-08-16 are included in the final result with a default price of 10.
-- Why This is Important:

-- Complete Product List: It ensures that every product in the Products table is represented in the final result set. For products with no price changes by 2019-08-16, it assigns a price of 10.
-- Correctness: Without the UNION, products with no prior price changes would be omitted, which would violate the requirement to list all products with their correct price as of 2019-08-16.
