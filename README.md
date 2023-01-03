# __RPC_Discord_Simple__

**Just a Rich Presence Discord to create a personalized activity for you with an easy-to-use module. Have fun 😋**
![background](https://cdn.discordapp.com/attachments/1047918302841798718/1059953539067158538/image.png)

# __INSTALLATION__
>### [Developper Portal](https://discord.com/developers/applications/) (Create Application)
>## ```pip install pastebinapi```


# EXEMPLE
```py
from pypresence import Presence
import time

client_id = '123456789123'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

print(RPC.update(state="Lookie Lookie", details="A test of qwertyquerty's Python Discord RPC wrapper, pypresence!"))  # Set the presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds
```

## __Build__
* [Pypresence](https://pypi.org/project/pypresence/)
* [Python](https://www.python.org/)
