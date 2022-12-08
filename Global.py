from datetime import datetime

def GetTime():
    """
    Just to get the formatted time for 
    the current function
    """
    return datetime.now().strftime("%H:%M:%S")
