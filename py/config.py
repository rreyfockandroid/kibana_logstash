import logging

def config():
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)