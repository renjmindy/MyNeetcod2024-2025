class ConfigParser:
    # TODO: Enhance the ConfigPartser class to support type-sensitive parsing
    # of integers, floats, and booleans while maintaining backward compatibility.
    def _parse_value(self, value):
        if value.lower() == 'true': return True
        elif value.lower() == 'false': return False
        else:
            try:
                return int(value)
            except ValueError:
                try:
                    return float(value)
                except ValueError:
                    return value

    def parse(self, file_path, type_sensitive=False):
        self.config = {}
        if not type_sensitive:
            with open(file_path, 'r') as file:
                for line in file:
                    key, value = line.strip().split('=')
                    self.config[key] = value  # All values are treated as strings
            return self.config
        else:
            with open(file_path, 'r') as file:
                for line in file:
                    key, value = line.strip().split('=')
                    self.config[key] = self._parse_value(value)
            return self.config
