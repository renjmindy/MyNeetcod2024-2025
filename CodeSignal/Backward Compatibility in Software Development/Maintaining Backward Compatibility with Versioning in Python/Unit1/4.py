import json

# Implement the FileUtility class with versioning support for reading files.
# Use the task description to complete the class implementation.
class FileUtility:
    version = 1  # Default version to 1

    def read_file(self, filepath):
        if self.version == 1:
            return self.read_file_v1(filepath)
            #with open(filepath, 'r', encoding='utf-8') as file:
            #    return file.read()
        elif self.version == 2:
            # TODO: Implement condition to call read_file_v2
            #pass
            return self.read_file_v2(filepath)

    @staticmethod
    def read_file_v1(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def read_file_v2(filepath):
        if filepath.endswith('.json'):
            with open(filepath, 'r', encoding='utf-8') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return "Invalid JSON format"
        else:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        # TODO: Implement reading plain text and JSON files
        # For JSON files, the content should be returned as a dictionary
        # For plain text files, the behavior should be the same as read_file_v1
        #pass
