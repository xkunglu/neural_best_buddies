
"""
    top level function just to handle script
    Example
        #!/bin/bash
        python3 main.py --datarootA ./images/original_A.png --datarootB ./images/original_B.png --name lion_cat --k_final 10

"""
from nbb.options import Options
import nbb

if __name__ == '__main__':
    nbb.run(Options().parse())
