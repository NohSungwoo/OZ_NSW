-- (1) **`customers`** 테이블에 새 고객을 추가하세요.
CREATE TABLE customers(
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name CHAR(20),
    customer_age INT,
    customer_memo VARCHAR(255)
);
INSERT customers(customer_name, customer_age, customer_memo)
VALUES ("노성우", 30, "개발자");

-- (2) **`products`** 테이블에 새 제품을 추가하세요.
CREATE TABLE products(
product_id INT PRIMARY KEY AUTO_INCREMENT,
product_name CHAR(30),
product_price INT,
product_memo VARCHAR(255)
);
INSERT products(product_name, product_price, product_memo)
VALUES("MAC", 30000000, "pro");

-- (3) **`employees`** 테이블에 새 직원을 추가하세요.
CREATE TABLE employees(
employee_id INT PRIMARY KEY AUTO_INCREMENT,
employee_name CHAR(30),
employee_salary INT,
employee_memo VARCHAR(255)
);
INSERT employees(employee_name, employee_salary, employee_memo)
VALUES ("노성우", 100000000000, "특급");

-- (4) **`offices`** 테이블에 새 사무실을 추가하세요.
CREATE TABLE offices(
office_id INT PRIMARY KEY AUTO_INCREMENT,
office_name CHAR(30),
office_foundation CHAR(30)
);

INSERT offices(office_name, officefoundation)
VALUES ("오늘의 책", "2021-08-17");

-- (5) **`orders`** 테이블에 새 주문을 추가하세요.
CREATE TABLE orders (
order_id INT PRIMARY KEY AUTO_INCREMENT,
order_kind CHAR(30),
order_name CHAR(30)
);

INSERT orders (order_kind, order_name)
VALUES("빵", "초코소라 케이크");

-- (6) **`orderdetails`** 테이블에 주문 상세 정보를 추가하세요.
CREATE TABLE orderdetails (
orderdetail_id INT PRIMARY KEY AUTO_INCREMENT,
orderdetail_count INT,
orderdetail_price INT
);
INSERT orderdetails(orderdetail_count, orderdetail_price)
VALUES(3개, 20000);
-- (7) **`payments`** 테이블에 지불 정보를 추가하세요.
CREATE TABLE payments(
	payment_id INT PRIMARY KEY AUTO_INCREMENT,
    payment_amount INT,
    payment_date CHAR(30)
);
INSERT payments(payment_amount, payment_date)
VALUES(100000, 2024-01-01);

-- (8) **`productlines`** 테이블에 제품 라인을 추가하세요.
CREATE TABLE productionlines(
productionline_id INT PRIMARY KEY AUTO_INCREMENT,
productionline_name CHAR(30),
productionline_kind VARCHAR(255)
) ;
INSERT productionlines(productionline_name, productionline_kind)
VALUES("A", "금속");

-- (9) **`customers`** 테이블에 다른 지역의 고객을 추가하세요.
ALTER TABLE customers 
ADD address CHAR(30);

INSERT customers(customer_name, customer_age, customer_memo, address)
VALUES("김선우", 30, "백수", "수원");

-- (10) **`products`** 테이블에 다른 카테고리의 제품을 추가하세요.
ALTER TABLE products 
ADD category CHAR(30);

INSERT products(product_name, product_price, product_memo, category)
VALUES("iphone", 1000000, 'pro', 'phone');

