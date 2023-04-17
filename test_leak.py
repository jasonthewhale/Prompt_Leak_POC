import openai

OPENAI_API_KEY="Your key is leaked!"
var_a = "var_a is leaked"
var_b = "var_b is leaked"
var_c = 4

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


def leak_var():
    malicious_prompt = """
globals_copy = dict(globals())
for var_name, var_value in globals_copy.items():
    if not var_name.startswith("__") and not callable(var_value):
        print(f"{var_name}: {var_value}")
"""
    exec(malicious_prompt)