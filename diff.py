import json_delta 
import json
import urllib.request

with open('test1.json', encoding='utf-8') as data_file:
    left = json.loads(data_file.read())

with open('test2.json', encoding='utf-8') as data_file:
    right = json.loads(data_file.read())

##print(data)

#output = json_delta._diff.diff(left, right, compare_lengths=False, common_key_threshold=1.0, verbose=True, key=None)
output = json_delta._udiff.udiff(left, right, patch=[], indent=0.1, use_ellipses=True, entry=True)

#output = json_delta._diff.needle_diff(left, right, NoneType)

#output = json_delta.load_and_diff(left, right, both=None, array_align=None, compare_lengths=None, common_key_threshold=None, minimal=None, verbose=True)

#output = json_delta.udiff(left,right, patch=[], indent=0, use_ellipses=True, entry=False)


print(output)

# with open("output.json", 'w') as f: 
#     for item in output: 
#         f.write("%s\n" % item)
