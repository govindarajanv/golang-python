class Handler:

    def handle(self, message):
        pass

class InfoHandler(Handler):

    def __init__(self, next):
        self.next = next

    def handle(self, message):
        if message.startswith("info"):
            print("!! INFO !!", message)
        else:
            self.next.handle(message)

class ErrorHandler(Handler):

    def __init__(self, next):
        self.next = next

    def handle(self, message):
        if message.startswith("error"):
            print("XX ERROR XX", message)
        else:
            self.next.handle(message)

class FailureHandler(Handler):

    def __init__(self, next):
        self.next = next

    def handle(self, message):
        if message.startswith("failure"):
            print("** FAILURE **", message)
        else:
            self.next.handle(message)

class Logger:

    def __init__(self):
        failureHandler = FailureHandler(None)
        errorHandler = ErrorHandler(failureHandler)
        infoHandler = InfoHandler(errorHandler)
        self.handler = infoHandler

    def log(self, message):
        self.handler.handle(message)
if __name__ == "__main__":
    logger = Logger()
    logger.log("failure - message 1")
    logger.log("info - message 2")
    logger.log("error - message 3")