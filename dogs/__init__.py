from dogs.canyon.neuron6 import Neuron6Dog
from dogs.canyon.neuron_cf7 import NeuronCF7Dog
from dogs.canyon.spectral6 import Spectral6Dog
from dogs.canyon.spectral_cf7 import SpectralCF7Dog
from dogs.dog import Dog

DOGS: tuple[type[Dog], ...] = (Neuron6Dog, NeuronCF7Dog, Spectral6Dog, SpectralCF7Dog)
