class IllnessDataSet(): 
    label = 'Label'
    data = []
    backgroundColor = ''
    borderColor = ''
    fill = False
    
    def __init__(self, key, illness_data, label='label', **kwargs):
        self.data = [x[key] if x[key] is not None and x[key] > 0 else 'NaN' for x in illness_data.values(key)]
        self.label = label
        if ('backgroundColor') in kwargs:
            self.backgroundColor = kwargs.get('backgroundColor')
        self.borderColor = kwargs.get('borderColor')
        self.fill = kwargs.get('fill')
