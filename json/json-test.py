import json

# json_string = """{
#     "glossary": {
#         "title": "example glossary",
#         "GlossDiv": {
#             "title": "S",
#             "GlossList": {
#                 "GlossEntry": {
#                     "ID": "SGML",
#                     "SortAs": "SGML",
#                     "GlossTerm": "Standard Generalized Markup Language",
#                     "Acronym": "SGML",
#                     "Abbrev": "ISO 8879:1986",
#                     "GlossDef": {
#                         "para": "A meta-markup language, used to create markup languages such as DocBook.",
#                         "GlossSeeAlso": ["GML", "XML"]
#                     },
#                     "GlossSee": "markup"
#                 }
#             }
#         }
#     }
# }"""


# Read the JSON data into Python
# json_data = json.loads(json_string)


# print(json_data)

# If you have a JSON in a file, you read the data using the load() function.
with open("data.json") as f:
    data = json.load(f)
