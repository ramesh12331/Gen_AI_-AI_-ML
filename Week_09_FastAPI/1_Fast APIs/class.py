#install necessary packages
#how to create basic end points
# load data from json file
#how to fetch data from json file using end points

#find all customers , products , cities etc...

#end point to search customer by city

#endpoint for customers by category

#endpoint for customers of above given age

#find products below given price

#caluclate total sales


from fastapi import FastAPI
import json


app = FastAPI()


@app.get('/')
def home():
    return {'message':'welocme to my landing page....'}


@app.get('/about')
def about():
    return {'message':'heyy there is no about get lost'}


@app.get('/data')
def data():
    return {'message':'this is my data'} 


#loading json data

class GetData:

    def get_data(self):
        with open('data.json','r') as f:
            data = json.load(f)

        return data


@app.get('/cities')
def fetch_data():
    data = GetData()

    customers = data.get_data()

    return [ customer['city']  for customer in customers]



@app.get('/products')
def get_prod(product : str):

    data = GetData()

    customers = data.get_data()

    for customer in customers:
        if customer['product'] == product:
            return customer['customer_name']
    return {'message':'no product found'}


@app.get('/city')
def city_info(city : str):

    data = GetData()

    customers = data.get_data()

    for cust in customers:
        if cust['city'] == city:
            return cust

    return {'customer not find'}


@app.get('/major')
def major_cust(age : int):
    data = GetData()
    
    customers = data.get_data()

    result =[]

    for customer in customers:
        if customer['age'] >=age:
            result.append(customer)
    return result

    return {'message':'chota bacha'}
    