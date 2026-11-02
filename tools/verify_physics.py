"""Independent numerical checks of the answer keys (integrals, matrices, direct solves), separate from the algebra."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

pi = np.pi
results = []


def check(name, got, want, tol=1e-5):
    ok = abs(got - want) <= tol * max(1, abs(want))
    results.append(ok)
    print(("ok  " if ok else "FAIL"), name, f"got={got:.6g} want={want:.6g}")


def I(f, a, b):
    return quad(f, a, b, limit=400)[0]


# Infinite well (a=1)
psi = lambda n, x: np.sqrt(2) * np.sin(n * pi * x)
check("<1|x|2>", I(lambda x: psi(1, x) * x * psi(2, x), 0, 1), -16 / (9 * pi**2))
for n, want in ((1, 8 / pi**2), (2, 0), (3, 8 / (9 * pi**2))):
    check(f"uniform P{n}", I(lambda x: psi(n, x), 0, 1) ** 2, want)

# Polynomial state x(1-x)
N2 = 1 / I(lambda x: (x * (1 - x)) ** 2, 0, 1)
check("poly N^2", N2, 30)
check("poly <p^2>", N2 * I(lambda x: (1 - 2 * x) ** 2, 0, 1), 10)
ex = N2 * I(lambda x: x * (x * (1 - x)) ** 2, 0, 1)
ex2 = N2 * I(lambda x: x**2 * (x * (1 - x)) ** 2, 0, 1)
check("poly var x", ex2 - ex**2, 1 / 28)

# Oscillator from truncated matrices, hbar=m=omega=1, with l^2=1/2
d = 60
a = np.diag(np.sqrt(np.arange(1, d)), 1)
ad = a.T
x = (a + ad) / np.sqrt(2)
p = 1j * (ad - a) / np.sqrt(2)
check("<1|x^2|1>", (x @ x)[1, 1], 1.5)
check("<3|x|2>", x[3, 2], np.sqrt(1.5))
check("<0|x^4|0>", np.linalg.matrix_power(x, 4)[0, 0], 3 * 0.25)
check("<0|x^6|0>", np.linalg.matrix_power(x, 6)[0, 0], 15 * 0.125)
comm = a @ a @ ad @ ad - ad @ ad @ a @ a
check("[a^2,ad^2] n=3", comm[3, 3], 4 * 3 + 2)
s = np.zeros(d, complex); s[0] = s[1] = 1 / np.sqrt(2)
for t in (0.0, 0.7):
    st = s * np.exp(-1j * (np.arange(d) + 0.5) * t)
    check(f"<x>({t})", (st.conj() @ x @ st).real, np.sqrt(0.5) * np.cos(t))
    check(f"<p>({t})", (st.conj() @ p @ st).real, -np.sqrt(0.5) * np.sin(t))
st = s
check("Delta x^2 (0+1)", (st.conj() @ x @ x @ st).real - (st.conj() @ x @ st).real ** 2, 0.5)

# Sudden displacement: overlap of displaced Gaussians (b=1, x0=0.8)
phi0 = lambda x: pi**-0.25 * np.exp(-x * x / 2)
check("displaced overlap^2", I(lambda x: phi0(x) * phi0(x - 0.8), -12, 12) ** 2, np.exp(-0.64 / 2))

# Mystery potential psi=x exp(-x^2/2): a finite-difference eigenproblem for V=x^2/2 in hbar=m=b=1
xs = np.linspace(-9, 9, 1801); h = xs[1] - xs[0]
H = np.diag(1 / h**2 + xs**2 / 2) - np.diag(np.ones(1800), 1) / (2 * h**2) - np.diag(np.ones(1800), -1) / (2 * h**2)
ev = np.linalg.eigvalsh(H)
check("mystery E (1st excited)", ev[1], 1.5, 1e-3)
# Half oscillator: odd states only
check("half-oscillator 1st excited", ev[3], 3.5, 1e-3)

# Finite well count, half well
def count_even_odd(z0):
    return int(np.ceil(2 * z0 / pi))
check("z0=7 count", count_even_odd(7), 5)
check("z0=2 count", count_even_odd(2), 2)

# Delta plus wall with hbar=m=1, alpha=1: threshold L=1/2
f = lambda k, L: k * (1 + 1 / np.tanh(k * L)) - 2
check("delta-wall: no state at L=0.4", float(all(f(k, 0.4) > 0 for k in np.linspace(.001, 5, 500))), 1)
check("delta-wall: state at L=0.6", float(any(f(k, 0.6) < 0 for k in np.linspace(.001, 5, 500))), 1)
check("delta-wall L=large kappa", brentq(lambda k: f(k, 40.0), .1, 5), 1.0)

# Two deltas: splitting for large L
kp = brentq(lambda k: k - (1 + np.exp(-2 * k * 6)), .5, 2)
km = brentq(lambda k: k - (1 - np.exp(-2 * k * 6)), .5, 2)
check("two-delta splitting", kp**2 - km**2, 4 * np.exp(-12), 2e-2)


def transmission_well(E, V0, a):
    """Direct 4x4 solve of the well's boundary conditions, hbar=2m=1."""
    k = np.sqrt(E); q = np.sqrt(E + V0)
    M = np.array([
        [-np.exp(1j * k * a), np.exp(-1j * q * a), np.exp(1j * q * a), 0],
        [1j * k * np.exp(1j * k * a), 1j * q * np.exp(-1j * q * a), -1j * q * np.exp(1j * q * a), 0],
        [0, np.exp(1j * q * a), np.exp(-1j * q * a), -np.exp(1j * k * a)],
        [0, 1j * q * np.exp(1j * q * a), -1j * q * np.exp(-1j * q * a), -1j * k * np.exp(1j * k * a)],
    ])
    b = np.array([np.exp(-1j * k * a), 1j * k * np.exp(-1j * k * a), 0, 0])
    return abs(np.linalg.solve(M, b)[3]) ** 2


