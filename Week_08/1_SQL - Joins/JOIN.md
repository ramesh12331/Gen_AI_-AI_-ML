Absolutely 👍 Since you are using **DBeaver + PostgreSQL**, let's add data specifically designed to make **INNER JOIN, LEFT JOIN, and RIGHT JOIN** easy to understand.

The important idea is to create **matching and non-matching records**.

### 🎯 Data we want

```text
CUSTOMERS                         ORDERS
---------                         ------
101 Rahul       ←──────────────→ 5001
102 Sneha       ←──────────────→ 5002
103 Arjun       ←──────────────→ 5003
104 Priya       ←──────────────→ 5004
105 Kiran       ←──────────────→ 5005
106 Anjali      ←──────────────→ 5006
107 Ravi        ←──────────────→ 5007
108 Pooja                         No Order
109 Vikram                        No Order
110 Deepika                       No Order

                                  5008 → customer_id 999
                                         No Customer
```

This is **perfect for JOIN practice**:

* `INNER JOIN` → only matching records
* `LEFT JOIN` → all customers, including customers without orders
* `RIGHT JOIN` → all orders, including an order without a customer

---

# 1️⃣ Add More Customers

You already have customers `101–105`.

Add these:

```sql
INSERT INTO customers
(customer_id, customer_name, gender, city, phone, join_date)
VALUES
(106, 'Anjali Verma', 'Female', 'Delhi', 9876543215, '2024-05-10'),
(107, 'Ravi Kumar', 'Male', 'Hyderabad', 9876543216, '2024-06-15'),
(108, 'Pooja Reddy', 'Female', 'Chennai', 9876543217, '2024-07-20'),
(109, 'Vikram Singh', 'Male', 'Pune', 9876543218, '2024-08-05'),
(110, 'Deepika Rao', 'Female', 'Mumbai', 9876543219, '2024-09-12');
```

Check:

```sql
SELECT *
FROM customers
ORDER BY customer_id;
```

You should now have:

```text
customer_id | customer_name
------------+----------------
101         | Rahul Sharma
102         | Sneha Reddy
103         | Arjun Kumar
104         | Priya Singh
105         | Kiran Rao
106         | Anjali Verma
107         | Ravi Kumar
108         | Pooja Reddy
109         | Vikram Singh
110         | Deepika Rao
```

---

# 2️⃣ Add More Orders

You already have orders `5001–5005`.

Add these:

```sql
INSERT INTO orders
(order_id, customer_id, store_id, order_date, payment_method)
VALUES
(5006, 106, 2, '2025-01-15', 'UPI'),
(5007, 107, 3, '2025-01-16', 'Cash'),
(5008, 999, 4, '2025-01-17', 'Card');
```

### ⚠️ Why `customer_id = 999`?

There is **no customer 999** in the customers table.

That's intentional.

```text
customers
106 → Anjali
107 → Ravi

orders
5006 → customer 106 ✅
5007 → customer 107 ✅
5008 → customer 999 ❌
```

This gives us an **unmatched order**, which is very useful for understanding `RIGHT JOIN`.

---

# 3️⃣ Check Orders

```sql
SELECT *
FROM orders
ORDER BY order_id;
```

You should have:

```text
order_id | customer_id | store_id | order_date | payment_method
---------+-------------+----------+------------+---------------
5001     | 101         | 1        | 2025-01-10 | UPI
5002     | 102         | 2        | 2025-01-11 | Card
5003     | 103         | 3        | 2025-01-12 | Cash
5004     | 104         | 4        | 2025-01-13 | UPI
5005     | 105         | 1        | 2025-01-14 | Card
5006     | 106         | 2        | 2025-01-15 | UPI
5007     | 107         | 3        | 2025-01-16 | Cash
5008     | 999         | 4        | 2025-01-17 | Card
```

---

# 🔵 4️⃣ INNER JOIN

## Definition

`INNER JOIN` returns **only records that have a match in both tables**.

```sql
SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.payment_method
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id;
```

### Dry Run

Think:

```text
CUSTOMERS              ORDERS
   101   ←────────────→ 101   ✅
   102   ←────────────→ 102   ✅
   103   ←────────────→ 103   ✅
   104   ←────────────→ 104   ✅
   105   ←────────────→ 105   ✅
   106   ←────────────→ 106   ✅
   107   ←────────────→ 107   ✅
   108                    ❌
   109                    ❌
   110                    ❌

                         999   ❌
```

Result:

```text
customer_id | customer_name | order_id
------------+---------------+---------
101         | Rahul Sharma  | 5001
102         | Sneha Reddy   | 5002
103         | Arjun Kumar   | 5003
104         | Priya Singh   | 5004
105         | Kiran Rao     | 5005
106         | Anjali Verma  | 5006
107         | Ravi Kumar    | 5007
```

Notice:

```text
108, 109, 110 → removed
999            → removed
```

### 🧠 Memory Trick

```text
INNER JOIN
    ↓
ONLY MATCHING DATA
```

---

# 🟢 5️⃣ LEFT JOIN

Now we want:

> **Show ALL customers, whether they have an order or not.**

```sql
SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.payment_method
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
ORDER BY c.customer_id;
```

### Dry Run

