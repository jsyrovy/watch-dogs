from dogs.canyon.neuron6 import Neuron6Dog
from dogs.canyon.neuron_cf7 import NeuronCF7Dog
from dogs.dog import Dog

DOGS: tuple[type[Dog], ...] = (Neuron6Dog, NeuronCF7Dog)
