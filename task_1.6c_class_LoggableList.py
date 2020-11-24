class LoggableList(Loggable, list):
    def append(self, value):
        super(LoggableList, self).append(value)
        self.log(value)
