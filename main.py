import sys

from logic.generator import generate
from views.app_view import AppView

if __name__ == '__main__':
    print("Starting Eigenfaces app")

    if len(sys.argv) and (sys.argv[1] == "--generate"):
        generate()

    view = AppView()
    view.display()
