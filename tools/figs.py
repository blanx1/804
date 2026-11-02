"""Inline SVG figures, computed from the actual physics. Each returns one line of HTML for markdown."""
import math

BLUE, RED, GREEN, ORANGE, GRAY = "#2F7FD8", "#d9534f", "#2e9e5b", "#d98a1f", "#888888"


class Plot:
    def __init__(self, xr, yr, w=560, h=280, caption="", alt=""):
        self.xr, self.yr, self.w, self.h, self.caption, self.alt = xr, yr, w, h, caption, alt or caption
        self.items = []

    def X(self, x):
        return 30 + (x - self.xr[0]) / (self.xr[1] - self.xr[0]) * (self.w - 50)

    def Y(self, y):
        return self.h - 22 - (y - self.yr[0]) / (self.yr[1] - self.yr[0]) * (self.h - 40)

    def line(self, pts, color=BLUE, width=2, dash=None):
        d = " ".join(f"{self.X(x):.1f},{self.Y(max(min(y, self.yr[1]), self.yr[0])):.1f}" for x, y in pts)
        dd = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="{width}"{dd}/>')
        return self

    def curve(self, f, a=None, b=None, n=300, **kw):
        a = self.xr[0] if a is None else a
        b = self.xr[1] if b is None else b
        return self.line([(a + (b - a) * k / n, f(a + (b - a) * k / n)) for k in range(n + 1)], **kw)

    def hline(self, y, a=None, b=None, color=GRAY, dash="5 4", width=1):
        a = self.xr[0] if a is None else a
        b = self.xr[1] if b is None else b
        return self.line([(a, y), (b, y)], color=color, dash=dash, width=width)

    def vline(self, x, color=GRAY, dash="5 4", width=1):
        return self.line([(x, self.yr[0]), (x, self.yr[1])], color=color, dash=dash, width=width)

    def text(self, x, y, s, color="currentColor", anchor="start", size=13):
        self.items.append(f'<text x="{self.X(x):.1f}" y="{self.Y(y):.1f}" fill="{color}" font-size="{size}" text-anchor="{anchor}">{s}</text>')
        return self

    def axes(self, xlabel="x", ylabel=""):
        self.line([(self.xr[0], 0), (self.xr[1], 0)], color="currentColor", width=1)
        if self.xr[0] <= 0 <= self.xr[1]:
            self.line([(0, self.yr[0]), (0, self.yr[1])], color="currentColor", width=1)
        self.text(self.xr[1], 0, xlabel, anchor="end")
        if ylabel:
            self.text(max(self.xr[0], 0), self.yr[1], "  " + ylabel)
        return self

    def html(self):
        cap = f"<figcaption>{self.caption}</figcaption>" if self.caption else ""
        svg = (f'<svg viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{self.alt}" '
               f'style="width:100%;max-width:{self.w}px;height:auto;font-family:inherit">' + "".join(self.items) + "</svg>")
        return f'<figure class="xq-svg">{svg}{cap}</figure>'


def pot(segments, xr, yr, caption, labels=(), levels=()):
    """Piecewise-constant/explicit potential; segments is a list of (x, V) corner points."""
    p = Plot(xr, yr, h=220, caption=caption)
    p.axes("x", "V(x)")
    p.line(segments, color=RED, width=2.5)
    for y, s in levels:
        p.hline(y)
        p.text(xr[1], y + (yr[1] - yr[0]) * 0.02, s, anchor="end")
    for x, y, s in labels:
        p.text(x, y, s)
    return p.html()


def infinite_well():
    p = Plot((-0.15, 1.15), (0, 10.5), caption="Infinite well: energies grow as n² and ψₙ has n−1 interior nodes.")
    p.line([(0, 10.5), (0, 0), (1, 0), (1, 10.5)], color=RED, width=2.5)
    for n in (1, 2, 3):
        E = n * n
        p.hline(E, 0, 1)
        p.curve(lambda x: E + 0.75 * math.sin(n * math.pi * x), 0, 1, color=BLUE)
        p.text(1.03, E, f"n={n}")
    return p.html()


