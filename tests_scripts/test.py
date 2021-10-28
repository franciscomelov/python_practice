class CasillaDeVotacion:
    def __init__(self, identificador, pais):
        self.__identificador=identificador
        self.__pais=pais
        self.__region=None

    # gettler  con la notacion de codorador

    # decorador y su dot notation
    @property
    def region(self):
        return self.__region

    @region.setter  # nos permite modificar
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La reegion {region} no es vakuda en {self.__pais}')


if __name__ == '__main__':
    casilla = CasillaDeVotacion(123, ['ciudad de mexico', 'Morelos'])
    print(casilla.region)
    casilla.region = 'Ciudad de mexico'
    print(casilla.region)