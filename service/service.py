import threading


class Service:
    def __init__(self):
        self.threadRun = False

    def start(self):
        self.threadRun = True
        threading.Thread(target=self.__run).start()

    def stop(self):
        self.threadRun = False

    def __run(self):
        while self.threadRun:
            self.run()

    def run(self):
        self.stop()
        raise Exception('未实现 service 的 run 函数')
