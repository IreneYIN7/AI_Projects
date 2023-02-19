from collections import defaultdict

# Define the defaultdict
d = defaultdict(list)
d['a1'] = ['b', 'c']
d['a2'] = ['b19', 'b29']
d['a3'] = ['xy', 'wx', 'a2']
d['a'] = ['a1', 'a2', 'a3']
d['b'] = -4
d['c'] = 3
d['b19'] = 5
d['b29'] = 2
d['xy'] = -1
d['wx'] = 8
print(d)
# Create a mapping of keys to their corresponding values
key_to_values = defaultdict(list)
for key, values in d.items():
    print("key: ", key)
    print("values: ", values)
    for value in values:
        if value in d:
            print(value)
            print(int(d[value]) * -1)
            key_to_values[key].append((value, int(d[value]) * -1))
        else:
            key_to_values[key].append(value)

# Create the desired format
result = ['a']
for key in ['a1', 'a2', 'a3']:
    values = key_to_values[key]
    if all(isinstance(x, tuple) for x in values):
        result.append([key] + values)
    else:
        result.append([key] + [[x for x in values if isinstance(x, str)]] + [x for x in values if isinstance(x, tuple)])

# Print the result
print(result)
