from colorama import init, Fore, Back, Style

# Initialize colorama
init()

# Print colorful Hello World
print(f"{Fore.YELLOW}Hello {Fore.BLUE}World!{Style.RESET_ALL}")
print(f"{Back.YELLOW}{Fore.BLACK}Welcome to the colorful world of Python!{Style.RESET_ALL}")
print(f"{Fore.CYAN}This is an enhanced version of Hello World!{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}Enjoy the colors!{Style.RESET_ALL}") 