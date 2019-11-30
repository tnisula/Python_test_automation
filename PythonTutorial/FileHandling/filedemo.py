"""
File I/O
'w' => Write-only mode
'r' => Read-only mode
'r+' => Read and Write mode
'a' => Append Mode
"""

my_list = ['This is the first line of the file.',
           'Second line of the file', 'Third line of the file']
my_file = open("firstfile.txt", 'w')

for item in my_list:
    my_file.write(str(item) + '\n')
my_file.close()

my_file = open("firstfile.txt", "r")
print(str(my_file.read()))
my_file.close()

print("Line by line ............")
my_file_line = open("firstfile.txt", "r")
print(str(my_file_line.readline()))
print(str(my_file_line.readline()))
print(str(my_file_line.readline()))
my_file_line.close()

"""
With / As keywords
"""
"""
print("Normal write start")
my_write = open("textfile.txt", "w")
my_write.write("Trying to write to the file")
my_write.close()

print("Normal read start")
my_read = open("textfile.txt", "r")
print(str(my_read.read))
my_read.close()
"""
print("With As Write start")
with open("withas.txt", "w") as with_as_write:
    with_as_write.write("This is an example of With As write/read\n")
    value = ('the answer', 42) # Tuple to ne written
    s = str(value)  # convert the tuple to string
    with_as_write.write(s)

print()
print("With As Read start")
with open("withas.txt", "r") as with_as_read:
    print(str(with_as_read.read()))

f = open('workfile.bin', 'w+b')
f.write(b'0123456789abcdef')
f.seek(5)      # Go to the 6th byte in the file
print(f.read(1))
f.seek(-3, 2)  # Go to the 3rd byte before the end
print(f.read(1))
f.close()

# How to write json data to a file
import json
data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

# How to read data from a file
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')