import sqlite3,sys,os
d=sys.argv[1]; os.makedirs(d,exist_ok=True)
for f in ("shop.sqlite","empty.sqlite","docs.sqlite"):
    p=f"{d}/{f}"
    if os.path.exists(p): os.remove(p)
c=sqlite3.connect(f"{d}/shop.sqlite")
c.executescript("""
CREATE TABLE customers(customer_id INTEGER PRIMARY KEY, full_name TEXT, region TEXT);
CREATE TABLE products(product_id INTEGER PRIMARY KEY, product_name TEXT, list_price REAL);
CREATE TABLE orders(order_id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(customer_id), order_date TEXT);
CREATE TABLE order_items(item_id INTEGER PRIMARY KEY, order_id INTEGER REFERENCES orders(order_id), product_id INTEGER, qty INTEGER, unit_price REAL);
INSERT INTO customers VALUES (1,'Kim','Seoul'),(2,'Lee','Busan'),(3,'Park','Seoul');
INSERT INTO products VALUES (1,'USB Sushi',20.0),(2,'Mug',8.0);
INSERT INTO orders VALUES (1,1,'2026-01-05'),(2,2,'2026-02-07');
INSERT INTO order_items VALUES (1,1,1,2,20.0),(2,1,2,1,8.0),(3,2,1,1,19.0);
"""); c.commit()
sqlite3.connect(f"{d}/empty.sqlite").commit()
c=sqlite3.connect(f"{d}/docs.sqlite")
long=" ".join(f"제{i}조 임차인은 계약 만료 {i}일 전까지 임대인에게 서면으로 갱신 의사를 통지하여야 한다." for i in range(1,201))
c.execute("CREATE TABLE documents(doc_id INTEGER PRIMARY KEY, title TEXT, body TEXT)")
c.execute("INSERT INTO documents VALUES (1,'임대차 계약 표준 약관',?)",(long,))
c.execute("INSERT INTO documents VALUES (2,'개인정보 처리 방침',?)",(long.replace('임차인','정보주체'),))
c.commit(); print("doc body chars:",len(long))
