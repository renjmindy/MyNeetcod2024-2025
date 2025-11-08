class LogRecordOverflowError(Exception):
    pass

class LogRecord:
    def __init__(self):
        pass

    # TODO: Enhance the log method to support the new features; metadata as dict and tags as list of strings.
    # Remember to handle the case where the overall log message might exceed 500 characters, raising a custom exception.
    def log(self, message, metadata=None, tags=None):
        if metadata and tags:
            metadata_string = ', '.join([str(k)+'='+str(v) for k, v in metadata.items()])
            tags_string = ', '.join([tag for tag in tags])
            log_message = f"Message: {message}; Metadata: {metadata_string}; Tags: {tags_string}"
        elif metadata:
            metadata_string = ', '.join([k+'='+v for k, v in metadata.items()])
            log_message = f"Message: {message}; Metadata: {metadata_string}"
        elif tags:
            tags_string = ', '.join([tag for tag in tags])
            log_message = f"Message: {message}; Tags: {tags_string}"
        else:
            log_message = f"Message: {message}"
                        
        if len(log_message) > 500:
            raise LogRecordOverflowError("Log record exceeds 500 characters.")
        
        return log_message
