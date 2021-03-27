import yaml

class DatabaseController:
    
    """
    structure of the database:
    
    User:
        hash(default):
            name: default
            temperature: 24.6
        hash(jack):
            name: jack
            temperature: 25.8
    """

    def __init__(self):
        self.dbFile = "database.yaml"
        self.dbUser = "User"
        self.dbName = "name"
        self.dbTemp = "temperature"

        # reset the database
        self.resetDatabase()


    def resetDatabase(self):
        with open("database_default.yaml") as f:
            lines = f.readlines()
            with open(self.dbFile, "w") as f1:
                f1.writelines(lines)


    # get the list of existing users
    def getExistingUsers(self):
        nameList = []
        with open(self.dbFile,'r') as yamlfile:
            database = yaml.safe_load(yamlfile)
            
            if database[self.dbUser] != None:
                for k, v in database[self.dbUser].items():
                    if database[self.dbUser][k][self.dbName] == "default":
                        pass
                    else:
                        nameList.append(database[self.dbUser][k][self.dbName])
                        print(nameList)
                return nameList
            else:
                return []
    

    # # read the yaml file for one data of a user
    def readNamedTemperature(self, userName):
        with open(self.dbFile, "r") as yamlFile:
            database = yaml.safe_load(yamlFile) 
            for k, v in database[self.dbUser].items():
                if userName == database[self.dbUser][k][self.dbName]:
                    # print(database[self.dbUser][k][self.dbTemp])
                    return database[self.dbUser][k][self.dbTemp]


    # update the yaml file by adding the newest registered user
    def addUser(self, userName, userTemp):
        
        if not self.checkExistUser(userName):

            # updater database
            # add user to name list
            userNameList = userName

            # add user to database
            with open(self.dbFile,'r') as yamlfile:
                databaseUpdate = yaml.safe_load(yamlfile) # Note the safe_load
                databaseUpdate[self.dbUser].update({hash(userName): {self.dbName:userName, self.dbTemp:userTemp}})

            if databaseUpdate:
                with open(self.dbFile,'w') as yamlfile:
                    yaml.safe_dump(databaseUpdate, yamlfile) # Also note the safe_dump
            return True
        else:
            print("user already exists")
            return False
    

    def deleteUser(self, userName):
        # delete user 
        if not self.checkExistUser(userName):    
            return False
        
        else:
            with open(self.dbFile,'r') as yamlfile:
                databaseUpdate = yaml.safe_load(yamlfile) # Note the safe_load

                userHashDelete = 0
                for k, v in databaseUpdate[self.dbUser].items():
                    if userName == databaseUpdate[self.dbUser][k][self.dbName]:
                        userHashDelete = k

                del databaseUpdate[self.dbUser][userHashDelete]
                
            if databaseUpdate:
                with open(self.dbFile,'w') as yamlfile:
                    yaml.safe_dump(databaseUpdate, yamlfile) # Also note the safe_dump
            return True


    # check the exist user by user name
    def checkExistUser(self, userName):
        userNameList = self.getExistingUsers()
        
        # name exist
        if userName in userNameList:
            return True
        else:
            # name not exist
            return False


# db = DatabaseController()
# db.resetDatabase()
# db.getExistingUsers()
# db.readNamedTemperature("default1")
# print(db.checkExistUser("default1"))
# db.addUser("jack", 24.6)
# db.addUser("john", 25.0)
# db.getExistingUsers()
# db.deleteUser("jack")