"""
python -m tests.dimport_test
"""
from src.dimport import Dimport

print(Dimport.load("src.hello", "Hello").message)
