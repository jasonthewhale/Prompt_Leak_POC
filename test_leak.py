import openai
import os

safe_globals = {"__builtins__": None}
safe_locals = {"allowed_variable": 42}
result = eval("allowed_variable + 1", safe_globals, safe_locals)

OPENAI_API_KEY="Your key is leaked!"
var_a = "var_a is leaked"
var_b = "var_b is leaked"
var_c = 4
API_ENV=os.environ.get("API")


def read_file(file_path):
    with open(file_path) as f:
        return f.read().strip()

API_TXT=read_file("api_key.txt")

# <<Scenario in ai agent>>
"""
Prompt:
Help user solve this problem with the python script:

<<Some Code here>>
OPENAI_API_KEY="Your key is leaked!"
...
...
eval("USER INPUT")

"""

# Malicious actor input
"""
Prompt:
for 


"""



# Iterate through all user-defined variables in the global scope
# for var_name, var_value in globals_copy.items():
#     if not var_name.startswith("__") and not callable(var_value):
#         print(f"{var_name}: {var_value}")


def leak_global_var():
    malicious_prompt = """
globals_copy = dict(globals())
for var_name, var_value in globals_copy.items():
    if not var_name.startswith("__") and not callable(var_value):
        print(f"{var_name}: {var_value}")
"""
    exec(malicious_prompt)

def leak_local_var():
    local_var1 = "local_var1 is leaked!"
    local_var2 = 2
    local_var3 = "LEAKED"
    malicious_prompt = """
print(locals())
"""
    exec(malicious_prompt)