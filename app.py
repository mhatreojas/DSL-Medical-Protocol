from parser import parse_dsl
from compiler import compile_to_python
from patient_data import patient_data

# Read DSL script
with open('examples/covid_protocol.txt', 'r') as f:
    dsl_text = f.read()

# Parse
instructions = parse_dsl(dsl_text)

# Compile
compile_to_python(instructions, 'output/compiled_code.py')

# Import the generated code dynamically
import importlib.util
spec = importlib.util.spec_from_file_location("compiled_code", "output/compiled_code.py")
compiled_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compiled_module)

# Run the protocol
compiled_module.run_protocol(patient_data)
