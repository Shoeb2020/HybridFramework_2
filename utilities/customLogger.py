
import logging

# To generate logs we need to create this customLogger.py file
# Here we need to import logger from logging package
# import logging
#
class LogGen: #(log generation class)
    @staticmethod
    def loggen(): # Making loggen() method (staticmethod so that we can easily call it
        logging.basicConfig(level=logging.INFO, force=True,
                            filename=".\\Logs\\Automation.log",
                            format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger() # creating logger object (its a simple variable)
        logger.setLevel(logging.INFO) # here we are setting level as INFO, there are other levels as well
        return logger

#______________________________________________________________________#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=".\\Logs\\GenerateAutomation.log",
#                             format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger=logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger



# basicConfig() is a method present inside logging package,
#         Here we can mention where we want to store our logs. ( file path and name we need to mention)
#         logging.basicConfig(filename=".//Logs//automation.log",
#                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:S% %p')
#
#         logging.basicConfig(filename="automation.log")
#         logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
#
#


# So basically we have created 1 utility file containing loggen() method.
# by using the logger object present inside loggen() method we can generate logs.
# Now in test_login.py file (ie. testCase file) whatever actions we are doing,
# we can log them into our log file. (ie. automation.log file)
# After creating customLogger.py file, go to the the test_login.py file and import this logGen() package
# # and add logs statements to login_test.py file to log the actions.