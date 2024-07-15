from dogs.dog import Dog
from dogs.ikea.smastad_platsa_skrin1 import SmastadPlatsaSkrin1
from dogs.ikea.smastad_platsa_skrin2 import SmastadPlatsaSkrin2
from dogs.ikea.smastad_platsa_sestava import SmastadPlatsaSestava

DOGS: tuple[type[Dog], ...] = (
    SmastadPlatsaSkrin1,
    SmastadPlatsaSkrin2,
    SmastadPlatsaSestava,
)
