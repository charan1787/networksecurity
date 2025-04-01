import logging
import os
from datetime import datetime

#Creating a file name for each log
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M')}.log"

#creates a path by creating the logs folder
log_path=os.path.join(os.getcwd(),"logs") 

#creates the path folder and if exists it ignores the same path
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)



