import sys
from time import sleep

for line in sys.stdin:
    # Process the input (e.g., just echoing it for this example)
    # You can replace this with your own logic
    processed_line = line.strip()
    
    # Output to stdout
    sys.stdout.write(f"Processed: {processed_line}\n")
    sys.stdout.flush()  # Make sure the output is flushed immediately
sleep(5)
print("Done")