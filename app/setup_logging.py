import argparse
import logging

def setup_logging(default_level='INFO'):
    parser = argparse.ArgumentParser(description="Python Application")
    parser.add_argument("--log", default=default_level, 
                        help="Set log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)")

    args = parser.parse_args()

    logging.basicConfig(level=args.log.upper())
    logger = logging.getLogger(__name__)
    
    return logger