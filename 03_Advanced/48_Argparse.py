import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='A simple command-line parser example.')

# Define command-line arguments
parser.add_argument('--input', help='Input file path', required=True)
parser.add_argument('--output', help='Output file path', required=True)
parser.add_argument('--verbose', help='Enable verbose mode', action='store_true')

# Parse the command-line arguments
args = parser.parse_args()

# Access the parsed arguments
input_file = args.input
output_file = args.output
verbose_mode = args.verbose

# Process the arguments
print('Input file:', input_file)
print('Output file:', output_file)
print('Verbose mode:', verbose_mode)
