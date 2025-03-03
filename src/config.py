class FileConfig:
    FILE_TYPES = ['NW_CREDIT', 'NW_DEBIT', 'STARLING']

    def __init__(self, date_col='Date', desc_col='Description', value_col='Value', flip_values=False):
        self.date_col = date_col
        self.desc_col = desc_col
        self.value_col = value_col
        self.flip_values = flip_values

    @staticmethod
    def natwest_debit():
        return FileConfig()
    
    @staticmethod
    def natwest_credit():
        return FileConfig(flip_values=True)

    @staticmethod
    def starling():
        return FileConfig(date_col='Date', desc_col='Reference', value_col='Amount (GBP)')

    @staticmethod
    def from_type(type):
        if type == 'NW_CREDIT':
            return FileConfig.natwest_credit()
        
        if type == 'STARLING':
            return FileConfig.starling()
        
        return FileConfig.natwest_debit()

    @staticmethod
    def detect_from_filename(filename):
        if 'mastercard' in filename.lower():
            return FileConfig.natwest_credit()

        if 'starling' in filename.lower():
            return FileConfig.starling()
        
        return FileConfig.natwest_debit()

