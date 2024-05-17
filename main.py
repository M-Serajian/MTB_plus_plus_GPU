#!/usr/bin/env python3



#system libs to make full package 
import sys
import os

# Calculate the absolute path to the directory where main.py resides
# This assumes main.py is in the root of your project
project_root = os.path.abspath(os.path.dirname(__file__))
# Add the project root to the Python path
sys.path.insert(0, project_root)




#python libs
import numpy as np
import argparse


#rapids libs
import cupy as cp
import cudf



#Configuration modules
from src.arg_pars.argument_pars import parse_arguments
from src.config.config import Config


# Setup argparse
args = parse_arguments()


# Set configuration
config = Config.get_instance()
config.set_debug(args.debug)
config.set_test(args.test)



# manual libraries after configurarion is complete 
from src.hashing.hash import hashing
from tests.collision.collision_detector import detect_collision





def main():

    # Runing tests if flag is 1
    if config.test:
        print("Test mode is activated.")
        detect_collision("/home/m.serajian/share/MTB/gerbil_output/csv/k-mer_samples.csv")











if __name__ == "__main__":
    main()