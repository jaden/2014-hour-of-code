import sys

def times_table(low, high):
    high += 1 # Account for 0-based counting

    width = len(str(high * high)) + 1 # Add one for space between columns

    fmt = "{:>%s}" % width # Set the format for each column

    # Print out the header
    sys.stdout.write(" " * (width + 1)) # Print space in front of header row
    for h in range(low, high):
        sys.stdout.write(fmt.format(h))
    print
    print "-" * (((abs(high - low) + 1) * width) + 1) # Print a horizontal line

    # Print out the times table
    for i in range(low, high):
        sys.stdout.write((fmt + "|").format(i))
        for j in range(low, high):        
            sys.stdout.write(fmt.format(i * j))
        print

times_table(1, 12)
