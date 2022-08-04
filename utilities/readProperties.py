import configparser

# Here we are creating an object 'config' which will have methods to read ini file
# This method is present under configparser.RawConfigParser()
config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

# This is simple python class
# Now we will be creating @staticmethod
# Benefit of @staticmethod is that we can access class method directly by mentioning method name,
# without creating an object
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():  # in staticmethod we need not to pass self in the function.
        email = config.get('common info', 'useremail')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
