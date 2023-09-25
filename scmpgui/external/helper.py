import subprocess
import time

external_script = 'dummy.py'

print('Starting dummy process.')
try:
    # Create a Popen instance without communicating
    process = subprocess.Popen(['python', external_script],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)

    # Provide input to the external program (replace 'input_data' with your input)
    input_data = "Hello, World!\nThis is a subprocess"
    process.stdin.write(input_data)
    process.stdin.close()

    # Check if the subprocess is still running
    while process.poll() is None:
        print("Waiting for the subprocess to finish...")
        time.sleep(1)  # Wait for 1 second before checking again

    # Subprocess has finished
    output, error = process.communicate()

    # Process or display the output as needed
    print(f'Output Recieved:\n{output}')
except subprocess.CalledProcessError as e:
    # Handle any errors that occur during execution
    print(f'Error: {e}', status=500)

# Code to run after the subprocess has finished
print("Subprocess has finished. Continuing with other code...")
