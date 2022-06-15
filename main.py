import json


def menu():
    print("\nUtilize os seguintes comandos para a utilização do sistema:")
    print("2 - Para selecionar a questão 2, que retorna se um número está contido na sequência de Fibonacci criada")
    print("3 - Para selecionar a questão 3, que retorna dados referentes ao faturamento diário de uma distribuidora")
    print("4 - Para selecionar a questão 4, que calcula o percentual de representação que cada estado teve dentro do "
          "valor total mensal da distribuidora.")
    print("5 -  Para selecionar a questão 5, que inverte os caracteres de um string")
    print("Ou digite qualquer outro valor para sair do programa")
    return input("Digite a opção desejada: ")


def Fibonacci(value):
    seq = [0, 1]
    last = seq[-1]
    penult = seq[-2]

    while last <= value:
        seq.append(last + penult)
        last = seq[-1]
        penult = seq[-2]
    if penult == value:
        return True
    return False


def cleanDict(data):
    j = 0
    for i in range(len(data) - 1):
        j = j + 1
        if data[j]['valor'] == 0.0:
            del data[j]
            j = j - 1

    return data


def resolvProblemsQ3(data):
    smallest = min(data, key=lambda d: d['valor'])
    print(f"O menor valor faturado foi {smallest['valor']}, no dia {smallest['dia']}.")

    biggest = max(data, key=lambda d: d['valor'])
    print(f"O maior valor faturado foi {biggest['valor']}, no dia {biggest['dia']}.")

    # calcula a média
    average = 0
    for value in data:
        average = average + value['valor']
    average = average / len(data)

    i = 0
    for value in data:
        if value['valor'] > average:
            i = i + 1
    print(f"O número de dias no mês em que o valor de faturamento diário foi superior à média mensal é {i}.")


def percent():
    data = [{"state": "SP", "invoicing": 67836.43},
            {"state": "RJ", "invoicing": 36678.66},
            {"state": "MG", "invoicing": 29229.88},
            {"state": "ES", "invoicing": 27165.48},
            {"state": "Outros", "invoicing": 19849.53}]

    total = 0
    for value in data:
        total = total + value['invoicing']

    print("Percentual de participação de cada estado:")
    for value in data:
        print(f"{value['state']}: {round(100 * value['invoicing'] / total)}%")


def invert(string: str):
    listString = []
    for char in string:
        listString.insert(0, char)
    invertedString = ''.join(listString)
    print("Frase invertida:\n", invertedString)


if __name__ == '__main__':

    while True:
        option = menu()

        match option:
            case "2":
                num = input("Informe o número: ")
                result = Fibonacci(int(num))
                print(result)
            case "3":
                # Cria um dicionário a partir de um arquivo JSON
                with open("dados.json") as file:
                    data = json.load(file)
                data = cleanDict(data)  # Retira todos os dias em que o faturamento foi igual a 0
                resolvProblemsQ3(data)
            case "4":
                percent()
            case "5":
                string = input("Insira a frase que deseja ser invertida: ")
                invert(string)
            case default:
                exit()
