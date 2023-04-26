from os import system as sy
sy("apt update && apt list --upgradeable && apt upgrade -y")
print("You are now working on a completely updated platform!!!")
