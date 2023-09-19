import argparse

parser = argparse.ArgumentParser(description="A program to demonstrate argument grouping.")

# Create an argument group for file-related options
file_group = parser.add_argument_group('File Options', 'Options related to file handling')

file_group.add_argument("-r", "--read", help="Read a file")
file_group.add_argument("-w", "--write", help="Write to a file")

# Create another group for authentication
auth_group = parser.add_argument_group('Authentication', 'Login credentials')

auth_group.add_argument("-u", "--user", help="Username")
auth_group.add_argument("-p", "--password", help="Password")

args = parser.parse_args()