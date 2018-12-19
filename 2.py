import numpy as np
from pprint import pprint

E = [1., 1., 1, 1]
beta = [0, (90 * np.pi / 180), (180 * np.pi / 180), (270 * np.pi / 180)]
theta = [(4 * np.pi / 180), (4 * np.pi / 180), (4 * np.pi / 180), (4 * np.pi / 180)]
gamma = [np.pi / 2., np.pi / 2., np.pi / 2., np.pi / 2.]
parametrywiazek = [E, beta, theta, gamma]

pprint(parametrywiazek)
print('\n')


def obliczeniewektorak(beta=beta, theta=theta)->[int]:
    k = np.array(
        [np.sin(theta) * np.allclose(np.cos(beta), 0), np.sin(theta) * np.allclose(np.sin(beta), 0), -np.cos(theta)])
    k *= (np.pi * 2 / 0.532)
    return k


def obliczeniepolaryzacji(beta=beta, theta=theta, gamma=gamma)-> np.array(int):
    p: np.array = [
        np.allclose(np.cos(theta) * np.cos(beta) * np.cos(gamma) - np.sin(beta) * np.sin(gamma), 0),
        np.allclose(np.cos(theta) * np.sin(beta) * np.cos(gamma) + np.cos(beta) * np.sin(gamma), 0),
        np.sin(theta) * np.cos(gamma)
    ]
    return p


wektoryk = [
    obliczeniewektorak(beta=beta[0], theta=theta[0]),
    obliczeniewektorak(beta=beta[1], theta=theta[1]),
    obliczeniewektorak(beta=beta[2], theta=theta[2]),
    obliczeniewektorak(beta=beta[3], theta=theta[3]),
]
pprint(wektoryk)
print('\n')

wersoryp = [
    obliczeniepolaryzacji(beta=beta[0], theta=theta[0], gamma=gamma[0]),
    obliczeniepolaryzacji(beta=beta[1], theta=theta[1], gamma=gamma[1]),
    obliczeniepolaryzacji(beta=beta[2], theta=theta[2], gamma=gamma[2]),
    obliczeniepolaryzacji(beta=beta[3], theta=theta[3], gamma=gamma[3])
]
pprint(wersoryp)
