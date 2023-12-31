import sys
from src.logger import logging
import traceback


def error_message_detail(err, details:sys):
    _,_,exc_tb = details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error in python script [{filename}] line number [{exc_tb.tb_lineno}] error message : [{str(err)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, err, details:sys):
        super().__init__(err)
        tb = traceback.extract_tb(err.__traceback__)
        for line in tb:
            logging.error(f"Error in python script [{line.filename}], line number [{line.lineno}], in [{line.name}]: {line.line}")
        self.error_message = error_message_detail(err,details)
        logging.error(self.error_message)
        
    
    def __str__(self):
        return self.error_message