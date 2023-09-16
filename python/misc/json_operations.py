import json

"""
json str    -> loads    -> dict     # De-serialization
dict        -> dump     -> json file
json file   -> load     -> dict
dict        -> dumps    -> json str # Serialization


dict -> dumps -> str
"""

# json string
data = """{
        "service_name": "wallet_service",
        "tech_stack": "java_maven_springboot",
        "hosting": "kuberneted"
        }"""

# 1 json string -> dict (deserialization)
service_dict = json.loads( data )
print( service_dict )

# 2 dict -> json file
with open("service.json", "w") as write_file:
    json.dump (service_dict, write_file)

# 3 json file -> dict
with open("service.json", "r") as read_file:
    data_dict = json.load(read_file)
    print (data_dict)

# 4 dict -> json string (serialization)
json_str = json.dumps (data_dict, indent = 4)
print (json_str)