```text
Customer 101 → Order 5001 ✅
Customer 102 → Order 5002 ✅
Customer 103 → Order 5003 ✅
Customer 104 → Order 5004 ✅
Customer 105 → Order 5005 ✅
Customer 106 → Order 5006 ✅
Customer 107 → Order 5007 ✅
Customer 108 → No order
Customer 109 → No order
Customer 110 → No order
```

Result:

```text
customer_id | customer_name | order_id
------------+---------------+---------
101         | Rahul Sharma  | 5001
102         | Sneha Reddy   | 5002
103         | Arjun Kumar   | 5003
104         | Priya Singh   | 5004
105         | Kiran Rao     | 5005
106         | Anjali Verma  | 5006
107         | Ravi Kumar    | 5007
108         | Pooja Reddy   | NULL
109         | Vikram Singh  | NULL
110         | Deepika Rao   | NULL
```

### Why `NULL`?

Because:

```text
108 → No matching order
109 → No matching order
110 → No matching order
```

But `LEFT JOIN` says:

> Keep every row from the **left table**.

So the customer remains, and order columns become `NULL`.

### 🧠 Memory Trick

```text
LEFT JOIN
    ↓
Keep EVERYTHING from LEFT table
```

---

# 🔴 6️⃣ RIGHT JOIN

Now we want:

> **Show ALL orders, even if the customer doesn't exist.**

```sql
SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.payment_method
FROM customers c
RIGHT JOIN orders o
    ON c.customer_id = o.customer_id
ORDER BY o.order_id;
```

### Dry Run

```text
Order 5001 → Customer 101 ✅
Order 5002 → Customer 102 ✅
Order 5003 → Customer 103 ✅
Order 5004 → Customer 104 ✅
Order 5005 → Customer 105 ✅
Order 5006 → Customer 106 ✅
Order 5007 → Customer 107 ✅
Order 5008 → Customer 999 ❌
```

Result:

```text
customer_id | customer_name | order_id
------------+---------------+---------
101         | Rahul Sharma  | 5001
102         | Sneha Reddy   | 5002
103         | Arjun Kumar   | 5003
104         | Priya Singh   | 5004
105         | Kiran Rao     | 5005
106         | Anjali Verma  | 5006
107         | Ravi Kumar    | 5007
NULL        | NULL          | 5008
```

Why?

```text
Order 5008
customer_id = 999

Customer 999 does NOT exist.
```

But `RIGHT JOIN` says:

> Keep everything from the **right table** (`orders`).

Therefore:

```text
customer_id → NULL
customer_name → NULL
order_id → 5008
```

---

# ⭐ 7️⃣ The Most Important Difference

| JOIN         | Keeps                |
| ------------ | -------------------- |
| `INNER JOIN` | Matching rows only   |
| `LEFT JOIN`  | All LEFT table rows  |
| `RIGHT JOIN` | All RIGHT table rows |

### Easy Diagram

```text
INNER JOIN

Customers ∩ Orders
       ↓
   MATCHING ONLY
```

```text
LEFT JOIN

Customers  +  matching Orders
     ↓
ALL CUSTOMERS
```

```text
RIGHT JOIN

matching Customers  +  Orders
                         ↓
                    ALL ORDERS
```

---

# 🎯 8️⃣ Find Customers Who Never Ordered

This is an excellent interview question.

```sql
SELECT
    c.customer_id,
    c.customer_name
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

Result:

```text
customer_id | customer_name
------------+--------------
108         | Pooja Reddy
109         | Vikram Singh
110         | Deepika Rao
```

### Logic

```text
LEFT JOIN
    ↓
Keep all customers

WHERE order_id IS NULL
    ↓
Keep only customers without orders
```

---

# 🎯 9️⃣ Find Orders Without Customers

Another important interview question:

```sql
SELECT
    o.order_id,
    o.customer_id,
    o.payment_method
FROM orders o
LEFT JOIN customers c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
```

Result:

```text
order_id | customer_id | payment_method
---------+-------------+---------------
5008     | 999         | Card
```

---

# 🧠 10️⃣ Best Data for Learning JOINs

Your data now intentionally contains:

```text
                 CUSTOMERS
              ┌─────────────┐
              │ 101         │────── 5001
              │ 102         │────── 5002
              │ 103         │────── 5003
              │ 104         │────── 5004
              │ 105         │────── 5005
              │ 106         │────── 5006
              │ 107         │────── 5007
              │ 108         │
              │ 109         │
              │ 110         │
              └─────────────┘

                    ORDERS

              5008 → customer 999
                         ↑
                    No customer
```

This gives you **both types of unmatched data**, which is exactly what you need to understand JOINs properly.

### ⭐ Practice in this order

```text
1. INNER JOIN
       ↓
2. LEFT JOIN
       ↓
3. RIGHT JOIN
       ↓
4. Find customers without orders
       ↓
5. Find orders without customers
       ↓
6. LEFT JOIN + WHERE
       ↓
7. Multiple-table JOIN
```

**One important PostgreSQL note:** if you later add a foreign key such as `orders.customer_id REFERENCES customers(customer_id)`, PostgreSQL will reject `customer_id = 999`. For JOIN practice, keep these tables without that foreign-key constraint, or use a separate practice dataset.
