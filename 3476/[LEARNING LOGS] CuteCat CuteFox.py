"""[LEARNING LOGS] CuteCat CuteFox"""

import json
n = int(input())
cats = {}
foxs = {}
for _ in range(n):
    cat_name = input().strip()
    s = json.loads(cat_name)
    for key ,value in s.items():
        if value.startswith('Cat'):
            cats.update(s)
        else:
            foxs.update(s)
if ('Cat01' not in cats.values()
        and 'Garfield' not in foxs
        and 'Garfield' not in cats):
    cats['Garfield'] = 'Cat01'
if ('Fox01' not in foxs.values()
        and 'Fubuki' not in cats
        and 'Fubuki' not in foxs):
    foxs['Fubuki'] = 'Fox01'
def sort_catfox(animal):
    """sort cat and fox """
    return int(animal[1][3:])
print(f"Cat : {len(cats)}")
print(f"Fox : {len(foxs)}")
for key , value in sorted(cats.items(),key=sort_catfox):
    print(f"{key} : {value}")
for key , value in sorted(foxs.items(),key=sort_catfox):
    print(f"{key} : {value}")