def finite_well():
    from scipy.optimize import brentq
    z0 = 4.0
    def even(eta): return eta * math.tan(eta) - math.sqrt(z0**2 - eta**2)
    def odd(eta): return -eta / math.tan(eta) - math.sqrt(z0**2 - eta**2)
    e1 = brentq(even, 0.01, math.pi / 2 - 1e-6)
    o1 = brentq(odd, math.pi / 2 + 1e-6, min(math.pi - 1e-6, z0 - 1e-9))
    e2 = brentq(even, math.pi + 1e-6, z0 - 1e-9)
    p = Plot((-2.6, 2.6), (-1.1, 0.35), caption=f"Finite well with z₀ = {z0:g}: three bound states. Each ψ curves toward the axis inside and decays exponentially outside.")
    p.line([(-2.6, 0), (-1, 0), (-1, -1), (1, -1), (1, 0), (2.6, 0)], color=RED, width=2.5)
    for eta, sign, col in ((e1, 1, BLUE), (o1, -1, GREEN), (e2, 1, ORANGE)):
        xi = math.sqrt(z0**2 - eta**2)
        E = -(xi / z0) ** 2
        def psi(x, eta=eta, xi=xi, sign=sign):
            inside = (math.cos(eta * x) if sign == 1 else math.sin(eta * x))
            edge = (math.cos(eta) if sign == 1 else math.sin(eta))
            if abs(x) < 1:
                return inside
            return edge * math.exp(-xi * (abs(x) - 1)) * (1 if x > 0 or sign == 1 else -1)
        p.hline(E, -1, 1)
        p.curve(lambda x, E=E, psi=psi: E + 0.13 * psi(x), color=col)
    return p.html()


def graphical():
    z = 4.0
    p = Plot((0, 5), (0, 5), w=420, h=340, caption="Bound states sit where the circle η²+ξ²=z₀² crosses ξ=η tan η (even, blue) or ξ=−η cot η (odd, green). Here z₀=4.")
    p.axes("η", "ξ")
    for k in range(3):
        a, b = k * math.pi + 1e-3, k * math.pi + math.pi / 2 - 1e-3
        p.curve(lambda e: e * math.tan(e), a, min(b, 5), color=BLUE)
        a2, b2 = k * math.pi + math.pi / 2 + 1e-3, k * math.pi + math.pi - 1e-3
        if a2 < 5:
            p.curve(lambda e: -e / math.tan(e), a2, min(b2, 5), color=GREEN)
    p.curve(lambda e: math.sqrt(max(z * z - e * e, 0)), 0, z, color=RED)
    return p.html()


def herm(n, y):
    a, b = 1.0, 2 * y
    if n == 0:
        return a
    for k in range(1, n):
        a, b = b, 2 * y * b - 2 * k * a
    return b


def ho_phi(n, x):
    return herm(n, x) * math.exp(-x * x / 2) / math.sqrt(2.0**n * math.factorial(n) * math.sqrt(math.pi))


def oscillator():
    p = Plot((-5, 5), (0, 8.2), caption="Oscillator, energies in units of ℏω: equally spaced levels, and φₙ leaks past the classical turning points.")
    p.curve(lambda x: x * x / 2, color=RED, width=2.5)
    for n in range(4):
        E = n + 0.5
        tp = math.sqrt(2 * E)
        p.hline(E, -tp, tp)
        p.curve(lambda x, n=n, E=E: E + 0.75 * ho_phi(n, x), color=BLUE)
        p.text(4.1, E + 0.05, f"n={n}")
    return p.html()


def delta_state():
    p = Plot((-3, 3), (-0.6, 1.2), h=220, caption="Attractive delta: a single bound state, ψ ∝ exp(−κ|x|), with a kink at the origin.")
    p.axes("x", "ψ(x)")
    p.curve(lambda x: math.exp(-1.5 * abs(x)), color=BLUE)
    p.line([(0, 0), (0, -0.55)], color=RED, width=3)
    p.text(0.1, -0.5, "V = −α δ(x)", color=RED)
    return p.html()


def step_T():
    p = Plot((0, 4), (0, 1.1), h=240, caption="Step of height V₀: R=1 for E<V₀; above it T rises from 0 toward 1. The horizontal axis is E/V₀.")
    p.axes("E / V₀")
    def T(e):
        if e <= 1:
            return 0
        k, q = math.sqrt(e), math.sqrt(e - 1)
        return 4 * k * q / (k + q) ** 2
    p.curve(T, 0, 4, color=BLUE)
    p.curve(lambda e: 1 - T(e), 0.001, 4, color=RED)
    p.text(3.0, 0.82, "T", color=BLUE)
    p.text(3.0, 0.12, "R", color=RED)
    return p.html()


def ramsauer():
    z0 = 13.0
    p = Plot((0, 3), (0, 1.1), h=240, caption=f"Square well with z₀ = {z0:g}: T(E) = [1 + V₀² sin²(2k₂a)/(4E(E+V₀))]⁻¹ reaches 1 whenever 2k₂a = nπ. Horizontal axis: E/V₀.")
    p.axes("E / V₀")
    def T(e):
        if e <= 0:
            return 0
        s = math.sin(2 * z0 * math.sqrt(1 + e))
        return 1 / (1 + s * s / (4 * e * (e + 1)))
    p.curve(T, 0.0005, 3, n=1500, color=BLUE, width=1.6)
    return p.html()


