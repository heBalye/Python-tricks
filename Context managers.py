import os
from contextlib import contextmanager
f = open('samle.txt', 'w')
f.write('something about me')
f.close()


with open('sample.txt', 'w'):
    f.write('something about me')


class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)

        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


# context manager in function


@contextmanager
def changedir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with changedir('one'):
    print(os.listdir())
