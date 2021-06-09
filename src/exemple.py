from SwichCase import Swich

while(True):
    #Entrada do usuario
    inp = input("Digite um nome: ")
    s = Swich(inp.lower())
    #Caso o nome que o usuario digitou seja algum desses, eh mostrado na tela.
    s.case("marcos", print, "Você disse Marcos")
    s.case("jhon", print, "Você disse Jhon")
    s.case("bruno", print, "Você disse bruno")
    
    #Caso o nome que o usuario digitou nao seja nenhum dos nomes acima, uma funcao padrao eh acionada
    s.default(print, "Nenhum nome correspondente a pesquisa")
    if inp == "0":
        break
