"""Dumb computer that can process opcodes, as per day 2 description.

"""

# pylint thinks that we need at least 2 public methods. I disagree.
# pylint: disable=too-few-public-methods
class DumbComputer():
    """Dumb computer class that can parse and execute opcodes as specified in day 2

    Attributes:
        instructions: A list of ints representing the memory of this computer. This
        list will contain instructions and results as parsed and executed from the
        memory string in the __init__ function.
    """

    def __init__(self, memory):
        """constructor the the DumbComputer.

        Args:
            memory: A string containing all of the input memory ints separated
            by commas, without any extra whitespace.
        """
        # convert all the memory values to integers
        self.memory = [int(i) for i in memory.split(",")]

    def process_instructions(self):
        """Function that processes all the instructions in memory and returns the
        contents of memory as a string of comma separated int values
        """
        for index, value in enumerate(self.memory):
            # an instruction occurs every 4 positions
            if index % 4 == 0:
                if value == 1:
                    arg1 = self.memory[self.memory[index + 1]]
                    arg2 = self.memory[self.memory[index + 2]]
                    output_position = self.memory[index + 3]
                    self.memory[output_position] = arg1 + arg2
                elif value == 2:
                    arg1 = self.memory[self.memory[index + 1]]
                    arg2 = self.memory[self.memory[index + 2]]
                    output_position = self.memory[index + 3]
                    self.memory[output_position] = arg1 * arg2
                elif value == 99:
                    break
                else:
                    raise ValueError("Invalid opcode: {}".format(opcode))
        # return placeholder value
        return ",".join(map(str, self.memory))
