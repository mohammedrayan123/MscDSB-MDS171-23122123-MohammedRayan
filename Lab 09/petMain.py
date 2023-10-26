
import random
class petStore:
    def __init__(self):
        self.pets={
            "dog":[],
            "cat":[],
            "rabbit":[],
            "parrot":[]
        }
        self.main()
    def genID(self):
        ID=""
        for i in range(0,5):
            ID+=str(random.randint(i,10))
        return ID
    def collectpet(self):
        pet_type = input("Enter pet type: ").lower()
        breed=input("Enter the Breed: ")
        age=int(input("Enter age of the pet(in months): "))
        price=int(input("Enter the Price: "))
        if pet_type in self.pets:
            ID=self.genID()
            self.pets[pet_type].append({
                "ID":ID,
                "Breed": breed.upper(),
                "Age": age,
                "Price": price,
                "Avability": True          
            })
            
    def searchPet(self):
        search_pet_type=input("Enter the Pet type you want to search[DOG/CAT/RABBIT/PARROT]: ").lower()
        search_breed=input("Enter the Breed you want to search: ").upper()
        search_id=input("Enter the pet ID: ")
        if search_pet_type in self.pets:
            for item in self.pets[search_pet_type]:
                if search_breed == item['Breed']:
                    if search_id in item["ID"]:
                        print(item)
                    # else:
                    #     print("ID not exist")
                else:
                    print("Breed is not exist")               
        else:
            print("Pet type not exist")
            
    
    def sellPet(self):
        search_pet_type=input("Enter the Pet type you want to search[DOG/CAT/RABBIT/PARROT]: ").lower()
        search_breed=input("Enter the Breed you want to search: ").upper()
        search_id=input("Enter the pet ID: ")
        if search_pet_type in self.pets:
            for item in self.pets[search_pet_type]:
                if search_breed == item['Breed']:
                    if search_id in item["ID"]:
                        item["Avability"] = False
                    # else:
                    #     print("ID not exist")
                else:
                    print("Breed is not exist")               
        else:
            print("Pet type not exist")
    
    def showAllpets(self):
        for item,value in self.pets.items():
            print(item,value)
    
    def main(self):
        while True:
            print("Wellcome to Christ Pet Store")
            print("Options")
            print("------------------")
            print("1.Store pet details")
            print("2.Search for a pet")
            print("3.Sell a pet")
            print("4.List all pets")
            print("5.Exit")
            choice=int(input("Enter Your Choice: "))
            if choice == 1:
                self.collectpet()
            elif choice == 2:
                self.searchPet()
            elif choice == 3:
                self.sellPet()
            elif choice == 4:
                self.showAllpets()
            elif choice == 5:
                print("Exiting....")
                break
            else:
                print("Invalid Input!!!!!")

# import petModule as pt
# def userLogin(role):
#     print("\nLogin Page")
#     print("_"*15)
#     name=None
#     username=input("Username:")
#     flag=False
#     if role==1:
#         for uname in open("Credentials.csv","r+").readlines():
#             cred=uname.split(",")
#             if cred[1]==username:
#                 flag=True
#                 name=cred[3]
#         if flag==False:
#             print("Username is incorrect")
#             userLogin(role)
#         else:
#             flag=False
#             password=input("Password:")
#             for cred in open("Credentials.csv","r+").readlines():
#                 passw=cred.split(",")
#                 if passw[2]==password:
#                     flag=True
#                     name=passw[3]
#             if flag==False:
#                 print("Password is incorrect")
#                 userLogin(role)
#             else:
#                 return True
# def adminAction(adminObj):
#     action=int(input("Select your action \n1.Store New Pet \n2.Search for Pet \n3.Sell a pet \n4.List all pets \n5.Exit"))
#     if action==1:
#         id=int(input("Enter the pet ID:"))
#         species=input("Enter the species of the pet:")
#         comName=input("Enter the common name of the pet:")
#         age=int(input("Enter the age of the pet:"))
#         price=int(input("Enter the price of the pet"))
#         adminObj.storePetDetails(id,species,comName,age,price)
#         adminAction(adminObj)
#     elif action==2:
#         adminObj.searchPet(input("Enter the common name of the pet:"))
#         adminAction(adminObj)
#     elif action==3:
#         adminObj.sellPet(input("Enter the ID of the pet:"))
#         adminAction(adminObj)
#     elif action==4:
#         adminObj.listAllPet()
#         adminAction(adminObj)
#     elif action==5:
#         return True
#     else:
#         print("Enter the right choice")
#         adminAction(adminObj)
# def userAction():
#     print("Welcome to Pet Store")
#     userObj=pt.petStore()
#     action=int(input("Please select your action \n1.Search for a pet \n2.List all pets \n3.Exit"))
#     if action==1:
#         userObj.searchPet(input("Enter the common name of the pet:"))
#         userAction()
#     elif action==2:
#         userObj.listAllPet()
#         userAction()
#     elif action==3:
#         return True
#     else:
#         print("Select correct action")
#         userAction()

# while(True):
#     userType=int(input("Select user type 1.Admin 2.Customer"))
#     exit=False
#     if userType==1:
#         if userLogin(userType):
#             adminObj=pt.petStore()
#         exit=adminAction(adminObj)
#     elif userType==2:
#         exit=userAction()
#     if exit:
#         exit()