import requests
import os
from lxml import html
from googlesearch import search

# Função para visualizar o menu

query_list = []
visible_list = []

def show_menu():
    print('1. Procurar por páginas que tem um determinado termo na URL')
    print('2. Procurar por páginas que tem um determinado termo no título')
    print('3. Procurar por páginas que tem um determinado termo no texto')
    print('4. Procurar em um determinado site')
    print('5. Procurar por um determinado tipo de arquivo (ex: pdf, docx, jpg, xls, etc)')
    print('')
    print('0. Pesquisar')
    print()

def google_hacking(query, amount): 
    # Realizar a busca no google
    results = search(query, num=20, stop=amount, pause=2) 

    f = open("links.txt", "w+")
    
    
    for result in results: 
        print(result)
        f.write(result + '\n') 
        f.write('\n')
   
    f.close()

def main():
    while 1:
        for i in range(len(visible_list)):
                    print(visible_list[i])
        print(' ')
        pesquisa_final = ""
        for i in range(len(query_list)):
            if pesquisa_final != "":
                pesquisa_final += ' ' + query_list[i]
            else:
                pesquisa_final += query_list[i]
        print(pesquisa_final)
        print(' ')
        show_menu()
        choice = input('Escolha a opção desejada: ')
        if choice == '1':
            while 1:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print('Status: ')
                for i in range(len(visible_list)):
                    print(visible_list[i])
                print(' ')
                print('1. Adicionar um termo')
                print('2. Voltar')
                print(' ')
                choice = input("Escolha a opção desejada: ")
                if choice == '1':
                    termo = input("Digite um termo: ")
                    visible_list.append("Procurar por um determinado termo na URL: " + termo)
                    query_list.append('inurl:"' + termo + '"')
                elif choice == '2':
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    break
        elif choice == '2':
            while 1:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print('Status: ')
                for i in range(len(visible_list)):
                    print(visible_list[i])
                print(' ')
                print('1. Adicionar um termo')
                print('2. Voltar')
                print(' ')
                choice = input("Escolha a opção desejada: ")
                if choice == '1':
                    termo = input("Digite um termo: ")
                    visible_list.append("Procurar por um determinado termo no título: " + termo)
                    query_list.append('intitle:"' + termo + '"')
                elif choice == '2':
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    break
        elif choice == '3':
            while 1:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print('Status: ')
                for i in range(len(visible_list)):
                    print(visible_list[i])
                print(' ')
                print('1. Adicionar um termo')
                print('2. Voltar')
                print(' ')
                choice = input("Escolha a opção desejada: ")
                if choice == '1':
                    termo = input("Digite um termo: ")
                    visible_list.append("Procurar por um determinado termo no texto: " + termo)
                    query_list.append('intext:"' + termo + '"')
                elif choice == '2':
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    break
        elif choice == '4':
            while 1:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print('Status: ')
                for i in range(len(visible_list)):
                    print(visible_list[i])
                print(' ')
                print('1. Adicionar um site')
                print('2. Voltar')
                print(' ')
                choice = input("Escolha a opção desejada: ")
                if choice == '1':
                    termo = input("Digite um termo: ")
                    visible_list.append("Procurar em um determinado site: " + termo)
                    query_list.append('site:"' + termo + '"')
                elif choice == '2':
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    break
        elif choice == '5':
            while 1:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print('Status: ')
                for i in range(len(visible_list)):
                    print(visible_list[i])
                
                print(' ')
                print('1. Adicionar um termo')
                print('2. Voltar')
                print(' ')
                choice = input("Escolha a opção desejada: ")
                if choice == '1':
                    termo = input("Digite um termo: ")
                    visible_list.append("Procurar por um determinado tipo de arquivo (ex: pdf, docx, jpg, xls, etc): " + termo)
                    query_list.append('filetype:"' + termo + '"')
                elif choice == '2':
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    break
        elif choice == '0':
            os.system('cls' if os.name == 'nt' else 'clear') 
            google_hacking(pesquisa_final, 40)
            break
        else:
            print('Opção inválida, tente novamente.')
        

main()
