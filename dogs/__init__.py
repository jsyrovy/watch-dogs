from dogs.canyon.spectral6 import Spectral6Dog
from dogs.canyon.spectral_cf7 import SpectralCF7Dog
from dogs.dog import Dog

DOGS: tuple[type[Dog], ...] = (Spectral6Dog, SpectralCF7Dog)
