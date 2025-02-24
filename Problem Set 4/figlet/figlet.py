from pyfiglet import Figlet
import sys

figlet = Figlet()
if len(sys.argv) == 1:
    str = input("Input: ")
    print(figlet.renderText(str))
elif (
    len(sys.argv) == 3
    and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
    and sys.argv[2] in figlet.getFonts()
):
    str = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(str))
else:
    sys.exit("Invalid usage")
