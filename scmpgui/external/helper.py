import subprocess

external_script = 'dummy.py'
    
try:
    # Create a Popen instance
    process = subprocess.Popen(['python', external_script], 
                                stdin=subprocess.PIPE, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE, 
                                text=True)

    # Provide input to the external program (replace 'input_data' with your input)
    input_data = "Hello, World!\nThis is a subprocess"
    output, error = process.communicate(input=input_data)

    # Process or display the output as needed
    # You can return it as a response or save it to a database, etc.
    
    print(f'Output: {output}')
except subprocess.CalledProcessError as e:
    # Handle any errors that occur during execution
    print(f'Error: {e}', status=500)