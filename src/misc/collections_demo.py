import collections
import json
tree = lambda:collections.defaultdict(tree)
print(tree2)
some_dict = tree2()
some_dict['colours']['favourite']="yellow"
print json.dumps(some_dict)