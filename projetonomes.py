import os
import sys
import time

try:
    from colorama import Fore, Style, init
except ImportError:
    print("\n📥 Instalando a biblioteca 'colorama'...\n")
    os.system(f"{sys.executable} -m pip install colorama")
    print("\n✅ Instalação concluída! Continuando o programa...\n")
    from colorama import Fore, Style, init

init(autoreset=True)

arte_inicial = f'''
{Fore.LIGHTGREEN_EX}⚡⚡ Poison_OktavZZ ⚡⚡
'''

print(arte_inicial)
print(Fore.RED + "\nIniciando o código", end="", flush=True)
for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)
print(Fore.RED + "\n")

print(Fore.RED + "\n✏️  Digite a mensagem que será enviada após o nome da pessoa:")
mensagem_base = input("> ").strip()

print(Fore.RED + "\n👤 Digite os nomes das pessoas separados por vírgula:")
nomes = input("> ").strip()

lista_nomes = [nome.strip() for nome in nomes.split(",")]

print(Fore.RED + "\n" + Fore.GREEN + "="*50)
print(Fore.YELLOW + " MENSAGENS GERADAS ".center(50, "="))
print(Fore.GREEN + "="*50 + "\n")

for nome in lista_nomes:
    nome_formatado = f"{Fore.CYAN}{nome}{Style.RESET_ALL}"
    mensagem_final = f"Olá {nome_formatado}, {mensagem_base}"

    print(Fore.RED + "\n" + "-"*50)
    print(f"\n📩 Mensagem para: {nome_formatado}\n")
    print(Fore.WHITE + mensagem_final)
    print(Fore.RED + "\n" + "-"*50)

    input(Fore.RED + "\n🔽 Pressione Enter para continuar...\n")

print(Fore.WHITE + "\n✅ Todas as mensagens foram exibidas. Programa finalizado.\n")

arte_final = f'''
{Fore.LIGHTGREEN_EX}⚡⚡ Poison_OktavZZ ⚡⚡
Obrigado por utilizar meu código! Levi manda abraços.
'''

print(arte_final)