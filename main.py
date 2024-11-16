from scan import Scan;import argparse;from rich.console import Console;console = Console()
accounts = [
    "      [#ff0066][/#ff0066]    ",
    "X / Twitter : [[#ff00ff]0x4161[/#ff00ff]]    ",
    "YouTube :     [[#ff33cc]0x4168[/#ff33cc]]    ",
    "InstaGram :   [[#ff66b2]FX_PY3[/#ff66b2]]    ",  
    "TeleGram :    [[#ff3399]ZeroX4168[/#ff3399]] ",  
    "GitHub :      [[#ff0066]0x4168[/#ff0066]]    ",
]
lines = [
    "[#ff00ff]███╗   ██╗███████╗████████╗   ███████╗ ██████╗ █████╗ ███╗   ██╗[/#ff00ff]",
    "[#ff1aeb]████╗  ██║██╔════╝╚══██╔══╝   ██╔════╝██╔════╝██╔══██╗████╗  ██║[/#ff1aeb]",
    "[#ff33d6]██╔██╗ ██║█████╗     ██║█████╗███████╗██║     ███████║██╔██╗ ██║[/#ff33d6]",
    "[#ff4dc2]██║╚██╗██║██╔══╝     ██║╚════╝╚════██║██║     ██╔══██║██║╚██╗██║[/#ff4dc2]",
    "[#ff66ad]██║ ╚████║███████╗   ██║      ███████║╚██████╗██║  ██║██║ ╚████║[/#ff66ad]",
    "[#ff8099]╚═╝  ╚═══╝╚══════╝   ╚═╝      ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝[/#ff8099]",""]

for account, line in zip(accounts, lines):
    console.print(f"{account:<50} {line}")
print("\n\n")
parser = argparse.ArgumentParser();parser.add_argument("-ho","--host", type=str);parser.add_argument("-f","--file", type=str);args = parser.parse_args()
if args.host:Scan(str(args.host))
elif args.file:Scan(file=args.file)
else:Scan(str("127.0.0.1"))