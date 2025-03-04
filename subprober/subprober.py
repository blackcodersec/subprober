import sys
import os

# Add the parent directory to the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.insert(0, parent_dir)

# Now use a relative import
from subprober.modules.handler import Main

def main():
    Main()
if __name__ == '__main__':
    main()
