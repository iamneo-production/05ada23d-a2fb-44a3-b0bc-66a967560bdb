import pymongo
client = pymongo.MongoClient("mongodb+srv://yingyingtiew:1234@cluster0.odyc3ax.mongodb.net/?retryWrites=true&w=majority")
db = client.virtusa

records=db.superwomen

d={"name":input("enter name"),"ph":int(input("Enter phone number")),"mail":input("Enter email id")}
records.insert_one(d)
print("inserted successfully")
read=records.find()
for x in read:
    print(x)
