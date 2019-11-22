import sys

from models.file_handler import FileHandler


class Solution:
    def execute(self):
        """ Process file and output result. """

        # Get file name from command line
        try:
            file_name = sys.argv[1]
        except IndexError as e:
            print("Error: File name must be provided from the command line.\n")
            sys.exit()

        # Open file
        f = FileHandler(file_name)

        # Solve - process each line of the file
        f.process()

        # Display result
        f.print()


if __name__ == "__main__":
    sol = Solution()
    sol.execute()
