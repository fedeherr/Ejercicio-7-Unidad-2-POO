class Hora:
    __hora = 0
    __minutos = 0
    __segundos = 0
    def __init__(self, hora = 0, minutos = 0, segundos = 0):
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos
    def Mostrar(self):
        return "Hora: %d:%d:%d" % (self.__hora, self.__minutos, self.__segundos)
    def gethora(self):
        return self.__hora
    def getminutos(self):
        return self.__minutos
    def getsegundos(self):
        return self.__segundos