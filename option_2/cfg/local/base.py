class Config:
    KEY_1 = VALUE_1

    def __init__(self, environment):
        self.verticals = {}
        
        # Loop through the verticals & import its config class
        for module in vertical_config_module:
            vertical_config_class = import_module(...)
            self.verticals[vertical] = vertical_config_class()
    
    def get(self, key, vertical):
        default_value = getattr(self, key)
        if vertical not in self.verticals:
            return default_value

        return getattr(self.verticals[vertical], key, default_value)

    def get_config_by_vertical(self, vertical):
        default_value = getattr(self, key)
        if vertical not in self.verticals:
            return default_value

        return getattr(self.verticals[vertical], key, default_value) 

    def __getattr__(self, key):
        


config = Config()