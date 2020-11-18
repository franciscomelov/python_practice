# https://platzi.com/comunidad/platzicodingchallenge-dia-3-reloj/


def en_segundos(h, m):
    seg = h*60**2   #convertir horas a segundos  60**2  == 60 *60
    seg += m *60    #convertir minutos a segundos y sumando
    print(seg)


if __name__ == "__main__":
    h = 20   # Horas
    m = 20   # Minutos
    en_segundos(h,m)