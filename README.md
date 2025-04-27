# Medical DSL Compiler 🏥

This project defines a **Domain Specific Language** for medical protocols like ICU monitoring or emergency interventions.

## How it works

- Doctors write protocols in an easy language inside `examples/*.txt`
- The `parser.py` parses this into instructions
- The `compiler.py` compiles these instructions into Python code
- `runtime.py` defines what actions like `administer` or `alert` do
- `app.py` connects everything and runs the system

## Running the project

```bash
python app.py
