from SwichCase import Swich

while(True):
    inp = input("Digite um nome: ")
    s = Swich(inp.lower())
    s.case("marcos", print, "Você disse Marcos")
    s.case("jhon", print, "Você disse Jhon")
    s.case("bruno", print, "Você disse bruno")
    s.default(print, "Nenhum nome correspondente a pesquisa")
    if inp == "0":
        break
