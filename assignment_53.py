'''
What is the output?
'''

class Logger:
    def log(self, message):
        print(f"Log: {message}")

class AdvancedLogger(Logger):
    def log(self, message):
        super().log(message)
        print(f"Advanced Log: {message}")

logger = AdvancedLogger()
logger.log("System error")


# Output:

# Log: System error
# Advanced Log: System error
