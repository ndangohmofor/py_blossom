from hash_map import HashMap
from blossom_lib import flower_definitions

blossom = HashMap(len(flower_definitions))
for i in flower_definitions:
    blossom.assign(i[0], i[1])

print(blossom.retrieve('daisy'))