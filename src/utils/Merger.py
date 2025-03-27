import json

class Merger:
    def __init__(self):
        self.elements = None
        self.filePath = None
        
    def saveElements(self, data):
        with open(self.filePath, 'w', encoding='utf-8') as file:
            json.dumps(data, file, indent=4)
            print('Elements Updated!!')
        
    def makeMerger(self, element1: str, element2: str):
        for k, v in self.elements.items():
            if v['el1'] == element1.lower() and v['el2'] == element2.lower():
                print()
                print(f'= {v['icon']}  {k.capitalize()}')
                print()
                break   