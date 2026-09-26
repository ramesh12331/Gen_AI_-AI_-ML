import pandas as pd


df = pd.read_csv("sales_data.csv")

# print(df)
# result = df.loc[df['unit_price']>30000,['order_id', 'city', 'product', 'unit_price']]
# result = df[df['unit_price'] >= 30000][
#     ['order_id', 'city', 'product', 'unit_price']
# ]

result = df['unit_price'] >= 30000
result = df[df['unit_price'] >= 30000]

result = df[(df['city'] == 'Hyderabad') & (df['customer_type'] == 'Premium')]
result = df[(df['city'] == 'Hyderabad') & (df['customer_type'] == 'Premium')].head().count()

result = df.sort_values(by='unit_price', ascending=False)
res=result[['order_id', 'city', 'unit_price']].head()
print(res)

df['Total_Price'] = df['quantity'] * df['unit_price']

# print(df['Total_Price'])
print(df)

df['discount_amount'] = (
    df['Total_Price'] * df['discount'] / 100
)

print(df[['order_id', 'Total_Price', 'discount', 'discount_amount']])

df['total_price_after_discount'] = (
    df['Total_Price'] - df['discount_amount']
)

# print(df[
#     [
#         'order_id',
#         'quantity',
#         'unit_price',
#         'Total_Price',
#         'discount',
#         'discount_amount',
#         'total_price_after_discount'
#     ]
# ])

print(df)


top_10_orders = df.sort_values(
    by='total_price_after_discount',
    ascending=False
)[
    ['order_id', 'city', 'product', 'quantity', 'total_price_after_discount']
].head(10)

print(top_10_orders)

city_sales = (
    df.groupby('city')['total_price_after_discount']
      .sum().sort_values(ascending=False)
)

city_sales = (
    df.groupby(['city','category','product'])['total_price_after_discount']
      .sum().sort_values(ascending=False)
)

print(city_sales)