-- (1) **`customers`** 테이블에서 모든 고객 정보를 조회하세요.
SELECT * FROM customers;
-- (2) **`products`** 테이블에서 모든 제품 목록을 조회하세요.
SELECT * FROM proudcts;
-- (3) **`employees`** 테이블에서 모든 직원의 이름과 직급을 조회하세요.
SELECT employee_name, employee_position FROM employees;
-- (4) **`offices`** 테이블에서 모든 사무실의 위치를 조회하세요.
SELECT offices_address FROM offices; 
-- (5) **`orders`** 테이블에서 최근 10개의 주문을 조회하세요.
SELECT * FROM orders LIMIT 10;
-- (6) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
SELECT * FROM orderdetalis WHERE orderdetails_name = '케이크';
-- (7) **`payments`** 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
SELECT * FROM payments WHERE payments_name = '노성우';
-- (8) **`productlines`** 테이블에서 각 제품 라인의 설명을 조회하세요.
SELECT productlines_memo FROM productlines;
-- (9) **`customers`** 테이블에서 특정 지역의 고객을 조회하세요.
SELECT * FROM customers WHERE address = '수원';
-- (10) **`products`** 테이블에서 특정 가격 범위의 제품을 조회하세요.
SELECT * FROM products WHERE products_price >= 1000;

-- (1) **`customers`** 테이블에서 특정 고객의 주소를 갱신하세요.
UPDATE customers
SET customer_address = "수원"
WHERE customer_name = "노성우";
-- (2) **`products`** 테이블에서 특정 제품의 가격을 갱신하세요.
UPDATE products
SET products_price = 500000
WHERE products_name = "애플워치";
-- (3) **`employees`** 테이블에서 특정 직원의 직급을 갱신하세요.
UPDATE employees
SET employee_position = "과장"
WHERE employees_name = "김선우";
-- (4) **`offices`** 테이블에서 특정 사무실의 전화번호를 갱신하세요.
UPDATE offices 
SET office_tel = "010-1234-5666"
WHERE office_name = "노성우";
-- (5) **`orders`** 테이블에서 특정 주문의 상태를 갱신하세요.
UPDATE orders 
SET quanity = 3
WHERE product_name = "hotel";
-- (6) **`orderdetails`** 테이블에서 특정 주문 상세의 수량을 갱신하세요.
UPDATE orderdetails
SET orderdetail_count = 4
WHERE orderdetail_name = "pizza";
-- (7) **`payments`** 테이블에서 특정 지불의 금액을 갱신하세요.
UPDATE payments 
SET payment_amount = 50000
WHERE payment_date = "2022-12-12";
-- (8) **`productlines`** 테이블에서 특정 제품 라인의 설명을 갱신하세요.
UPDATE productlines 
SET productline_memo = "새 제품"
WHERE productline_name = "A";
-- (9) **`customers`** 테이블에서 특정 고객의 이메일을 갱신하세요.
UPDATE customers 
SET customer_email = "shtjddn@gmail.com"
WHERE customer_name = "노성우";

-- (1) **`customers`** 테이블에서 특정 고객을 삭제하세요.
DELETE FROM customers
WHERE customer_name = "노성우";
-- (2) **`products`** 테이블에서 특정 제품을 삭제하세요.
DELETE FROM products
WHERE product_name = "맥북";
-- (3) **`employees`** 테이블에서 특정 직원을 삭제하세요.
DELETE FROM employees
WHERE employee_name = "김선우";
-- (4) **`offices`** 테이블에서 특정 사무실을 삭제하세요.
DELETE FROM offices
WHERE office_name = "노성우";
-- (5) **`orders`** 테이블에서 특정 주문을 삭제하세요.
DELETE FROM orders
WHERE quantity > 5;
-- (6) **`orderdetails`** 테이블에서 특정 주문 상세를 삭제하세요.
DELETE FROM orderdetails 
WHERE orderdetial_count = 2;
-- (7) **`payments`** 테이블에서 특정 지불 내역을 삭제하세요.
DELETE FROM payments
WHERE payment_date = "2023-12-20";
-- (8) **`productlines`** 테이블에서 특정 제품 라인을 삭제하세요.
DELETE FROM productlines
WHERE productline_name = "A";
-- (9) **`customers`** 테이블에서 특정 지역의 모든 고객을 삭제하세요.
DELETE FROM customers
WHERE customer_address = "수원";
-- (10) **`products`** 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
DELETE FROM products
WHERE product_category = "음식";