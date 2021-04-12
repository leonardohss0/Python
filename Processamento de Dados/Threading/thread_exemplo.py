import threading

class Fatorizador(threading.Thread):
    def __init__(self, num, **kwargs):
        super(Fatorizador, self).__init__(**kwargs)
        self.__num = num
        self.__results = None

    def run(self):
        self.__results = []
        for i in range(1, self.__num):
            if self.__num % i == 0:
                self.__results.append(i)

    def get_results(self):
        return [i for i in self.__results]


def main():
    f = Fatorizador(1929921)
    f.start()
    f.join()

    print(f.get_results())

if __name__ =='__main__':
    main()