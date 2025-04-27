def compile_to_python(instructions, output_path):
    with open(output_path, 'w') as f:
        f.write("# Auto-generated compiled protocol\n\n")
        f.write("from runtime import administer, alert\n\n")
        f.write("def run_protocol(patient_data):\n")
        
        for instr in instructions:
            cond = f"patient_data['{instr['variable']}'] {instr['operator']} {instr['value']}"
            if instr["action"] == "Administer":
                action = f"administer('{instr['params'][0]}', '{instr['params'][1]}')"
            elif instr["action"] == "Alert":
                action = f"alert('{instr['params'][0]}')"
            else:
                action = "# Unknown action"

            f.write(f"    if {cond}:\n")
            f.write(f"        {action}\n\n")
