import base64
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

def print_banner():

    banner = rf"""
    {Fore.CYAN} /$$$$$$$   /$$$$$$  /$$   /$$ {Fore.YELLOW}
    {Fore.CYAN}| $$__  $$ /$$__  $$| $$  | $$ {Fore.YELLOW}
    {Fore.CYAN}| $$  \ $$| $$  \__/| $$  | $$ {Fore.YELLOW}
    {Fore.CYAN}| $$$$$$$ | $$$$$$$ | $$$$$$$$ {Fore.YELLOW}
    {Fore.CYAN}| $$__  $$| $$__  $$|_____  $$ {Fore.YELLOW}
    {Fore.CYAN}| $$  \ $$| $$  \ $$      | $$ {Fore.YELLOW}
    {Fore.CYAN}| $$$$$$$/|  $$$$$$/      | $$ {Fore.YELLOW}
    {Fore.CYAN}|_______/  \______/       |__/ {Fore.YELLOW}
    """

    print(banner)
    print(f"{Fore.GREEN}Bienvenido al programa de Encode/Decode en Base64")
    print(f"{Fore.MAGENTA}Creado por: Folkencillo\n")

def encode_to_base64(text):
    """
    Codifica una cadena de texto en Base64.
    :param text: Cadena de texto a codificar.
    :return: Cadena codificada en Base64.
    """
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    base64_text = base64_bytes.decode('utf-8')
    return base64_text

def decode_from_base64(base64_text):
    """
    Decodifica una cadena Base64 a texto plano.
    :param base64_text: Cadena Base64 a decodificar.
    :return: Cadena de texto decodificada.
    """
    try:
        base64_bytes = base64_text.encode('utf-8')
        text_bytes = base64.b64decode(base64_bytes)
        text = text_bytes.decode('utf-8')
        return text
    except Exception as e:
        return f"{Fore.RED}Error al decodificar: {e}"

def main():
    print_banner()
    while True:
        print(f"\n{Fore.YELLOW}Seleccione una opción:")
        print(f"{Fore.CYAN}1. Codificar (Encode) a Base64")
        print(f"{Fore.CYAN}2. Decodificar (Decode) desde Base64")
        print(f"{Fore.CYAN}3. Salir")
        
        opcion = input(f"{Fore.GREEN}Ingrese su opción (1/2/3): ")
        
        if opcion == "1":
            texto = input(f"{Fore.WHITE}Ingrese el texto a codificar: ")
            resultado = encode_to_base64(texto)
            print(f"\n{Fore.GREEN}Texto codificado en Base64:\n{Fore.YELLOW}{resultado}")
        
        elif opcion == "2":
            texto_base64 = input(f"{Fore.WHITE}Ingrese el texto Base64 a decodificar: ")
            resultado = decode_from_base64(texto_base64)
            print(f"\n{Fore.GREEN}Texto decodificado:\n{Fore.YELLOW}{resultado}")
        
        elif opcion == "3":
            print(f"{Fore.RED}Saliendo del programa...")
            break
        
        else:
            print(f"{Fore.RED}Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()