def mach_zehnder(bomb=False):
    i = [
        '<rect x="118" y="88" width="46" height="8" transform="rotate(45 141 92)" fill="#2F7FD8"/>',
        '<rect x="378" y="228" width="46" height="8" transform="rotate(45 401 232)" fill="#2F7FD8"/>',
        '<rect x="378" y="88" width="46" height="6" transform="rotate(45 401 91)" fill="#888"/>',
        '<rect x="118" y="228" width="46" height="6" transform="rotate(45 141 231)" fill="#888"/>',
        '<path d="M20 92H500M141 92V232H500M401 92V300" fill="none" stroke="#d98a1f" stroke-width="2"/>',
        '<text x="115" y="70" fill="currentColor" font-size="14">BS1</text>',
        '<text x="408" y="258" fill="currentColor" font-size="14">BS2</text>',
        '<text x="392" y="72" fill="currentColor" font-size="14">M1</text>',
        '<text x="102" y="258" fill="currentColor" font-size="14">M2</text>',
        '<text x="505" y="237" fill="currentColor" font-size="14">D0</text>',
        '<text x="392" y="318" fill="currentColor" font-size="14">D1</text>',
        '<text x="30" y="82" fill="currentColor" font-size="14">photon in</text>',
        '<text x="250" y="84" fill="currentColor" font-size="13">upper branch</text>',
        '<text x="250" y="224" fill="currentColor" font-size="13">lower branch</text>',
    ]
    if bomb:
        i.append('<circle cx="270" cy="232" r="13" fill="#d9534f"/><text x="250" y="262" fill="currentColor" font-size="13">bomb</text>')
    cap = ("Elitzur–Vaidman test: a live bomb in the lower branch acts as a which-path detector." if bomb
           else "Mach–Zehnder interferometer. Two beam splitters, two mirrors, two detectors.")
    return (f'<figure class="xq-svg"><svg viewBox="0 0 560 330" role="img" aria-label="{cap}" style="width:100%;max-width:560px;height:auto;font-family:inherit">'
            + "".join(i) + f"</svg><figcaption>{cap}</figcaption></figure>")


def packet_spread():
    p = Plot((-6, 14), (0, 0.65), h=230, caption="Free Gaussian packet: the peak moves at the group velocity while dispersion spreads it. Curves show |Ψ|² at t=0, t₁ and t₂.")
    p.axes("x", "|Ψ|²")
    def rho(x, x0, s):
        return math.exp(-((x - x0) ** 2) / (2 * s * s)) / (s * math.sqrt(2 * math.pi))
    for x0, s, c, lab in ((0, 0.7, BLUE, "t=0"), (5, 1.2, GREEN, "t₁"), (10, 2.0, ORANGE, "t₂")):
        p.curve(lambda x, x0=x0, s=s: rho(x, x0, s), color=c)
        p.text(x0, rho(x0, x0, s) + 0.02, lab, color=c, anchor="middle")
    return p.html()


def hydrogen_radial():
    p = Plot((0, 20), (0, 0.6), h=250, caption="Hydrogen radial probability P(r)=|uₙₗ|² in units of a₀⁻¹: 1s peaks at a₀, 2p at 4a₀, and 2s has one radial node.")
    p.axes("r / a₀", "P(r)")
    p.curve(lambda r: 4 * r * r * math.exp(-2 * r), 0, 20, color=BLUE)
    p.curve(lambda r: (r * r / 2) * (1 - r / 2) ** 2 * math.exp(-r), 0, 20, color=GREEN)
    p.curve(lambda r: (r**4 / 24) * math.exp(-r), 0, 20, color=ORANGE)
    p.text(1.2, 0.56, "1s", color=BLUE)
    p.text(6.0, 0.16, "2s", color=GREEN)
    p.text(3.0, 0.22, "2p", color=ORANGE)
    return p.html()


def veff():
    p = Plot((0, 20), (-0.6, 0.45), h=240, caption="Effective radial potential for hydrogen (units e²/2a₀, r in a₀): the centrifugal barrier ℓ(ℓ+1)/r² keeps ℓ>0 states away from the origin.")
    p.axes("r / a₀", "Vₑff")
    for l, c in ((0, BLUE), (1, GREEN), (2, ORANGE)):
        p.curve(lambda r, l=l: l * (l + 1) / (r * r) - 2 / r, 0.3, 20, color=c)
        p.text(20, l * (l + 1) / 361 - 2 / 19 + 0.03, f"ℓ={l}", color=c, anchor="end")
    return p.html()


def resonance_delta():
    p = Plot((0, 10), (0, 3.4), h=240, caption="Phase shift through a resonance: δ jumps rapidly by about π near k₀, giving a large positive time delay and a large inner amplitude.")
    p.axes("k", "δ(k)")
    p.curve(lambda k: math.atan2(0.25, 5 - k), 0, 10, color=BLUE)
    return p.html()
