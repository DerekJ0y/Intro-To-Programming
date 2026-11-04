# shopping=['eggs','eggs','suasage','Bacon','leatuce','bread','juice']
# print(len(shopping))

# print(shopping[4])

# print(shopping)
# shopping.append('apples')
# print(shopping)

# print(shopping[0])
# shopping.insert(0, 'White ink')
# print(shopping[0])

# print(shopping.count('eggs'))

# shopping.remove('eggs')
# print(shopping)

# shopping.sort()
# print(shopping) # it put the list into alphabetical order

# shopping.reverse()
# print(shopping)


# inventory={'book':6,
#            'paper':100,
#            'oranges':20,
#            'pork loin':7,
#            'Turkey':'out of stock'}

# print(inventory['Turkey'])

# inventory.update({'grape': 4})
# print(inventory)

# inventory['pork loin']+=7
# print(inventory['pork loin'])

# print(inventory.keys())

# print(inventory.values())

# for keys in inventory.keys():
#     print(keys)

# for values in inventory.values():
#     print(values)

# for keys, values in inventory.items():
#     print(f'{keys}: {values}')

customers={ '1':{'name':'phil',
                 'car':{'brand':'toyota',
                        'year':'2003',
                        'model':'corola'},
                'damage':{'exstent':'sever',
                          'price':'$200'},
                'covered by warenty':'yes'
                },
            '2':{'name':'Laurie',
                'car':{'brand':'Chevrolet',
                        'year':'2010',
                        'model':'tahoe'},
                'damage':{'exstent':'minor',
                        'price':'$20'},
                        'covered by warenty':'no'
                },
            '3':{'name':'Zoe',
                            'car':{'brand':'Kia',
                                    'year':'2025',
                                    'model':'Soul'},
                            'damage':{'exstent':'totalled',
                                    'price':'$30,000'},
                                    'covered by warenty':'no'
                }
}

print(customers['1']['car']['brand'])