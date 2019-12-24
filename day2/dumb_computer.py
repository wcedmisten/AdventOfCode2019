"""Dumb computer that can process opcodes, as per day 2 description.

"""

class DumbComputer(object):
    """Dumb computer class that can parse and execute opcodes as specified in day 2

    Attributes:
        instructions: A list of ints representing the memory of this computer. This
        list will contain instructions and results as parsed and executed from the
        instructions string in the __init__ function.
    """

    def __init__(self, instructions):
        """constructor the the DumbComputer.

        Args:
            instructions: A string containing all of the opcode instructions separated
            by commas, without any extra whitespace.
        """
        # convert all the instructions to integers
        self.instructions = [int(i) for i in instructions.split(",")]
    
    def process_instructions(self):
        """Function that processes all the instructions in memory and returns the
        contents of memory as a string of comma separated int values
        """
        for opcode in self.instructions:
            if opcode == 1:
                print(1)
            elif opcode == 2:
                print(2)
            elif opcode == 99:
                print(99)
#            else:
#                raise ValueError("Invalid opcode: {}".format(opcode))
        # return placeholder value
        return ""
         
