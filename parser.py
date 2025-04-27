import re

def parse_dsl(dsl_text):
    instructions = []
    lines = dsl_text.strip().split('\n')
    for line in lines:
        match = re.match(r'IF (\w+) ([<>=]+) (\d+) THEN (\w+)\(([\w\s,\/]+)\)', line)
        if match:
            variable, operator, value, action, params = match.groups()
            params = [p.strip() for p in params.split(',')]
            instructions.append({
                "variable": variable,
                "operator": operator,
                "value": int(value),
                "action": action,
                "params": params
            })
        else:
            print(f"Warning: Could not parse line: {line}")
    return instructions
