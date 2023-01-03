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
    state="𝗖𝗵𝗲𝗰𝗸 𝗠𝘆 𝗚𝗶𝘁𝗛𝘂𝗯 🚀", # Second Text
        details="𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗽𝗲𝗱 𝗕𝘆 𝗦𝗮𝗻𝗱𝗮𝘅#𝟯𝟵𝟴𝟰 💻", # First Text
            large_image="sandaxpick", # Big Image 
                 small_image="piquesmall", # Little image corner right
                     large_text="Follow twitch vu que tu vois ça 🕵️‍♂️", # when your mouse hovers over the large image
                            buttons=[{"label": "Discord 🌴", "url": "https://discord.gg/mDdGhkRSXx"}, {"label": "GitHub 👾", "url": "https://github.com/Sandaxxx"}],

    start=time.time()))
print()

# CONNECT VALID
print(Fore.BLUE+"[♠] "+Fore.WHITE+"> "+Fore.GREEN+'Success Connections ')

# ON THE RPC ALL TIME
while True: 
    time.sleep(50) 
