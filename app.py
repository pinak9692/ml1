# App.py should look like this below
from src.mlx1.logger import logging #A1
from src.mlx1.exception import CustomException #A2


import sys #A2


if __name__=="__main__":
    logging.info("The execution has started")
   
    try:
        a = 1/0
       
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
