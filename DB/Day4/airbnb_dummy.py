import pymysql
import pymysql.cursors

# db connection
connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 's87962640',
    db = 'testdatabase',
    charset= 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

# 1 새로운 제품 추가: Python 스크립트를 사용하여 
# '.Products' 테이블에 새로운 제품을 추가하세요. 
# 예를 들어, "Python Book"이라는 이름의 제품을 29.99달러 가격으로 추가합니다.
def add_product() :
    cursor = connection.cursor()
    productName = 'Python Book'
    price = 29.99
    stockQuantity = 1
    sql = f'INSERT INTO products(productName, price, stockQuantity) VALUES("{productName}", {price}, {stockQuantity})'
    cursor.execute(sql)
    connection.commit()
    cursor.close()    

add_product()

# 2. 고객 목록 조회: 'Customers' 테이블에서 
# 모든 고객의 정보를 조회하는 Python 스크립트를 작성하세요.
def get_customers() :
    cursor = connection.cursor()

    sql = f"SELECT * FROM Customers"
    cursor.execute(sql)
    customers = cursor.fetchall()
    print(customers)
    cursor.close()

get_customers()

# 3. 제품 재고 업데이트: 제품이 주문될 때마다 
# 'Products' 테이블의 해당 제품의 재고를 감소시키는 Python 스크립트를 작성하세요.
def update_products() :
    cursor = connection.cursor()
    order_Quantity = 1
    
    sql = f"UPDATE products SET stockQuantity = stockQuantity - {order_Quantity} WHERE productName = 'Python Book' "

    cursor.execute(sql)
    connection.commit()
    cursor.close()

update_products()

# 4.고객별 총 주문 금액 계산: 'Orders' 테이블을 사용하여 
# 각 고객별로 총 주문 금액을 계산하는 Python 스크립트를 작성하세요.
def cal_total_order() :
    cursor = connection.cursor()
    sql = f"SELECT customerID, SUM(totalAmount) FROM Orders GROUP BY customerID"

    cursor.execute(sql)
    cursor.close()

cal_total_order()

# 5. 고객 이메일 업데이트: 고객의 이메일 주소를 업데이트하는 Python 스크립트를 작성하세요. 
# 고객 ID를 입력받고, 새로운 이메일 주소로 업데이트합니다.
def update_email() :
    cursor = connection.cursor()
    customerID = 'shtjddn0817'
    email = 'shtjddn0817@gmail.com'
    sql = f"UPDATE Customers SET customerID = {customerID}, email = {email}"

    cursor.execute(sql)
    connection.commit()

# 6. 주문 취소: 주문을 취소하는 Python 스크립트를 작성하세요. 
# 주문 ID를 입력받아 해당 주문을 'Orders' 테이블에서 삭제합니다.
def cancle_orders() :
    cursor = connection.cursor()
    orderID = 'shtjddn0817'
    sql = f"DELETE FROM Orders WHERE orderID = {orderID}"

    cursor.execute(sql)
    connection.commit()
    cursor.close()

cancle_orders()

# 7. 특정 제품 검색: 제품 이름을 기반으로 'Products' 테이블에서
# 제품을 검색하는 Python 스크립트를 작성하세요.
def search_products() :
    cursor = connection.cursor()
    productName = 'MAC'
    sql = f"SEARCH * FROM Products WHERE productName = {productName}"

    cursor.execute(sql)
    product_list = cursor.fetchall()
    print(product_list)
    cursor.close()

search_products()

# 8. 특정 고객의 모든 주문 조회: 고객 ID를 기반으로 
# 그 고객의 모든 주문을 조회하는 Python 스크립트를 작성하세요.
def search_customer() :
    cursor = connection.cursor()
    customerID = 3
    sql = f'SELECT * FROM Customers JOIN Orders ON Customers.customerId = Orders.customerID
    WHERE customerID = {customerID}'
    
    cursor.execute(sql)
    customer_order_list = cursor.fetchall()
    print(customer_order_list)

search_customer()

# 9. 가장 많이 주문한 고객 찾기: 'Orders' 테이블을 사용하여 
# 가장 많은 주문을 한 고객을 찾는 Python 스크립트를 작성하세요.
def get_many_order() :
    cursor = connection.cursor()
    sql = f"SELECT * FROM Orders JOIN Customers ON Orders.customerID = Customers.customerID
    ORDER BY totalAmount DESC LIMIT 1 "

    cursor.execute(sql)
    many_order_list = cursor.fetchall()
    cursor.close()

get_many_order()

