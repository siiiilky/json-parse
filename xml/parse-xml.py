import untangle
obj = untangle.parse('test.xml')

print(obj.root.child['name'])