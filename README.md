# smartphone_store_flask

## objective

This project is a simple web application that show the list of smartphones and their details. The application is built using Flask framework and tinydb database.

## requirements

- [ ] The app should have a home page that displays a list of smartphone.
- [ ] The app should have a form that allows users to add new smartphone to the list.
- [ ] The app should show a smartphone by specifying the smartphone type in the URL.
- [ ] The app should show a smartphone by specifying the smartphone name in the URL.
- [ ] The app should show a smartphone by specifying the smartphone price in the URL.

## database

list of smartphone:

- `Smanusng`
- `Apple`
- `Huawei`
- `Xiaomi`
- `Oppo`
- `Vivo`
- `Nokia`
- `Redmi`

properties of smartphone:

- `name` - the name of the smartphone.
- `company` - the company that made the smartphone.
- `color` - the color of the smartphone.
- `RAM` - the RAM of the smartphone.
- `memory` - the memory of the smartphone.
- `price` - the price of the smartphone.
- `img_url` - the image url of the smartphone.

## SmartphoneDB - database class

for this project we will use a database class to store our data. The database class will have the following methods:

- [ ] `__init__` - the constructor method that will initialize the database class.
- [ ] `brands` - this method will return a list of smartphone brands.
- [ ] `add_smartphone` - this method will add a new smartphone to the database.
- [ ] `get_smartphone_by_brand` - this method will return a list of smartphone by specifying the smartphone brand.
- [ ] `get_smartphone_by_name` - this method will return a list of smartphone by specifying the smartphone name.
- [ ] `get_smartphone_by_price` - this method will return a list of smartphone by specifying the smartphone price.
- [ ] `delete_smartphone` - this method will delete a smartphone from the database.


## Endpoints

- [ ] GET `/smartphone` - this endpoint will return a list of smartphone.
- [ ] GET `/smartphone/brands` - this endpoint will return a list of smartphone brands.
- [ ] GET `/smartphone/brand/<brand>` - this endpoint will return a list of smartphone by specifying the smartphone brand.
- [ ] GET `/smartphone/name/<name>` - this endpoint will return a list of smartphone by specifying the smartphone name.
- [ ] GET `/smartphone/price/<price>` - this endpoint will return a list of smartphone by specifying the smartphone price.
- [ ] POST `/smartphone/add` - this endpoint will add a new smartphone to the database.
- [ ] POST `/smartphone/delete/<doc_id>` - this endpoint will delete a smartphone from the database.