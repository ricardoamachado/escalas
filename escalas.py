def montar_escala(indice_tonica,lista_notas,lista_intervalos):
    """ 
    Retorna uma lista com as notas da escala musical desejada.
    Parâmetros:
    indice_tonica : int
        Refere-se ao índice da tônica na lista_notas.
    lista_notas : list str
        Representa a lista com as notas musicais.
    lista_intervalos: list int
        Representa a lista com os intervalos da escala musical desejada.
        0: Representa tônica.
        1: Representa semitom.
        2: Representa um tom.
    """
    lista_escala = []
    indice_escolhido = indice_tonica
    for num in lista_intervalos:
        indice_escolhido += num
        indice_escolhido = indice_escolhido % 12 
        lista_escala.append(lista_notas[indice_escolhido])


    return lista_escala
def main():
    # N = Tônica, T = Tom, ST = Semitom.
    # Notação para escalas: 0 = N, 1 = ST, 2 = T.
    notas = ['A', 'Bb/A#', 'B', 'C', 'Db/C#', 'D', 'Eb/D#', 'E', 'F', 'Gb/F#', 'G','Ab/G#']
    intervalos_escala_maior = [0,2,2,1,2,2,2,1]
    intervalos_escala_menor_natural = [0,2,1,2,2,1,2,2]
    intervalos_escala_menor_harmonica = [0,2,1,2,2,1,3,1]
    intervalos_escala_menor_melodica = [0,2,1,2,2,2,2,1]
    intervalos_escala_dominante = [0,2,2,1,2,2,1,2]
    print("Qual a tônica da sua escala ?")
    for i in range(0,12):
        print(f"Digite {i} para {notas[i]}")
    while True:
        try:
            tonica = int(input())
            break
        except:
            print("Entrada Inválida, Tente Novamente.")
    print("Qual a escala desejada ?")
    print("Digite 0 para Escala Maior \nDigite 1 para Escala Menor Natural \nDigite 2 para Escala Menor Harmônica \nDigite 3 para Escala Menor Melôdica \nDigite 4 para Escala Dominante")
    while True:
        try:
            num_escala = int(input())
            break
        except:
            print("Entrada Inválida, Tente Novamente.")
    if num_escala not in [0,1,2,3,4]:
        print("Entrada Inválida, Mostrando Escala Dominante.")
    if num_escala == 0:
        print(montar_escala(tonica,notas,intervalos_escala_maior))
    elif num_escala == 1:
        print(montar_escala(tonica,notas,intervalos_escala_menor_natural))
    elif num_escala == 2:
        print(montar_escala(tonica,notas,intervalos_escala_menor_harmonica))
    elif num_escala == 3:
        print(montar_escala(tonica,notas,intervalos_escala_menor_melodica))
    else:
        print(montar_escala(tonica,notas,intervalos_escala_dominante))

main()
# for i in range(0,12):
#     print(montar_escala(i,notas,intervalos_escala_menor_melodica))
#     print(f"i={i}")