import cmd

class MyCmd(cmd.Cmd):

    intro = "Welcome to MyCmd. Type 'help' or '?' to list command."

    prompt = "MyCmd"

    def do_greet(self, line):
        """ Greet a person by name """
        print("Hello, " + line)

    def do_add(self, line):
        """Add two numbers"""
        numbers = line.split()
        if len(numbers) == 2:
            try:
                result = int(numbers[0]) + int(numbers[1])
                print("Result:", result)

            except ValueError:
                print("Invalid numbers")

        else:
            print("Usage: add <number1> <number2>")

    def do_exit(self, line):
        """Exit the program"""
        return True


if __name__ == "__main__":
    MyCmd().cmdloop()

