"""
Demonstrates logging in Python.
Covers: basicConfig, handlers, formatters, log levels
"""
import logging

def main():
    # Simple configuration
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='app.log',
        filemode='w'
    )
    
    # Create logger
    logger = logging.getLogger("MyLogger")
    
    # Add a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.debug("Debug message - detailed info for developers")
    logger.info("Info message - general confirmation of success")
    logger.warning("Warning message - something unexpected happened")
    logger.error("Error message - some functionality failed")
    logger.critical("Critical message - serious error, system may stop")

if __name__ == "__main__":
    main()
