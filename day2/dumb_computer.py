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
                    raise ValueError("Invalid opcode: {}".format(value))
        # return placeholder value
        return ",".join(map(str, self.memory))

def brute_force_solve(desired_output):
    input_memory = ("1,{},{},3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1"
                    ",31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59"
                    ",10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,"
                    "10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1"
                    ",115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,"
                    "2,14,0,0")
    # check all combinations of noun and verb between 0-99
    for noun in range(100):
        for verb in range(100):
            computer = DumbComputer(input_memory.format(noun, verb))
            result = computer.process_instructions()
            if result.split(",")[0] == desired_output:
                return 100 * noun + verb
    raise ValueError("Could not find input that matches desired output")

"""
input_memory = ("1,{},{},3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1"
                ",31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59"
                ",10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,"
                "10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1"
                ",115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,"
                "2,14,0,0")

computer = DumbComputer(input_memory.format(12, 2))
print(computer.process_instructions().split(",")[0])
"""
