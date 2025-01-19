# Implement a context manager using the with statement that opens a file,
# writes text, and closes the file automatically.
class FileWriter:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write(self.text)
        self.file.close()

# Usage
with FileWriter('/Users/siddhantsmac/Desktop/120 Questions/output.txt', 'Hello, World!') as file:
    pass