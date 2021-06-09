class Swich:
    def __init__(self, target):
        self.target = target
        self.caseTrue = False
    #Caso o comparador seja igual ao argumento alvo
    #executa a função passada como parametro.
    #Caso essa função tenha argumentos eles são passados
    #como segundo parâmetro, recomento que os argumentos
    #sejam concatenados em uma lisca caso seja mais de um
    #e que a própria função trate essa lista com argumentos
    def case(self, comparer,func, args = None):
        if self.target == comparer:
            if args != None:
                self.caseTrue = True
                func(args)
            else:
                self.caseTrue = True
                func()
    #Caso nenhum dos cases encontre o alvo, a função default
    #será executada, ela deve ser chamada por último
    def default(self, func, args = None):
        if not self.caseTrue:
            if args != None:
                func(args)
            else:
                func()
    

    