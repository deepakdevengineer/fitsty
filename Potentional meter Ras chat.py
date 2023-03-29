from  gpiozero import MCP3008
from time import sleep
import matplotlib.pyplot as plt
pot=MCP3008(7)

while True:
    print(pot.value * 100)
    sleep(1)
    
data  =  {
         "x"  : [i for i in range(1,10)],
         "y"  : [(100)]
         }
plt.scatter(
       data["x"],
       data["y"],
       marker ="o",
       markersize="4"
       )

plt.show()
plt.title("Potantial")
plt.xlabel("")
plt.xlabel("")

