class StateOutputs:

    def __init__(self):
        self.__program_output = ".csv"

    #__program_output = ".csv"
    __program_output_types = ["CSV", "JSON", "None"]

    def get_program_types(self):
        """ Get the current acceptable types
            for the program to output.
        """
        return self.__program_output_types

    @property
    def program_output(self):
        """ Get the current output type 
            set for the program
        """
        return self.__program_output
    @program_output.setter
    def program_output(self, types:str):
        """ Set the output type of the program
            This is used at the beginning to decide
            where the output of the program will be saved.
        """
        if(types == "CSV"):
            self.__program_output == ".csv"
            print("trying to set to csv")
        elif(types == "JSON"):
            self.__program_output == ".json"
            print("trying to set to json")
        else:
            self.__program_output == ""
            print("trying to set to unknown")