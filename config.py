class FileConfig:
    FILE_TYPES = ['NW_CREDIT', 'NW_DEBIT', 'STARLING']

    def __init__(self, date_col='Date', desc_col='Description', value_col='Value', flip_values=False):
        self.date_col = date_col
        self.desc_col = desc_col
        self.value_col = value_col
        self.flip_values = flip_values

    @staticmethod
    def from_type(type):
        if type == 'NW_CREDIT':
            return FileConfig(flip_values=True)
        
        if type == 'STARLING':
            return FileConfig(date_col='Date', desc_col='Reference', value_col='Amount (GBP)')
        
        return FileConfig()
