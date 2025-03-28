import json

class Merger:
    def __init__(self):
        self.elements = None
        self.filePath = None
        
    def saveElements(self, data):
        with open(self.filePath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    
    
    def verifyDiscovered(self, element) -> bool:
        for k, v in self.elements.items():
            if k == element:
                if v['discovered'] == True:
                    return True
                return False
    
        
    def makeMerger(self, element1: str, element2: str):
        tempState = 0
        
        for k, v in self.elements.items():
            
            if v['el1'] == element1 and v['el2'] == element2:
                
                if self.verifyDiscovered(v['el1']):
                    
                    if self.verifyDiscovered(v['el2']):
                        
                        tempState = 1
                        v['discovered'] = True
                        self.saveElements(self.elements)
                        
                        print()
                        print(f'= {v['icon']}  {k}')
                        print()
                    
                    else:
                        
                        print(f'You not have the Element_2: {v['el2']}')
                        tempState = 0
                
                else:
                    
                    print(f'You do not have the Element_1: {v['el1']}')
                    tempState = 0
                
                
        if tempState == 0:
            print('Not exist this combination')
            return
                    