# Import required modules
import os                          # For file system path and directory operations
import logging                     # Python's built-in logging module
from datetime import datetime      # For timestamping log file names

# Define a custom logger class
class CustomLogger:
    def __init__(self, log_dir="logs"):
        """
        Initializes the custom logger by creating a log directory and configuring the logging settings.
        :param log_dir: Name of the directory to store log files. Defaults to "logs".
        """

        # Create the full path to the logs directory (e.g., /path/to/current_dir/logs)
        self.logs_dir = os.path.join(os.getcwd(), log_dir)

        # Create the directory if it doesn't exist. `exist_ok=True` prevents errors if the directory exists.
        os.makedirs(self.logs_dir, exist_ok=True)

        # Create a timestamped log file name (e.g., 08_17_2025_14_30_55.log)
        log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

        # Get the full path to the log file (e.g., /path/to/logs/08_17_2025_14_30_55.log)
        log_file_path = os.path.join(self.logs_dir, log_file)

        # Configure the logging system
        logging.basicConfig(
            filename=log_file_path,     # Set the log file path
            format='[%(asctime)s]- %(levelname)s %(name)s: (line:%(lineno)d) - %(message)s',
                                        # Define log message format:
                                        # Timestamp - Level - Logger Name - Line Number - Message
            level=logging.INFO,         # Set default log level to INFO
        )
        
    def get_logger(self, name=__file__):
        """
        Returns a logger instance with the specified name.
        :param name: Optional name for the logger (usually the file name).
        :return: Configured logger object.
        """
        # Return a logger object with a name (basename strips full path for clarity)
        return logging.getLogger(os.path.basename(name))

# Example usage when this script is run directly
if __name__ == "__main__":
    # Instantiate the custom logger
    logger = CustomLogger()
    
    # Get a logger instance with the name "__file__" (as a string here, not the __file__ variable)
    logger = logger.get_logger("__file__")
    
    # Write an INFO-level log message
    logger.info("Custom Log initialization complete.")
# This code sets up a custom logging system that creates a log file in a specified directory