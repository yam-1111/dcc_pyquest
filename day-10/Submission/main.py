
import json

class UserInfos:
    def __init__(self, name=None, age=None, favorite_food=None):
        self.name = name
        self.age = age
        self.favorite_food = favorite_food

    def interactive(self, filename : str):
        """
        prompts the user to input on json writing
        args :
            filename (str): filepath of the file to be written
        returns : None
        """
        self.name = str(input("What is your name: "))
        while True:
            try:
                self.age = int(input("What is your age: "))
                if self.age < 0:
                    raise Exception
                else:
                    break
            except:
                print("Please enter integer")
        self.favorite_food = str(input("What is your favorite food?"))
        self.export(filename)

    def export(self, filename : str, operation='w'):
        """
        exports the given attr to the json
        args : 
            filename(str): filepath of the file to be written
            operation(str) : file operation 
        returns : None
        """
        with open(filename, operation) as f:
            json.dump(self.__dict__, f)
    
UserInfos().interactive("/home/vee/Personal/15-Days-of-Python/day-10/output.json")