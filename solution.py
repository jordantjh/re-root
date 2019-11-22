import sys

from models.file_handler import FileHandler


class Solution:
    def execute(self):
        """ Process file and output result. """

        # Get file name from command line
        file_name = self.get_file_name()

        # Open file
        f = FileHandler(file_name)

        # Solve - process each line of the file
        f.process()

        # Display result
        f.print()

    def get_file_name(self):
        """ Get file name from command line """

        try:
            file_name = sys.argv[1]
        except IndexError as e:
            print("Error: File name must be provided from the command line.\n")
            sys.exit()

        return file_name


if __name__ == "__main__":
    sol = Solution()
    sol.execute()
