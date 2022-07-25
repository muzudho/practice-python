"""
python -m tests.dimport_test2 -m src.hello
"""
from src.dimport import Dimport
import argparse

# Command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('-m', help='module')
args = ap.parse_args()

print(Dimport.load(args.m, "Hello").message)
