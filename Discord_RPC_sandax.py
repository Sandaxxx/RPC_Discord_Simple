import time
from colorama import init, Fore, Back, Style
init()
from pypresence import Presence


# ID OF APPLICATION DEVELOPPER PORTAL DISCORD (https://discord.com/developers/applications/) 
ClientID = 'YOUR ID APPLICATION'

RPC = Presence(ClientID) 
RPC.connect() # CONNECTION 

print(Fore.BLUE+"[♠] "+Fore.WHITE+"> "+Fore.YELLOW+"Connecting...")
print(Fore.MAGENTA)

print(RPC.update(
    state="Plz Star the project :'(", # Second Text
        details="Dev by Sandax", # First Text
            large_image="Image1", # Big Image 
                 small_image="Image2", # Little image corner right
                     large_text="If u see the message your a bot ", # when your mouse hovers over the large image
                            buttons=[{"label": "Discord", "url": "https://discord.gg"}, {"label": "GitHub 👾", "url": "https://github.com/Sandaxxx/RPC_Discord_Simple"}],

    start=time.time()))
print()

# CONNECT VALID
print(Fore.BLUE+"[♠] "+Fore.WHITE+"> "+Fore.GREEN+'Success Connections ')

# ON THE RPC ALL TIME
while True: 
    time.sleep(50) 
