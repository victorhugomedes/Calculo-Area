def area_quadrada(): #função para o cálculo da área de um quadrado
    base = float(input("Digite a base:\n"))
    altura = float(input("Digite a altura:\n"))
    
    area = base * altura
    print(f"A área desse quadrado é: {area:.2f}\n")

def area_triangulo(): #função para o cálculo de um triangulo
    base = float(input("Digite a base:\n"))
    altura = float(input("Digite a altura:\n"))
    
    area = (base * altura) / 2
    print(f"A área desse triângulo é: {area:.2f}\n")

def area_retangulo(): #função para o cálculo de um retangulo
    base = float(input("Digite a base:\n"))
    altura = float(input("Digite a altura:\n"))
    
    area = base * altura
    print(f"A área desse retângulo é: {area:.2f}\n")

def main():
    opcao = 1
    
    while opcao != 0: #laço do menu 
        print("Escolha de qual área você gostaria de calcular:")
        print("Digite '1' caso queira o cálculo da área do quadrado!")
        print("Digite '2' caso queira o cálculo da área do triângulo!")
        print("Digite '3' caso queira o cálculo da área do retângulo!")
        print("Digite '0' caso queira sair do programa!")
        
        opcao = int(input("Escolha o recurso que irá utilizar:\n"))
        
        if opcao == 0:
            print("Você escolheu sair do programa!")
        elif opcao == 1:
            area_quadrada()
        elif opcao == 2:
            area_triangulo()
        elif opcao == 3:
            area_retangulo()
        else:
            print("Opção inválida, tente novamente!")

if __name__ == "__main__":
    main()
