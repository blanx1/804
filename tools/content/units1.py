"""Learn units for Lectures 1-9: foundations, matter waves, wavefunctions, operators."""
from dsl import U, R, N, S, M, C
import figs

P1 = "Part I: What makes quantum mechanics different"
P2 = "Part II: Waves, wavefunctions and the Schrödinger equation"
P3 = "Part III: Wavepackets, momentum space and operators"

UNITS = [
U("key", P1, "Lecture 1", "Key features of quantum mechanics", "foundations",
  "Five ideas set quantum mechanics apart from classical physics: linearity, complex numbers, loss of determinism, superposition and entanglement.",
  [
  R("Linearity", r"""
A theory is **linear** when its equation of motion has the form $L u = 0$ with
$L(au_1 + bu_2) = aLu_1 + bLu_2$. Then any combination of solutions is again a solution.

Maxwell's equations are linear, which is why electromagnetic waves pass through each other. General relativity
and Newton's equations for most forces are not. The Schrödinger equation

$$i\hbar\frac{\partial\Psi}{\partial t} = \hat H\Psi$$

**is** linear, and quantum mechanics takes that very seriously: the state space itself is a vector space, and
adding solutions is a physical operation.
"""),
  R("Complex numbers are essential", r"""
In classical electromagnetism, complex numbers are a convenience: you take the real part at the end.
In quantum mechanics they are in the equation itself, through the explicit $i$. A real $\Psi$ at $t=0$ generally
becomes complex right away.

Probabilities come from the **norm squared** $|\Psi|^2 = \Psi^*\Psi$. Two states that differ by an overall phase,
$\Psi$ and $e^{i\alpha}\Psi$, are physically identical. A **relative** phase between terms of a superposition,
however, is measurable, because it controls interference.
"""),
  M("Which of these pairs describe the *same* physical state?",
    [r"$\psi_1+\psi_2$ and $\psi_1-\psi_2$", r"$\psi_1+\psi_2$ and $i\psi_1+i\psi_2$", r"$\psi_1+\psi_2$ and $\psi_1+i\psi_2$", r"$\psi_1+\psi_2$ and $2\psi_1+\psi_2$"], 1,
    r"Only $i\psi_1+i\psi_2 = i(\psi_1+\psi_2)$ differs by an *overall* phase. The others change the relative phase or weights, which can change measurement outcomes."),
  R("Loss of determinism", r"""
Quantum mechanics predicts **probabilities**. A photon reaching a polarizer at angle $\alpha$ to its polarization
passes with probability $\cos^2\alpha$. Identical photons can give different outcomes, and nothing in the state
says which photon will pass.

Could there be hidden variables that decide the result in advance? Local hidden variables are testable, and
Bell-type experiments rule them out. Quantum randomness is not ignorance of some deeper local description.
"""),
  R("Superposition is not 'a bit of each'", r"""
Measure a state $|\psi\rangle = \alpha|A\rangle + \beta|B\rangle$ in which $A$ and $B$ have definite values
$a\ne b$ of some observable. You get

* result $a$ with probability $|\alpha|^2$, leaving the state $|A\rangle$,
* result $b$ with probability $|\beta|^2$, leaving the state $|B\rangle$,

and **never** an intermediate value. Superposition also isn't a statistical mixture: an electron with spin along
$+x$ is $\tfrac{1}{\sqrt2}(|\!\uparrow\rangle+|\!\downarrow\rangle)$ and passes an $x$-measurement with certainty.
A 50/50 mixture of up and down electrons would not.

Note too that a vector and its negative are the same state, so $|\!\uparrow\rangle$ and $|\!\downarrow\rangle$ are
*not* negatives of each other, though they point in opposite directions in space: they're orthogonal basis vectors.
"""),
  N(r"A photon polarized at $60^\circ$ to the axis of a polarizer. What is the probability that it passes?", 0.25,
    why=r"$P=\cos^2 60^\circ = 1/4$."),
  R("Entanglement", r"""
Two systems are **entangled** when their joint state can't be written as a product of one state for each:

$$|\psi\rangle = \tfrac{1}{\sqrt2}\big(|u_1\rangle|u_2\rangle + |v_1\rangle|v_2\rangle\big)\quad\text{cannot be factored}.$$

Measuring particle 1 immediately tells you what particle 2 will give, however far apart they are. No usable signal
travels this way, because each side alone just sees random results.

**Test:** $(a|u\rangle+b|v\rangle)(c|u\rangle+d|v\rangle)$ has coefficients $ac,ad,bc,bd$, so a two-particle state with
coefficient matrix $\begin{pmatrix}A&B\\C&D\end{pmatrix}$ is a product exactly when $AD-BC=0$.
"""),
  C("Select every state that is **entangled**. ($u,v$ label single-particle basis states; normalization omitted.)",
    [r"$|u\rangle|u\rangle + |u\rangle|v\rangle$", r"$|u\rangle|u\rangle + |v\rangle|v\rangle$",
     r"$|u\rangle|u\rangle+|u\rangle|v\rangle+|v\rangle|u\rangle+|v\rangle|v\rangle$", r"$|u\rangle|v\rangle-|v\rangle|u\rangle$"], [1, 3],
    r"Compute $AD-BC$: option 1 factors as $|u\rangle(|u\rangle+|v\rangle)$; option 3 as $(|u\rangle+|v\rangle)(|u\rangle+|v\rangle)$. Options 2 and 4 have $AD-BC\neq0$."),
  ],
  quiz=[
  M("An observable has eigenstates $|A\\rangle$ and $|B\\rangle$ with values 1 and 3. A particle is in $\\tfrac{1}{\\sqrt2}(|A\\rangle+|B\\rangle)$. Which is true of one measurement?",
    ["It gives 2", "It gives 1 or 3, each with probability 1/2", "It gives 1, then 3, alternating in time", "The result depends on the overall phase of the state"], 1,
    "A measurement returns an eigenvalue; 2 is the *average* of many measurements, not a possible result."),
  S(r"What is $|e^{i\theta}(a+ib)|^2$ for real $a,b,\theta$? (in terms of a, b, theta)", "a^2+b^2", "a b theta", r"$a^2+b^2$",
    "A phase has unit norm, so it never changes a norm squared."),
  ]),

U("mz", P1, "Lecture 2", "Photons, Mach–Zehnder and bomb testing", "foundations",
  "Represent a photon in an interferometer by a two-component vector, beam splitters by unitary matrices, and see interference and interaction-free measurement.",
  [
  R("A two-component state", r"""
Inside an interferometer a single photon is a superposition of being in two beams:

$$\begin{pmatrix}\alpha\\\beta\end{pmatrix},\qquad |\alpha|^2+|\beta|^2=1,$$

where $|\alpha|^2$ and $|\beta|^2$ are the probabilities of finding it in the upper or lower branch.

A **phase shifter** multiplies one component by $e^{i\delta}$. A **beam splitter** acts by a $2\times2$ matrix.
To conserve probability for *every* input the matrix must be **unitary**: $U^\dagger U = 1$.
"""),
  R("The interferometer", figs.mach_zehnder() + r"""

Use the balanced beam splitters from lecture:

$$\text{BS1}=\frac{1}{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix},\qquad \text{BS2}=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}.$$

Matrices act right to left, so the whole device is $\text{BS2}\cdot\text{BS1}$, and that product is the identity.
The input $\binom{1}{0}$ comes out as $\binom{1}{0}$: **every photon goes to D0.**

The contributions to D1 cancel exactly. That's interference, and it occurs one photon at a time, so each photon
must in some sense take both paths.
"""),
  M("You block the lower branch with an absorber and send in one photon from the left. What can happen?",
    ["It reaches D0 with certainty", "It reaches D0 or D1 with probability 1/2 each", "Absorbed with probability 1/2; otherwise D0 or D1 with probability 1/4 each", "Absorbed with certainty"], 2,
    r"BS1 gives $\tfrac{1}{\sqrt2}\binom11$. The absorber takes the lower part with probability 1/2. If not absorbed, the state is $\binom10$, and BS2 sends it to $\tfrac{1}{\sqrt2}\binom{1}{-1}$: D0 or D1 equally. Blocking a path destroys the interference, so D1 can now fire."),
  R("Elitzur–Vaidman bombs", figs.mach_zehnder(True) + r"""
A live bomb has a detector that explodes on any photon; a dud lets photons pass. Put one in the lower branch:

| outcome | dud | live bomb |
|---|---|---|
| explodes | 0 | 1/2 |
| D0 | 1 | 1/4 |
| D1 | 0 | 1/4 |

**A click at D1 proves the bomb is live, without any photon having hit it.** If D0 clicks, the test is inconclusive,
so repeat it. Summing the repeats, a fraction $\tfrac{1/4}{1/4+1/2}=\tfrac13$ of live bombs get certified intact.

Better beam splitters improve on 1/3. With a nearly reflective splitter and many passes, the fraction approaches 1
(the quantum Zeno idea).
"""),
  N(r"A beam splitter is applied to $\tfrac{1}{\sqrt2}\binom{1}{1}$ with matrix $\tfrac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$. What is the probability of finding the photon in the *lower* output?", 0,
    why=r"The output is $\binom10$: the amplitude for the lower beam is $\tfrac12(1-1)=0$."),
  R("Phase shifters and detection probabilities", r"""
Insert a phase $e^{i\delta}$ in the lower branch of the same interferometer. After BS1 the state is
$\tfrac{1}{\sqrt2}\binom{1}{e^{i\delta}}$, and after BS2:

$$\frac12\binom{1+e^{i\delta}}{-1+e^{i\delta}},\qquad P_0=\cos^2\frac\delta2,\quad P_1=\sin^2\frac\delta2.$$

Scanning $\delta$ moves the photon smoothly between detectors, even though the phase shifter never absorbs anything.
"""),
  S(r"With the phase shifter above, what is $P_1$? (in terms of delta)", ["sin(delta/2)^2", "(1-cos(delta))/2"], "delta", r"$\sin^2(\delta/2)$",
    r"$|{-1}+e^{i\delta}|^2/4 = (2-2\cos\delta)/4=\sin^2(\delta/2)$."),
  ],
  quiz=[
  M("Why must a beam-splitter matrix be unitary?", ["To make its entries real", "So total probability is 1 for every input state", "So that it's equal to its inverse", "So all entries have equal magnitude"], 1,
    r"$\|U\psi\|^2=\psi^\dagger U^\dagger U\psi=\|\psi\|^2$ for all $\psi$ exactly when $U^\dagger U=1$."),
  N("With a 50/50 Mach–Zehnder, testing one live bomb repeatedly until a conclusive result, what fraction explode?", 2/3,
    why=r"Each round: boom 1/2, D1 1/4, D0 (repeat) 1/4. Probability of boom overall is $\tfrac{1/2}{1/2+1/4}=2/3$."),
  ]),

U("photons", P2, "Lecture 3", "Photoelectric effect and Compton scattering", "matterwaves",
  "Light comes in quanta with E = hν and p = h/λ. Two experiments that showed it, and how to compute with them.",
  [
  R("Quanta of light", r"""
Einstein's proposal: light of frequency $\nu$ carries energy in packets, **photons**, with

$$E = h\nu=\hbar\omega,\qquad p=\frac{E}{c}=\frac{h}{\lambda}=\hbar k.$$

A useful shortcut for all numerical work: $hc\simeq 1240\ \text{eV·nm}$ and $\hbar c\simeq197.3\ \text{MeV·fm}=197.3\ \text{eV·nm}$.
Visible light (around 500 nm) has photons of about 2.5 eV.
"""),
  R("Photoelectric effect", r"""
Shine light on a metal, and electrons leave with

$$E_e = h\nu - W,$$

where $W$ is the **work function**. The facts that classical waves can't explain:

1. There's a **threshold frequency** $\nu_0=W/h$, below which no electrons emerge however bright the light is.
2. Electron energy depends on the **frequency**, not on the intensity.
3. Intensity only sets *how many* electrons come out.
4. There's no measurable time delay, even in dim light.

A stopping voltage $V_s$ measures the energy: $eV_s=h\nu-W$. The slope of $V_s$ versus $\nu$ gives $h/e$.
"""),
  N("A metal has work function 2.3 eV. What is the maximum kinetic energy of electrons ejected by 310 nm light, in eV?", 1240/310-2.3, "eV",
    why=r"$E_\gamma=1240/310=4.0$ eV, so $E_e=4.0-2.3=1.7$ eV."),
  R("Compton scattering", r"""
A photon scattering off an electron behaves as a particle collision. Relativistic energy and momentum conservation give

$$\lambda_f-\lambda_i=\lambda_C(1-\cos\theta),\qquad \lambda_C=\frac{h}{m_ec}\simeq 2.43\times10^{-12}\text{ m}.$$

The shift doesn't depend on the incident wavelength, and it's biggest for backscattering, where it equals $2\lambda_C$.
This is a clear signature of a particle: a classical wave wouldn't shift in wavelength this way.

To be visible, the shift must be comparable to $\lambda$, so Compton used X-rays.

Using $\hbar c$ and $m_ec^2=0.511$ MeV: $\lambda_C = 2\pi\,\hbar c/(m_ec^2)\approx 2.43$ pm.
"""),
  N(r"A photon scatters off a free electron at $\theta=90^\circ$. What is the wavelength shift, in pm?", 2.43, "pm",
    why=r"$\Delta\lambda=\lambda_C(1-\cos 90^\circ)=\lambda_C$."),
  ],
  quiz=[
  C("Doubling the intensity of above-threshold light on a metal does which of these?", ["Doubles the number of electrons per second", "Doubles each electron's kinetic energy", "Lowers the work function", "Leaves the maximum electron energy unchanged"], [0, 3],
    "More photons means more electrons; each electron still absorbs one photon of the same energy."),
  N("A photon has energy 1 MeV. What is its wavelength, in pm?", 1240e-6/1e-3*1e-0, "pm",
    why=r"$\lambda=hc/E=1240\text{ eV·nm}/10^6\text{ eV}=1.24\times10^{-3}$ nm $=1.24$ pm."),
  ]),

U("debroglie", P2, "Lectures 3–4", "de Broglie waves, phase and group velocity", "matterwaves",
  "Every particle has a wavelength λ = h/p. Learn how wave speeds work and why the free-particle wavefunction must be a complex exponential.",
  [
  R("The de Broglie wavelength", r"""
de Broglie's bold extension to matter: a particle with momentum $p$ has an associated wave with

$$\lambda=\frac hp,\qquad p=\hbar k,\qquad E=\hbar\omega.$$

Davisson–Germer electron diffraction confirmed it. For a nonrelativistic particle with kinetic energy $K$:

$$\lambda=\frac{h}{\sqrt{2mK}}=\frac{hc}{\sqrt{2(mc^2)K}}.$$

For electrons, a handy result: $\lambda\simeq 1.226\ \text{nm}/\sqrt{K/\text{eV}}$.

Quantum effects matter when $\lambda$ is comparable to the system's size. Macroscopic objects have absurdly tiny $\lambda$.
"""),
  N("What is the de Broglie wavelength of an electron with kinetic energy 100 eV, in nm? (Use $m_ec^2=0.511$ MeV, $hc=1240$ eV·nm.)", 1240/(2*0.511e6*100)**0.5, "nm",
    why=r"$pc=\sqrt{2(5.11\times10^5)(100)}\approx1.01\times10^4$ eV, so $\lambda=1240/10^4\approx0.123$ nm."),
  R("A puzzle under Galilean boosts", r"""
Observers $S$ and $S'$ with relative velocity $v$ disagree on a particle's momentum, and so on its wavelength.
Ordinary waves (sound) have the same wavelength in all frames. So the de Broglie wave **can't be an ordinary observable
wave**: its phase isn't a Galilean scalar.

Working out how $kx-\omega t$ changes under $x=x'+vt$ with $E=p^2/2m$ shows that $\Psi$ transforms with an extra
position-dependent phase. Since $|\Psi|^2$ doesn't feel that phase, probabilities stay frame independent, as they should.
"""),
  R("Phase and group velocity", r"""
A plane wave $e^{i(kx-\omega t)}$ has crests moving at the **phase velocity** $v_{ph}=\omega/k$.
A *packet* peaked near $k_0$ moves at the **group velocity**, found by stationary phase:

$$v_g=\left.\frac{d\omega}{dk}\right|_{k_0}.$$

The argument: $\Psi=\int dk\,\Phi(k)e^{i(kx-\omega(k)t)}$ only adds up where the phase is stationary at the peak,
$\frac{d}{dk}(kx-\omega t)=0$ at $k_0$, which is $x=\omega'(k_0)t$.

For a free nonrelativistic particle, $\omega=\hbar k^2/2m$:

$$v_{ph}=\frac{\hbar k}{2m}=\frac{v}{2},\qquad v_g=\frac{\hbar k}{m}=v.$$

The packet moves with the particle. That's the velocity that matters.
"""),
  S(r"For $\omega(k)=\sqrt{c^2k^2+\Omega^2}$, what is $v_g$? (in terms of c, k, Omega)", "c^2 k/sqrt(c^2 k^2+Omega^2)", "c k Omega", r"$\dfrac{c^2k}{\sqrt{c^2k^2+\Omega^2}}$",
    r"Differentiate: $v_g=c^2k/\omega$. This is the relativistic relation $v=pc^2/E$, with $\hbar\Omega=mc^2$."),
  R("Which free-particle wave?", r"""
Which of $\sin(kx-\omega t)$, $\cos(kx-\omega t)$, $e^{i(kx-\omega t)}$, $e^{-i(kx-\omega t)}$ describes a particle with
momentum $\hbar k>0$? Superposition settles it.

1. **Real waves fail.** Superpose right- and left-movers with equal weight: $\sin(kx-\omega t)+\sin(kx+\omega t)=2\sin kx\cos\omega t$,
   which vanishes for all $x$ whenever $\cos\omega t=0$. A particle can't have a wavefunction that is identically zero at some
   instant. Cosines fail the same way.
2. **Exponentials work.** $e^{i(kx-\omega t)}+e^{i(-kx-\omega t)}=2\cos kx\,e^{-i\omega t}$ never vanishes identically, because $e^{-i\omega t}$ is never zero.
3. **We can't keep both signs.** If $e^{i(kx-\omega t)}$ and $e^{-i(kx-\omega t)}$ both described a right-mover, their sum
   would too, but that sum is $2\cos(kx-\omega t)$, which already failed.

So we choose one, by convention $\Psi=e^{i(kx-\omega t)}$. Complex numbers aren't optional.
"""),
  ],
  quiz=[
  M("A free nonrelativistic packet: how is its group velocity related to its phase velocity?", [r"$v_g=v_{ph}$", r"$v_g=2v_{ph}$", r"$v_g=v_{ph}/2$", r"$v_g v_{ph}=c^2$"], 1,
    r"From $\omega\propto k^2$: $v_g=2\omega/k=2v_{ph}$. The relation $v_gv_{ph}=c^2$ applies to the relativistic free particle."),
  N("Two electrons: one has twice the kinetic energy of the other (both nonrelativistic). What is the ratio of the faster electron's wavelength to the slower one's?", 2**-0.5,
    why=r"$\lambda\propto K^{-1/2}$, so the ratio is $1/\sqrt2$."),
  ]),

U("schrod", P2, "Lecture 5", "The Schrödinger equation", "schrodinger",
  "Build the equation from the plane wave, meet operators, and read Ψ as a probability amplitude.",
  [
  R("From plane wave to equation", r"""
Differentiating $\Psi=e^{i(kx-\omega t)}$ gives

$$\frac\hbar i\frac{\partial\Psi}{\partial x}=\hbar k\Psi=p\Psi,\qquad i\hbar\frac{\partial\Psi}{\partial t}=\hbar\omega\Psi=E\Psi.$$

So we identify the **momentum operator** and read off the free equation from $E=p^2/2m$:

$$\hat p=\frac\hbar i\frac{\partial}{\partial x},\qquad i\hbar\frac{\partial\Psi}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2\Psi}{\partial x^2}.$$

First order in time means $\Psi(x,0)$ alone determines the future. Linearity means superpositions of plane waves also solve it.
"""),
  R("Operators and commutators", r"""
An operator maps functions to functions. $\Psi$ is an eigenfunction of $\hat p$ with eigenvalue $p_0$ if
$\hat p\Psi=p_0\Psi$. Order matters:

$$[\hat x,\hat p]\equiv\hat x\hat p-\hat p\hat x=i\hbar.$$

To derive it, apply to a test function: $x\frac\hbar i f'-\frac\hbar i(xf)'=-\frac\hbar i f=i\hbar f$.

Two identities cover most exam computations:

$$[A,BC]=[A,B]C+B[A,C],\qquad [\hat p,f(\hat x)]=\frac\hbar i f'(\hat x).$$

Adding a potential gives the full equation:

$$i\hbar\frac{\partial\Psi}{\partial t}=\hat H\Psi,\qquad\hat H=\frac{\hat p^2}{2m}+V(\hat x,t).$$
"""),
  S(r"Using the identities above, what is $[\hat x,\hat p^2]$? Write $\hat p$ as p. (in terms of hbar, p; use i)", "2 i hbar p", "hbar p", r"$2i\hbar\hat p$",
    r"$[x,p^2]=[x,p]p+p[x,p]=2i\hbar p$."),
  R("What Ψ means", r"""
Born's rule: $|\Psi(x,t)|^2dx$ is the probability of finding the particle in $[x,x+dx]$. So for a physical state

$$\int_{-\infty}^\infty|\Psi|^2dx=1.$$

$\Psi$ itself has units $L^{-1/2}$ in one dimension and $L^{-3/2}$ in three. A plane wave isn't normalizable, so it's not
a physical state. It's an idealization and a building block for packets.
"""),
  N(r"$\Psi(x,0)=Ne^{-|x|/a}$. What is $N^2 a$ for a normalized state?", 1,
    why=r"$\int e^{-2|x|/a}dx=a$, so $N^2=1/a$."),
  ],
  quiz=[
  S(r"Evaluate $[\hat p,\hat x^3]$. Write $\hat x$ as x. (in terms of hbar, x; use i)", "-3 i hbar x^2", "hbar x", r"$-3i\hbar\hat x^2$",
    r"$[p,f(x)]=\tfrac\hbar i f'=-i\hbar\cdot3x^2$."),
  M(r"What are the units of $\Psi$ for a particle moving in three dimensions?", [r"dimensionless", r"$L^{-1/2}$", r"$L^{-3/2}$", r"$L^{-3}$"], 2,
    r"$|\Psi|^2d^3x$ is dimensionless, so $|\Psi|^2$ has units $L^{-3}$."),
  ]),

U("prob", P2, "Lecture 6", "Normalization, Hermiticity and probability current", "schrodinger",
  "Why normalization survives time evolution, what Hermitian means, and how probability flows.",
  [
  R("Normalization is conserved", r"""
Let $N(t)=\int|\Psi|^2dx$. If $\Psi$ solves the Schrödinger equation with a **Hermitian** Hamiltonian and vanishes at infinity,
then $dN/dt=0$. Hermiticity of an operator $T$ is the statement

$$\int(T\Psi_1)^*\Psi_2\,dx=\int\Psi_1^*(T\Psi_2)\,dx.$$

The Schrödinger equation is only consistent with a probability interpretation because $\hat H$ is Hermitian.
$\hat p$ is Hermitian, as integration by parts shows; the factor of $i$ is what fixes the sign.
"""),
  R("Probability current", r"""
Local conservation has the same form as charge conservation:

$$\frac{\partial\rho}{\partial t}+\frac{\partial J}{\partial x}=0,\qquad \rho=|\Psi|^2,\qquad J=\frac\hbar m\text{Im}\left(\Psi^*\frac{\partial\Psi}{\partial x}\right).$$

Integrating over a region shows that $J(a)-J(b)$ is the rate at which probability flows into $[a,b]$.

Key cases to remember:

* A **real** wavefunction, or any real function times a constant phase, has $J=0$.
* $Ae^{ikx}+Be^{-ikx}$ has $J=\frac{\hbar k}{m}(|A|^2-|B|^2)$, and the cross terms cancel.
* $J$ has units of 1/time in one dimension. In 3D, $\vec J=\frac\hbar m\text{Im}(\Psi^*\nabla\Psi)$.
"""),
  S(r"What is $J$ for $\Psi=Ae^{ikx}$? (in terms of hbar, k, m, A, with real A)", "hbar k A^2/m", "hbar k m A", r"$\dfrac{\hbar k}{m}A^2$",
    r"$\Psi^*\partial_x\Psi=ik|A|^2$, so $J=\tfrac\hbar m k|A|^2$: density times velocity."),
  C("Which of these have zero probability current at every $x$? ($k$ real, nonzero.)", [r"$\sin kx$", r"$e^{i\alpha}\cos kx$", r"$e^{ikx}$", r"$e^{ikx}+e^{-ikx}$"], [0, 1, 3],
    r"$e^{ikx}+e^{-ikx}=2\cos kx$ is real, and a constant phase doesn't change the current. Only the traveling wave carries current."),
  R("Current gives you phase information", r"""
Write $\Psi=\sqrt{\rho}\,e^{iS(x)}$ with real $S$. Then

$$J=\frac{\hbar}{m}\rho\frac{dS}{dx},$$

so **the velocity field is $\frac\hbar m\nabla S$**. Probability flows because the phase varies with position.
That is the physical meaning of the phase of $\Psi$.
"""),
  ],
  quiz=[
  M(r"A region $[a,b]$ has $J(a)=2\ \text{s}^{-1}$ and $J(b)=5\ \text{s}^{-1}$. What happens to the probability of being inside?", ["It rises at 3 per second", "It falls at 3 per second", "It rises at 7 per second", "It stays constant"], 1,
    r"$dP/dt=J(a)-J(b)=-3$."),
  S(r"For $\Psi=Ae^{ikx}+Be^{-ikx}$ with real $A,B$, what's $J$? (in terms of hbar, k, m, A, B)", "hbar k (A^2-B^2)/m", "hbar k m A B", r"$\dfrac{\hbar k}{m}(A^2-B^2)$",
    "The cross terms are complex conjugates up to sign, so they cancel in the imaginary part."),
  ]),

U("packets", P3, "Lecture 7", "Wavepackets and uncertainty", "wavepackets",
  "A localized particle is a superposition of many momenta. See why narrow packets have broad spectra, and why they spread.",
  [
  R("Fourier representation", r"""
Any normalizable state can be built from plane waves:

$$\Psi(x,0)=\frac{1}{\sqrt{2\pi}}\int dk\,\Phi(k)e^{ikx},\qquad \Phi(k)=\frac{1}{\sqrt{2\pi}}\int dx\,\Psi(x,0)e^{-ikx}.$$

A general fact about Fourier transforms is $\Delta x\,\Delta k\gtrsim1$. Multiplying by $\hbar$ yields the uncertainty
relation. Narrow in space means broad in momentum, and vice versa. It isn't about a clumsy measurement: it's a property of waves.

The precise statement for rms widths is $\Delta x\,\Delta p\ge\hbar/2$, with equality for a Gaussian.

The Gaussian integral you'll use constantly:

$$\int_{-\infty}^\infty e^{-ax^2+bx}dx=\sqrt{\frac\pi a}\,e^{b^2/4a},\qquad\text{Re }a>0.$$
"""),
  R("Time evolution and spreading", figs.packet_spread() + r"""
For a free particle each plane wave evolves with its own phase, so

$$\Psi(x,t)=\frac{1}{\sqrt{2\pi}}\int dk\,\Phi(k)\,e^{ikx-i\hbar k^2t/2m},$$

where $\Phi(k)$ doesn't depend on $t$, because momentum is conserved. **This is the standard recipe: decompose at $t=0$,
attach a phase to each $k$, and recombine.**

Different $k$'s travel at different speeds, so packets spread. Expanding the phase about $k_0$:

* The linear term moves the packet at $v_g$.
* The quadratic term $\frac{\hbar t}{2m}(k-k_0)^2$ changes the shape once it's about 1 for $k-k_0\sim\Delta k$.

So the **shape-preservation time** is $t_s\sim\dfrac{m}{\hbar(\Delta k)^2}$, equivalently $t\,\Delta v\lesssim\Delta x$.
A narrower packet spreads faster.

For a Gaussian with initial width $\Delta_0=\Delta x(0)$, $\quad\Delta x(t)=\Delta_0\sqrt{1+\left(\dfrac{\hbar t}{2m\Delta_0^2}\right)^2}$.
Note $\Delta p$ stays constant in the free evolution, although $\Delta x$ grows.
"""),
  N("An electron is localized to $\\Delta x=0.1$ nm. Estimate $\\Delta p\\,c$ from the uncertainty bound $\\Delta x\\Delta p=\\hbar/2$, in eV.", 197.3/(2*0.1), "eV", tol=0.03,
    why=r"$\Delta p\,c=\hbar c/(2\Delta x)=197.3/(0.2)\approx987$ eV."),
  S(r"Using the Gaussian formula, what is $\int_{-\infty}^\infty e^{-x^2/2\sigma^2}dx$? (in terms of sigma)", "sqrt(2 pi) sigma", "sigma", r"$\sqrt{2\pi}\,\sigma$",
    r"Take $a=1/2\sigma^2$, $b=0$."),
  ],
  quiz=[
  M("Two Gaussian packets of the same mass start with widths $\\Delta$ and $2\\Delta$. Which spreads faster, and how does the time scale compare?", ["The wider, by factor 4", "The narrower: its spreading time is 4 times shorter", "The narrower: its spreading time is 2 times shorter", "They spread at the same rate"], 1,
    r"$t_s\sim m\Delta^2/\hbar$. Halving the width quarters the time."),
  S(r"For the free Gaussian, express the width at $t=2m\Delta_0^2/\hbar$ in terms of $\Delta_0$. (in terms of D0)", "sqrt(2) D0", "D0", r"$\sqrt2\,\Delta_0$",
    r"The bracket is $\hbar t/2m\Delta_0^2=1$, so $\Delta x=\Delta_0\sqrt2$."),
  ]),

U("momspace", P3, "Lecture 8", "Momentum space and expectation values", "wavepackets",
  "Φ(p) contains the same information as Ψ(x). Compute averages and see how they evolve in time.",
  [
  R("Momentum space", r"""
Parseval's identity says Fourier transforms preserve the norm:

$$\int|\Psi(x)|^2dx=\int|\Phi(k)|^2dk,$$

so $|\Phi(k)|^2dk$ is the probability that the wavenumber lies in $[k,k+dk]$. In momentum space $\hat p$ is multiplication,
and $\hat x=i\hbar\,\partial_p$. Position and momentum representations are two descriptions of one state.
"""),
  R("Expectation values", r"""
For an operator $\hat Q$,

$$\langle\hat Q\rangle_\Psi(t)=\int dx\,\Psi^*(x,t)\,\hat Q\,\Psi(x,t).$$

This is the **average** over many identically prepared systems. It isn't necessarily a possible single outcome. So:

$$\langle\hat x\rangle=\int x|\Psi|^2dx,\qquad\langle\hat p\rangle=\int\Psi^*\frac\hbar i\partial_x\Psi\,dx=\int\hbar k|\Phi(k)|^2dk.$$

Two time savers: **an odd integrand over a symmetric range gives zero**, and **a real wavefunction has $\langle\hat p\rangle=0$**.

Multiplying by a phase $e^{iqx/\hbar}$ shifts the momentum: $\langle\hat p\rangle\to\langle\hat p\rangle+q$, and doesn't touch $\Delta p$ or $|\Psi|^2$.
"""),
  N(r"$\Psi(x)=\sqrt{\tfrac{2}{a}}\sin(\pi x/a)$ on $0<x<a$. What is $\langle\hat p\rangle$?", 0,
    why=r"The wavefunction is real, so $\langle\hat p\rangle=0$. (The expectation value must be real, while $\frac\hbar i\int\psi\psi'dx$ would be imaginary unless it vanished.)"),
  R("Time dependence and Ehrenfest", r"""
For any Hermitian $\hat Q$ with no explicit time dependence:

$$\frac{d}{dt}\langle\hat Q\rangle=\frac i\hbar\langle[\hat H,\hat Q]\rangle.$$

Take $\hat Q=\hat x$ and $\hat Q=\hat p$ to get **Ehrenfest's theorem**, and classical-looking equations for averages:

$$\frac{d\langle x\rangle}{dt}=\frac{\langle p\rangle}{m},\qquad\frac{d\langle p\rangle}{dt}=-\left\langle V'(x)\right\rangle.$$

Warning: in general $\langle V'(x)\rangle\ne V'(\langle x\rangle)$, so $\langle x\rangle$ doesn't quite follow a classical path.
They're equal for $V$ quadratic or linear, which is why oscillator packets oscillate classically.

Also, if $[\hat H,\hat Q]=0$, then $\langle\hat Q\rangle$ is conserved in every state.
"""),
  S(r"A particle has $V=Fx$ with constant $F$. What is $d\langle p\rangle/dt$? (in terms of F)", "-F", "F", r"$-F$",
    "Ehrenfest: $-\\langle V'\\rangle=-F$."),
  ],
  quiz=[
  S(r"$\Psi=e^{iqx/\hbar}f(x)$ with real normalized $f$. What's $\langle\hat p\rangle$? (in terms of q)", "q", "q", r"$q$",
    r"The derivative acting on $f$ gives a real-function integrand $ff'$ that integrates to zero; the phase contributes $q$."),
  C("For a free particle, which are constant in time?", [r"$\langle\hat p\rangle$", r"$\Delta p$", r"$\Delta x$", r"$|\Phi(k,t)|^2$"], [0, 1, 3],
    r"$\hat p$ commutes with $\hat H=\hat p^2/2m$, so its whole distribution is conserved, while the packet spreads in $x$."),
  ]),

U("herm", P3, "Lecture 9", "Observables, Hermitian operators and uncertainty", "operators",
  "Observables are Hermitian operators. Eigenvalues are measurement outcomes, eigenstates form a basis, and non-commuting pairs obey an uncertainty bound.",
  [
  R("Why Hermitian?", r"""
Define the adjoint by $\int(\hat K\Psi_1)^*\Psi_2=\int\Psi_1^*(\hat K^\dagger\Psi_2)$. An operator is **Hermitian** when $\hat K^\dagger=\hat K$.
Rules: $(AB)^\dagger=B^\dagger A^\dagger$ and $(cA)^\dagger=c^*A^\dagger$.

Consequences that make Hermitian operators observables:

1. **Eigenvalues are real.**
2. **Eigenfunctions with different eigenvalues are orthogonal**.
3. **Eigenfunctions form a complete basis**, so $\Psi=\sum_nc_n\psi_n$ with $c_n=\int\psi_n^*\Psi\,dx$.

If $\hat Q$ and $\hat R$ are Hermitian, then $[\hat Q,\hat R]$ is **anti-Hermitian** and $i[\hat Q,\hat R]$ is Hermitian.
"""),
  C(r"$\hat A,\hat B$ are Hermitian and don't commute. Select all that are Hermitian.", [r"$\hat A\hat B$", r"$\hat A\hat B+\hat B\hat A$", r"$\hat A\hat B-\hat B\hat A$", r"$i(\hat A\hat B-\hat B\hat A)$"], [1, 3],
    r"$(AB)^\dagger=BA\ne AB$. The commutator flips sign under $\dagger$, and the extra $i$ fixes it."),
  R("The measurement postulate", r"""
Expand $\Psi=\sum_nc_n\psi_n$ in eigenstates of $\hat Q$, with eigenvalues $q_n$. Measuring $Q$:

* yields one of the $q_n$, with probability $|c_n|^2$;
* collapses the state to the corresponding $\psi_n$, so repeating immediately gives the same result.

So $\sum|c_n|^2=1$ and $\langle Q\rangle=\sum_nq_n|c_n|^2$.
"""),
  S(r"$\psi=\tfrac{1}{\sqrt3}\psi_1+\sqrt{\tfrac23}\psi_2$ with $\hat H\psi_n=E_n\psi_n$. What is $\langle H\rangle$? (in terms of E1, E2)", "E1/3+2 E2/3", "E1 E2", r"$\tfrac13E_1+\tfrac23E_2$",
    r"Add eigenvalues weighted by $|c_n|^2$."),
  R("Uncertainty", r"""
Define $(\Delta Q)^2=\langle Q^2\rangle-\langle Q\rangle^2=\langle(Q-\langle Q\rangle)^2\rangle\ge0$. **$\Delta Q=0$ if and only if the state is an eigenstate of $\hat Q$.**

The general uncertainty inequality:

$$\Delta A\,\Delta B\ge\left|\frac{1}{2i}\langle[\hat A,\hat B]\rangle\right|.$$

Putting in $A=x$, $B=p$ gives $\Delta x\Delta p\ge\hbar/2$. The bound depends on the state via the expectation value of the
commutator. If $[\hat A,\hat B]=0$ you can have simultaneous eigenstates, though not every state is one.
Conversely, a nonzero commutator can still have some simultaneous eigenstate, if the commutator annihilates it.

**Energy–time.** With $\Delta t\equiv\Delta Q/|d\langle Q\rangle/dt|$, one gets $\Delta E\,\Delta t\ge\hbar/2$. Here $\Delta t$ is not an operator
uncertainty; it's the time for the state to change appreciably.

**Using uncertainty to estimate.** Replacing $p\sim\hbar/\Delta x$ in the energy and minimizing gives quick ground-state estimates.
"""),
  N(r"A particle is in $\psi$ with $\langle x\rangle=2$ and $\langle x^2\rangle=5$ (arbitrary length units). What is $\Delta x$?", 1,
    why=r"$\Delta x=\sqrt{5-4}=1$."),
  ],
  quiz=[
  M(r"What is the Hermitian conjugate of $\hat x\hat p$?", [r"$\hat x\hat p$", r"$\hat p\hat x$", r"$-\hat x\hat p$", r"$-\hat p\hat x$"], 1, r"$(xp)^\dagger=p^\dagger x^\dagger=px$."),
  M(r"Energy of a state is measured and found to be $E_3$. Energy is measured again right away. What's the result?", [r"$E_3$ with certainty", r"Some $E_n$ with probabilities $|c_n|^2$ of the original state", r"$E_3$ with probability $|c_3|^2$", r"Unknown"], 0,
    "The state collapsed to the $E_3$ eigenstate, so the repeat is certain."),
  S(r"Lower bound on $\Delta x\,\Delta(p^2)$? Using $[x,p^2]=2i\hbar p$, in terms of hbar and the magnitude P of $\langle p\rangle$ (P>0).", "hbar P", "hbar P", r"$\hbar|\langle p\rangle|$",
    r"$\left|\frac{1}{2i}\langle2i\hbar p\rangle\right|=\hbar|\langle p\rangle|$."),
  ]),
]