E, V0, a_ = 1.3, 4.0, 0.9
check("well T formula", transmission_well(E, V0, a_), 1 / (1 + V0**2 * np.sin(2 * np.sqrt(E + V0) * a_) ** 2 / (4 * E * (E + V0))))

# Reflection delay: numerically differentiate the phase of r at E=V0/2 (hbar=m=1, so E=k^2/2)
V = 2.0
phase = lambda E: np.angle((np.sqrt(2 * E) - 1j * np.sqrt(2 * (V - E))) / (np.sqrt(2 * E) + 1j * np.sqrt(2 * (V - E))))
dE = 1e-5
check("step delay", (phase(1 + dE) - phase(1 - dE)) / (2 * dE), 2 / V, 1e-4)

# Delta next to wall, direct log-derivative check of the phase
k, L, beta = 1.0, pi / 2, 1.0
delta = -pi / 4
A = np.sin(k * L + delta) / np.sin(k * L)
check("delta-wall jump", k * np.cos(k * L + delta) - A * k * np.cos(k * L), beta * A * np.sin(k * L))

# Hydrogen with a0=1
u10 = lambda r: 2 * r * np.exp(-r)
u20 = lambda r: 2 * r / 2**1.5 * (1 - r / 2) * np.exp(-r / 2)
u21 = lambda r: r**2 / (np.sqrt(3) * 2**1.5) * np.exp(-r / 2)
for nm, u in (("1s", u10), ("2s", u20), ("2p", u21)):
    check(f"norm {nm}", I(lambda r: u(r) ** 2, 0, 80), 1)
check("<r>_1s", I(lambda r: r * u10(r) ** 2, 0, 80), 1.5)
check("<r>_2p", I(lambda r: r * u21(r) ** 2, 0, 80), 5)
check("<1/r>_2p", I(lambda r: u21(r) ** 2 / r, 1e-9, 80), 0.25)
check("P(r>a0) 1s", I(lambda r: u10(r) ** 2, 1, 80), 5 * np.exp(-2))
check("2p mode", brentq(lambda r: 4 * r**3 * np.exp(-r) - r**4 * np.exp(-r), 1, 10), 4)

# L_x^2 in Y_lm from ladder matrices, l=2
l = 2
ms = np.arange(l, -l - 1, -1)
Lp = np.zeros((2 * l + 1, 2 * l + 1))
for j in range(1, 2 * l + 1):
    Lp[j - 1, j] = np.sqrt(l * (l + 1) - ms[j] * (ms[j] + 1))
Lx = (Lp + Lp.T) / 2
for j, m in enumerate(ms):
    check(f"<Lx^2> l=2 m={m}", (Lx @ Lx)[j, j], (l * (l + 1) - m**2) / 2)

# Bomb test matrices
c, s_ = np.cos(.6), np.sin(.6)
B1 = np.array([[c, -s_], [s_, c]]); B2 = np.array([[c, s_], [-s_, c]])
out = B2 @ B1 @ np.array([1, 0])
check("dud goes to D0", abs(out[0]) ** 2, 1)
after = np.array([(B1 @ np.array([1, 0]))[0], 0])
check("live P(D1)", (B2 @ after)[1] ** 2, s_**2 * c**2)

# Circle state cos^2
L_ = 1.0
N2 = 1 / I(lambda x: np.cos(2 * pi * x) ** 4, 0, 1)
check("circle N^2", N2, 8 / 3)
c0 = I(lambda x: np.sqrt(N2) * np.cos(2 * pi * x) ** 2, 0, 1) ** 2
check("circle P(n=0)", c0, 2 / 3)
c2 = I(lambda x: np.sqrt(N2) * np.cos(2 * pi * x) ** 2 * np.cos(4 * pi * x), 0, 1) ** 2
check("circle P(n=+2)", c2, 1 / 6)

# Current for N(x+ib)exp(-x^2/2a^2), by finite differences (hbar=m=N=1, b=0.7, a=1.3)
b_, a2 = .7, 1.3
P_ = lambda x: (x + 1j * b_) * np.exp(-x * x / (2 * a2**2))
x0, h2 = .4, 1e-6
J = (np.conj(P_(x0)) * (P_(x0 + h2) - P_(x0 - h2)) / (2 * h2)).imag
check("current", J, -b_ * np.exp(-x0**2 / a2**2))

print(f"\n{sum(results)}/{len(results)} checks passed")
raise SystemExit(0 if all(results) else 1)
