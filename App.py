import sys
import os


def get_relative_path(file):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
        
    return os.path.join(base_path, file)




from src.utils.CLIket import CLIket

filepath = get_relative_path("src/data/elements.json")
configpath = get_relative_path("src/config/config.json")

cliket = CLIket(filepath, configpath)
cliket.Home()

while cliket.on:
    response = cliket.asker()
    cliket.listener(response)