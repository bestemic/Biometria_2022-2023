import sys

from helpers import Helper
from views.app_view import AppView


if __name__ == '__main__':
    print("Starting Eigenfaces app")
    helper = Helper()

    if len(sys.argv) and (sys.argv[1] == "-generate"):
        helper.generate()

    # view = AppView()

    # view.display()