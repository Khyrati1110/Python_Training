import logging

logging.basicConfig(filename='C:/Python_training/logs/app.log',level=logging.INFO,format='%(acstime)s - %(levelname)s - %(message)s')

logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")

print("Logging succesful")