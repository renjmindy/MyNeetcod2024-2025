import re
import json

class Printer:
    def print_content(self, content, content_type='plain'):
        if content_type == 'plain': print(content)
        elif content_type == 'html':
            text = re.sub('<[^<]+?>', '', content) 
            print(text)
        elif content_type == 'json':
            parsed = json.loads(content) 
            print(json.dumps(parsed, indent=4, sort_keys=True))
        else: 
            raise ValueError("an unsupported type is passed")
    
    # TODO: Extend the Printer class to support HTML content. Strip HTML tags before printing.
    # TODO: Add support for printing JSON content in a pretty format.
