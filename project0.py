"""project:0 - Topic: Car dealership management using python & mongoDB """
import datetime
import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = client['dealership']
cars = db['cars']
customers = db['customers']
purchases = db['purchases']
def add_car(make,model,colour,year,price):
    """function to get details of car"""
    document={
      'Make': make,
      'Model': model,
      'Colour': colour,
      'Year': year,
      'Price': price,
      'Dated': datetime.datetime.now()
     }
    return db.cars.insert_one(document)
def add_customer(first_name,last_name,phone,location):
    """user defined function to store details of the customer"""
    document={
     'First_Name': first_name,
     'Last_Name': last_name,
     'Phone_Number': phone,
     'Location': location,
     'Dated': datetime.datetime.now()
     }
    return db.customers.insert_one(document)
def add_purchase(car_id,customer_id,mode):
    """user defined function to store details of the purchase"""
    document={
      'Car_ID': car_id,
      'Customer_ID': customer_id,
      'Mode_of_Payment': mode,
      'Dated': datetime.datetime.now()
     }
    #assert db.purchases.find({"Customer_ID": document['Customer_ID'] }) == False , "The customer_id entered already exists..!"
    if db.purchases.find_one({"Customer_ID": document['Customer_ID'] }):
        # When the entered customerID already exists, it will display error message as  a document inside it.
        return db.purchases.insert_one({"error":"Customer_ID entered already exists","_id":0})
    return db.purchases.insert_one(document)
def exit():
    print("You have exited..")
def add():
    a = str(input("Enter the type of details to add (out of car,customer,purchase)  :"))
    if a == "customer" or a == "Customer":
      print("          -------------Enter your details----------------")
      first_name = str(input("Enter your first name                                          : "))
      last_name = str(input("Enter your last name                                           : "))
      phone = int(input("Enter your phone number                                         : "))
      location = str(input("Enter the place you live                                         : "))
      add_customer(first_name,last_name,phone,location)
      print("Your details have been added successfully..!")
    elif a == "car" or a == "Car":
      print("         ----------Enter car details to insert-----------")
      make = str(input("Enter your car make                                              : "))
      model = str(input("Enter your car model                                             : "))
      colour = str(input("Enter your car colour                                            : "))
      year = int(input("Enter your car year                                              : "))
      price = int(input("Enter your car price                                             : "))
      add_car(make,model,colour,year,price) 
      print("Successfully added car details..") 

def update():
    print("Enter what you want to update out of these: ")
    print("Press 1 for updating your car details     :")
    print("Press 2 for updating your details         :")
    a = int(input("        ------------Enter your choice -------------"))
    if a!=1 and a!=2:
        print("Please enter a valid choice..")
    elif a==1:
        b = str(input("Enter which parameter of car details you want to update:"))   
        if b == "Make" or b == "make":
            b_1 = str(input("Enter the make to replace                                 : "))
            b_2 = str(input("Enter your make choice                                    : "))
            db.cars.update_one({"Make":b_1},{"$set":{"Make":b_2}})
            print("Successfully updated your car make..!")
        elif b=="Model" or b=="model":
            b_1 = str(input("Enter the model to replace                                : "))
            b_2 = str(input("Enter your model choice                                   : "))   
            db.cars.update_one({"Model":b_1},{"$set":{"Model":b_2}})
            print("Successfully updated your car model..!")
        elif b=="Colour" or b=="colour":
            b_1 = str(input("Enter the colour to replace                               : "))
            b_2 = str(input("Enter your colour choice                                  : "))   
            db.cars.update_one({"Colour":b_1},{"$set":{"Colour":b_2}})
            print("Successfully updated your car colour..!")   
        elif b=="year" or b=="Year":
            b_1 = int(input("Enter the year to replace                                 : "))
            b_2 = int(input("Enter your year choice                                    : "))   
            db.cars.update_one({"Year":b_1},{"$set":{"Year":b_2}})
            print("Successfully updated your car year..!")
        elif b=="Price" or b=="price":
            b_1 = int(input("Enter the price to replace                                : "))
            b_2 = int(input("Enter your price choice                                   : "))   
            db.cars.update_one({"Price":b_1},{"$set":{"Price":b_2}})
            print("Successfully updated your car price..!")
    elif a == 2:
        c = str(input("Enter the type of customer details to modify:"))
        if c == "firstname" or c == "Firstname":
            c_1 = str(input("Enter the first name to be replaced          : "))
            c_2 = str(input("Enter the first name of your choice          : "))
            db.customers.update_one({"First_Name":c_1},{"$set":{"First_Name":c_2}})
            print("Your First name update was successful!")
        elif c == "secondname" or c == "Secondname":
            c_1 = str(input("Enter the second name to be replaced         : "))
            c_2 = str(input("Enter the second name of your choice         : "))
            db.customers.update_one({"Second_Name":c_1},{"$set":{"Second_Name":c_2}})
            print("Your Second name update was successful!")
        elif c == "phone" or c == "Phone":
            c_1 = int(input("Enter the phone number to be replaced        : "))
            c_2 = int(input("Enter the phone number of your choice        : "))
            db.customers.update_one({"Phone_Number":c_1},{"$set":{"Phone_Number":c_2}})
            print("Your Phone number update successful!")   
        elif c == "Location" or c == "location":
            c_1 = str(input("Enter the location to be replaced            : "))
            c_2 = str(input("Enter the location of your choice            : "))
            db.customers.update_one({"Location":c_1},{"$set":{"Location":c_2}})
            print("Your Location update successful!")        
