#!/usr/bin/env python
# -*- coding:utf-8 -*-

ab = {
    'swaroop': 'swaroop@swaroopch.com',
    'larry': 'larry@ruby-lang.org',
    'spammer': 'spammer@hotmail.com',
    'matsumoto': 'matz@ruby-lang.org'
}

print("swaroop's address is ",ab['swaroop'])

del ab['spammer']

print('\nthere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('contact{} at {}'.format(name, address))

ab['guido'] = 'guido@python.org'

if 'guido' in ab:
    print("\nguido's address is",ab['guido'])

bri = set(['braail', 'russia', 'india'])
print('india' in bri)
bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))
bri.remove('russia')
print(bri & bric)