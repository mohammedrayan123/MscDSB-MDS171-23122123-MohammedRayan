# # class petstore:
# #     def __init__(self):
# #         # self.petype = petype
# #         # self.bread = bread
# #         # self.age = age
# #         # self.gender = gender
# #         # self.price = price
# #         petlist = []
        
# #     def search():
# #         unum = input("Enter uniq")
# #         flag = False
# #         for i in unum:
# #             if unum == i:
# #                 flag = True
# #                 break
# #         if flag == True:
# #             print("Name exist in the list")
# #         else:
# #             print("does not exist")
    
# #     def list(self,unum,petype,bread,age,gender,price):
# #         self.petlist.append = [unum] 


# class petstore:
#     def __init__(self):
#         self.pets = {
#             "Dog" : [{"Breed":"Stray Dog", "Age": "2 m", "Gender":"Male", "Price": 15000},{"Breed":"Black Dog", "Age": "1 y", "Gender":"Female", "Price": 1000},{"Breed":"White Dog", "Age": "4 m", "Gender":"Male", "Price": 30000}],
#             "Cat" : [{"Breed":"Brown Cat", "Age": "3 m", "Gender":"Male", "Price": 5000},{"Breed":"Stray Cat", "Age": "8 m", "Gender":"Female", "Price": 10},{"Breed":"Beautiful Cat", "Age": "7 m", "Gender":"Female", "Price": 7000}],
#             "Rabbit" : [{"Breed":"White Rabbit", "Age": "5 m", "Gender":"Male", "Price": 9000},{"Breed":"Ugly Rabbit", "Age": "10 m", "Gender":"Male", "Price": 500},{"Breed":"Brown Rabbit", "Age": "2 m", "Gender":"Female", "Price": 10000}],
#             "Fish" : [{"Breed":"Gold Fish", "Age": "18 d", "Gender":"unknown", "Price": 70},{"Breed":"Dead Fish", "Age": "7 m", "Gender":"Prefer not to Say", "Price": 20},{"Bread":"Shy Fish", "Age": "Shy m", "Gender":"Its Shy", "Price": 600}]
#         }
        
#     # def collectPet(self,unum,petype,breed,age,gender,price):
#     #     pass
    
#     # def printPet(self):
#     #     pass
#     #     for key in 
#     #     print(self.pets)
        
#     def searchPet(self):
#         flag = 0
#         pettype = input("Enter the pet type u wanna search")
#         for i in self.pets[pettype]:
#             breed = input("Enter the Breed u wanna get details of")
#             for key in i[breed]:
#                 print(key,end='')
#                 if key == breed:
#                     print("Found")
#                     flag = 1
#             if flag == 0:
#                 print("Not Found")
#             # for value in i.values():
#             #     print(value)
# a=petstore()
# a.searchPet()

class petStore:
    def __init__(self):
        self.pet_Dict={"details":[]}
    
    def storePetDetails(self,id,species,comName,age,price):
        sub_pet_Dict={"id":id,"species":species,"comName":comName,"age":age,"price":price}
        self.pet_Dict["details"].append(sub_pet_Dict)
        print("Pet stored successfully!")
    
    def searchPet(self,comName):
        flag=0
        for i in self.pet_Dict["details"]:
            if i["comName"]==comName:
                print("ID:",i["id"])
                print("Species:",i["species"])
                print("Common Name:",i["comName"])
                print("Age:",i["age"])
                print("Price:",i["price"])
                flag=1
        if flag==0:
            print("Pet is not available")

    def sellPet(self,id):
        for i in range(0,len(self.pet_Dict["details"])):
            if self.pet_Dict["details"][i]["id"]==id:
                del self.pet_Dict["details"][i]
    def listAllPet(self):
        for i in self.pet_Dict["details"]:
            print("ID:",i["id"])
            print("Species:",i["species"])
            print("Common Name:",i["comName"])
            print("Age:",i["age"])
            print("Price:",i["price"])
    