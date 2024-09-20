-- Step 1: Create the 'products' table
CREATE TABLE IF NOT EXISTS products (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2)
);


-- Step 2: Insert sample data into the 'products' table
INSERT INTO products (id, name, price) 
VALUES 
(1, 'Product A', 100.00),
(2, 'Product B', 200.00),
(3, 'Product C', 300.00),
(4, 'Product D', 400.00);

-- Step 3: Update the price of all products by 10%
UPDATE products
SET price = price * 1.10;

-- Step 4: Display the updated product names and prices
SELECT name, price 
FROM products;