def delete():
    a=str(input("Enter the type of document to delete      : "))
    if a == "car" or a == "Car":
        b = str(input("Enter the type to remove the document     : "))
        if b == "make" or b == "Make":
            b_1=str(input("Enter the make to remove the document     : "))
            db.cars.delete_one({"Make":b_1})
            print("Successfully removed the car document based on the input make given..")
    elif a == "customer" or a == "Customer":
        b = str(input("Enter the parameter type to remove the document: "))
        if b == "First name" or b == "first name":
            b_1=str(input("Enter the first name to remove the document    : "))  
            db.customers.delete_one({"First_Name":b_1})
            print("Successfully removed the customer details..")      
def search():
    a = str(input("Enter the type of document to search      : "))
    if a == "car" or a == "Car":
        b = str(input("Enter the parameter of car to search for  : "))
        if b == "make" or b == "Make":
            count=0
            b_1 = str(input("Enter the make of the car to search for   : "))
            curs = db.cars.find({"Make" :{"$regex" :b_1,"$options":"$i"}},{"_id":0,"Make":1,"Model":1,"Colour":1,"Year":1,"Price":1})
            for record in curs:
                count+=1
                print(record)
        print("The no.of matching records are: ",count)        
        print("Successfully searched your car details...") 



print("Enter your choice out of these            :")
print("Press '1'- for adding a document          :")
print("Press '2'- for updating a document        :")
print("Press '3'- for deleting a document        :")
print("Press '4'- to search for a document       :")
print("Press '5'- to exit                        :")
num = int(input("Enter the number of your choice           :"))
operations=[add,update,delete,search,exit]
if (num-1) not in range(0,len(operations)):
    print("Enter valid option please.. ")
if (num-1) in range(0,len(operations)):
    output = operations[num-1]()



'''
add_car('Ford','Fiesta','Brown',2013,600000)
add_customer('Tony','Stark',9840123668,'Thiruvanmiyur')
add_purchase(1,3124,'Cheque')  


add_car('Toyota','Innova','Blue',2017,1200000)
add_customer('Ram','Kumar',9840345223,'Besant Nagar')
add_purchase(2,4024,'Cash')

add_car('Hyundai','Venue','White',2015,800000)
add_customer('Ben','Robert',9760345223,'Adayar')
add_purchase(3,2536,'Credit')

add_car('Volkswagen','Polo','White',2017,900000)
add_customer('Antony','Ajay',9789745223,'Pallavakkam')
add_purchase(4,2102,'Cash')

add_car('Kia','Seltos','Blue',2020,1100000)
add_customer('Abdul','Hameed',9789751423,'Mylapore')
add_purchase(5,3333,'Cash')

add_car('Benz','S-Class','Black',2018,3400000)
add_customer('Mohammed','Hashim',9745753412,'Hyderabad')
add_purchase(6,3333,'Cheque') 
'''