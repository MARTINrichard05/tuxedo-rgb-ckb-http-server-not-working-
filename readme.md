it is a project that aims to provide more possibilities for the tuxedo laptop's rgb keyboard

i'm a beginner but , i love to learn

for now it is a bit in scratch state and keyborad.py needs to have admin rights so for now the best way to run it is by doing : 

sudo python start.py

for now it is not a realy stable solution

just send an get http request like that:
http://127.0.0.1:6670/[r,g,b]

r g and b between 0 and 255

use install.sh to install the server



// legacy files not recomanded
modes :

0   : only one custom color
1   : rgb rainbow like everyone likes
2   : switching colors without transitions
3   : i'm gona try to put transitions to the 2
4   : read rgb values (0-255) from rgb_rt
function name in the custom.py file

customs functions : 

they are called every time the leds have to refresh and all they need to do is return [r,g,b] values