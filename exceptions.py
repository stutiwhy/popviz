# for any type of data cleaning error
class DataCleaningError(Exception):
    def __init__(self, message="An error occurred during data cleaning."):
        self.message = message
        super().__init__(self.message)

# this exception will be raised if there is a missing column in the dataset
class MissingColumnError(DataCleaningError): 
    def __init__(self, column_name):
        self.column_name = column_name
        self.message = f"Missing required column: {column_name}."
        super().__init__(self.message)

# defining a file handling exception that can be raised at any file handling error.
class FileHandlingError(Exception): 
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# creating exception for plotting errors
class PlottingError(Exception):
    def __init__(self, message="An error occurred during plotting."):
        self.message = message
        super().__init__(self.message)
