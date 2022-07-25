class ReproductorMusica:
    version_firmware = 1.0
    def __init__(self):
        self.__lista_reproduccion=["Te Felicito","Formentera","Tacones Rojos","Ateo","Loco"]
        self.cancion_actual = None


    def play(self):
        self.cancion_actual=self.__lista_reproduccion[0]
        

    def listar_canciones(self):
        return self.__lista_reproduccion

    @classmethod
    def actualizar_firmware(cls, nueva_version):
        if nueva_version > cls.version_firmware:
            cls.version_firmware = nueva_version
        


ipod=ReproductorMusica()
ipod.play()
print(f"canción actual: {ipod.cancion_actual}")
ipod.play()
print(f"canción actual: {ipod.cancion_actual}")

print(f"lista de reproduccion: {ipod.listar_canciones()}")

print(f"version actual: {ipod.version_firmware}")
ipod.actualizar_firmware(2.0)
print(f"version actual: {ipod.version_firmware}")
