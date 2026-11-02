"""Learn units for Lectures 10-22: bound states, oscillator, scattering, 3D and hydrogen."""
from dsl import U, R, N, S, M, C
import figs

P4 = "Part IV: Energy eigenstates and bound states"
P5 = "Part V: Scattering"
P6 = "Part VI: Three dimensions and hydrogen"

UNITS = [
U("stationary", P4, "Lecture 10", "Stationary states and time evolution", "stationary",
  "Separate variables, find energy eigenstates, and learn the recipe that solves any time-independent problem.",
  [
  R("Stationary states", r"""
For time-independent $V$, try $\Psi(x,t)=\psi(x)f(t)$. Separation gives $f=e^{-iEt/\hbar}$ and the **time-independent Schrödinger equation**:

$$\hat H\psi=-\frac{\hbar^2}{2m}\psi''+V\psi=E\psi.$$

In a stationary state, $|\Psi|^2$ doesn't change, and neither does the expectation value of any time-independent operator.
The state just rotates by a global phase. Also, $\Delta H=0$.

$E$ must be real for a normalizable state, and for bound states the energies are discrete.
"""),
  R("The time-evolution recipe", r"""
**Any** initial state evolves in three steps:

1. Expand: $\Psi(x,0)=\sum_nc_n\psi_n(x)$, with $c_n=\int\psi_n^*\Psi(x,0)dx$.
2. Attach phases: $\Psi(x,t)=\sum_nc_ne^{-iE_nt/\hbar}\psi_n(x)$.
3. Done. The probabilities $|c_n|^2$ and $\langle H\rangle$ are constant.

A superposition of *different* energies isn't stationary. In $|\Psi|^2$, the cross term between $\psi_m$ and $\psi_n$ oscillates at the
**Bohr frequency** $\omega_{mn}=(E_m-E_n)/\hbar$. An overall phase cancels, and only energy differences are observable.
"""),
  S(r"$\Psi(x,0)=\tfrac{1}{\sqrt2}(\psi_1+\psi_2)$. At what angular frequency does $|\Psi|^2$ oscillate? (in terms of E1, E2, hbar, with E2>E1)", "(E2-E1)/hbar", "E1 E2 hbar", r"$(E_2-E_1)/\hbar$",
    r"The cross term has the time factor $e^{\pm i(E_2-E_1)t/\hbar}$."),
  R("Conditions on ψ", r"""
For a Hamiltonian with reasonable $V$:

| $V$ | $\psi$ | $\psi'$ |
|---|---|---|
| continuous | continuous | continuous |
| finite jump | continuous | continuous |
| delta function | continuous | jumps |
| hard wall ($\infty$ on one side) | continuous, $\psi=0$ at the wall | jumps, $\psi'\neq0$ allowed |

$\psi$ always stays continuous, because a jump would make $\psi''$ too singular to match $V\psi$.
"""),
  R("Free particle on a circle", r"""
Take a circle of circumference $L$, with $\psi(x+L)=\psi(x)$ since $x$ and $x+L$ are the same physical point. Solutions:

$$\psi_n=\frac{1}{\sqrt L}e^{ik_nx},\qquad k_n=\frac{2\pi n}{L},\qquad E_n=\frac{\hbar^2k_n^2}{2m}=\frac{2\pi^2\hbar^2n^2}{mL^2},\quad n\in\mathbb Z.$$

There's a state with $n=0$, $E=0$ (a constant is normalizable on a circle), which isn't degenerate. Every $n\ne0$ level is **doubly degenerate** ($\pm n$,
clockwise or counterclockwise). The momentum eigenstates are also energy eigenstates here, because $\hat p$ commutes with $\hat H$.
"""),
  N("On a circle, what's the ratio of $E_1$ to the ground-state energy of an infinite well of width $L$?", 4,
    why=r"Circle: $2\pi^2\hbar^2/mL^2$. Well: $\pi^2\hbar^2/2mL^2$. Ratio is 4."),
  ],
  quiz=[
  C("In a stationary state of a time-independent $V$, which are time-independent?", [r"$\Psi(x,t)$", r"$|\Psi(x,t)|^2$", r"$\langle\hat p\rangle$", r"$\langle\hat x^2\rangle$"], [1, 2, 3],
    "The wavefunction itself still has a phase factor, but it cancels in all these expectation values."),
  N(r"$\Psi(x,0)=\tfrac35\psi_1+\tfrac45\psi_3$ with energies $E_1=1$ eV and $E_3=9$ eV. What's $\langle H\rangle$ in eV?", 0.36*1+0.64*9, "eV",
    why=r"$\tfrac{9}{25}(1)+\tfrac{16}{25}(9)=6.12$ eV."),
  ]),

U("wells", P4, "Lecture 11", "Infinite and finite square wells", "wells",
  "The two workhorse bound-state problems, including the graphical solution for the finite well.",
  [
  R("Infinite square well", figs.infinite_well() + r"""
With $V=0$ on $0<x<a$ and infinite elsewhere, $\psi(0)=\psi(a)=0$ quantizes $k$:

$$\psi_n=\sqrt{\frac2a}\sin\frac{n\pi x}{a},\qquad E_n=\frac{\hbar^2\pi^2n^2}{2ma^2},\qquad n=1,2,\dots$$

Things to know without thinking:

* $n=0$ is excluded (it gives $\psi=0$), and negative $n$ are the same states up to a sign.
* $\psi_n$ has $n-1$ interior **nodes**.
* The states alternate parity about the center: $n$ odd is even about $a/2$, and $n$ even is odd.
* Orthonormal: $\int_0^a\psi_m\psi_n=\delta_{mn}$, and $\langle x\rangle=a/2$ in every eigenstate.
* The zero-point energy $E_1>0$ is what uncertainty demands.
"""),
  N(r"An electron is in a well of width 1 nm. What's its ground-state energy in eV? (Use $\hbar c=197.3$ eV·nm, $m_ec^2=0.511\times10^6$ eV.)", 197.3**2*3.14159265**2/(2*0.511e6), "eV",
    why=r"$E_1=\pi^2(\hbar c)^2/(2m_ec^2a^2)=\pi^2(197.3)^2/(1.022\times10^6)\approx0.376$ eV."),
  R("Finite square well", figs.finite_well() + r"""
Take $V=-V_0$ for $|x|<a$ and $0$ outside. Bound states have $-V_0<E<0$. Since $V$ is even, states can be chosen even or odd.
Define dimensionless quantities:

$$\eta^2=\frac{2m(E+V_0)a^2}{\hbar^2},\qquad\xi^2=\frac{2m|E|a^2}{\hbar^2},\qquad z_0^2=\frac{2mV_0a^2}{\hbar^2},\qquad\eta^2+\xi^2=z_0^2.$$

Inside, $\psi$ is $\cos$ or $\sin$ with wavenumber $\eta/a$. Outside, it decays like $e^{-\xi|x|/a}$. Matching $\psi'/\psi$ at $x=a$:

$$\text{even: }\xi=\eta\tan\eta,\qquad\text{odd: }\xi=-\eta\cot\eta.$$
"""),
  R("Counting bound states", figs.graphical() + r"""
Each intersection of the circle of radius $z_0$ with a curve is a state. Reading the plot:

* There's **always at least one** even bound state, however shallow the well.
* The $k$-th state appears as $z_0$ passes $(k-1)\pi/2$, so the count is $\lceil 2z_0/\pi\rceil$.
* A shallow well has $\eta\approx z_0$, $\xi\approx z_0^2$, with a tiny binding energy.
* A deep well approaches infinite-well levels of width $2a$ (just slightly lower, as $\psi$ leaks out).

Half-well trick: if there's a hard wall at $x=0$ and a well on $0<x<a$, only **odd** states survive, since $\psi(0)=0$.
So a half-well needs $z_0>\pi/2$ for any bound state.
"""),
  N(r"A symmetric finite well has $z_0=7$. How many bound states does it have?", 5,
    why=r"$2z_0/\pi=4.46$, rounded up is 5.", qtype="computational"),
  ],
  quiz=[
  N(r"For $\psi_2$ of the infinite well of width $a$, what's the probability of finding the particle in $0<x<a/2$?", 0.5, why=r"$|\psi_2|^2$ is symmetric about $a/2$."),
  M("Compared with an infinite well of the same width $2a$, the finite well's levels measured from its bottom are", ["higher", "lower", "the same", "higher for odd states, lower for even"], 1,
    "Leaking outside gives the state a longer effective width, so a longer wavelength and lower kinetic energy."),
  S(r"An infinite well has width $a$. What's $E_3-E_1$? (in terms of hbar, m, a; use pi)", "4 pi^2 hbar^2/(m a^2)", "hbar m a", r"$\dfrac{4\pi^2\hbar^2}{ma^2}$",
    r"$(9-1)\hbar^2\pi^2/2ma^2$."),
  ]),

U("general", P4, "Lecture 12", "General properties and sketching wavefunctions", "wells",
  "Rules that hold for every 1D potential, and how to sketch ψ just by looking at V.",
  [
  R("Theorems for 1D bound states", r"""
For time-independent $V(x)$ on the real line:

1. **No degenerate bound states.** Given two solutions with the same $E$, their Wronskian $\psi_1\psi_2'-\psi_2\psi_1'$ is constant, and it vanishes at infinity, so they're proportional.
2. **Real eigenfunctions.** Bound states can be chosen real (and non-degenerate ones *are* real up to a phase).
3. **Parity.** If $V(x)=V(-x)$, bound states are even or odd.
4. **No states below $V_{\min}$.** $E>V_{\min}$ for normalizable states.
5. **Node theorem.** Ordering bound states $\psi_1,\psi_2,\dots$ by energy, $\psi_n$ has exactly $n-1$ interior nodes.

Non-degeneracy doesn't apply on a circle (the boundary at infinity is missing) or to scattering states.
"""),
  C("A particle's on the full real line in a generic bound-state potential. Which are true?", ["Bound-state energies can't be degenerate", "The $n$-th state has $n-1$ nodes", "If $V$ is even every bound state is even", "$E$ can be below $V_{\\min}$ if it's far enough from the origin"], [0, 1],
    "Even $V$ gives even **or** odd states, and $E>V_{\\min}$ always."),
  R("Curving toward or away", r"""
Rewrite the TISE as $\psi''=-\dfrac{2m}{\hbar^2}(E-V)\psi$.

* **Classically allowed** ($E>V$): $\psi''$ has the opposite sign from $\psi$, so $\psi$ **curves toward the axis** and oscillates.
* **Classically forbidden** ($E<V$): $\psi''$ has the same sign as $\psi$, so $\psi$ **curves away** and grows or decays.
* **Turning point** ($E=V$): an inflection point of $\psi$.
"""),
  R("Local wavelength and amplitude", r"""
In a slowly varying potential, define the local momentum $p(x)=\sqrt{2m(E-V(x))}$ and $\lambda(x)=2\pi\hbar/p(x)$.

* Where $E-V$ is bigger, $\lambda$ is **shorter**: it oscillates faster.
* Where $E-V$ is bigger, the amplitude is **smaller**: $|\psi|\propto1/\sqrt{p(x)}$, because a fast particle spends little time there.

A sketch-grading checklist: the right number of nodes, correct parity, $\psi$ continuous and smooth, shorter wavelength and
smaller amplitude where the kinetic energy is high, inflection points at turning points, and decay in forbidden regions.
"""),
  R("Shooting method", r"""
A numerical way to find bound states of an even potential:

1. Pick a trial $E$.
2. Start at $x=0$ with $\psi(0)=1,\psi'(0)=0$ (even) or $\psi(0)=0,\psi'(0)=1$ (odd).
3. Integrate $\psi''=\frac{2m}{\hbar^2}(V-E)\psi$ out to large $x$.
4. If $\psi$ blows up, $E$ isn't an eigenvalue. The **sign of the divergence flips** as $E$ crosses an eigenvalue, so bisect.

The fact that almost all $E$ blow up is why energies are quantized.
"""),
  M(r"Near a point where $E>V(x)$, what's true of a positive $\psi$?", ["It's concave down (curves toward the axis)", "It's concave up (curves away from the axis)", "It must be flat", "It must vanish"], 0,
    r"$\psi''=-\tfrac{2m}{\hbar^2}(E-V)\psi<0$."),
  ],
  quiz=[
  M("The potential is deeper on the left half of a well than on the right. Where's a high-lying eigenstate's amplitude largest, and where's its wavelength longest?", ["Left, left", "Right, right", "Left, right", "Right, left"], 1,
    "On the right, the kinetic energy is smaller, so the particle moves slower: longer wavelength and larger amplitude."),
  N("How many nodes (excluding the walls) does the 6th excited state of a 1D potential have?", 6, why=r"6th excited is $n=7$; $n-1=6$ nodes.", qtype="conceptual"),
  ]),

U("delta", P4, "Lecture 13", "Delta potential, node theorem and oscillator wavefunctions", "wells",
  "The delta well's single bound state, and solving the oscillator as a differential equation.",
  [
  R("The delta function well", figs.delta_state() + r"""
For $V=-\alpha\delta(x)$ with $\alpha>0$, integrate the TISE across zero:

$$\psi'(0^+)-\psi'(0^-)=-\frac{2m\alpha}{\hbar^2}\psi(0).$$

For $E<0$ outside the origin $\psi=Ae^{-\kappa|x|}$, $\kappa=\sqrt{2m|E|}/\hbar$. The jump condition gives $\kappa=m\alpha/\hbar^2$:

$$E=-\frac{m\alpha^2}{2\hbar^2},\qquad\psi=\sqrt\kappa\,e^{-\kappa|x|}.$$

There's **exactly one** bound state. Note the length scale $1/\kappa=\hbar^2/m\alpha$.
Taking a finite well to zero width with $2aV_0=\alpha$ fixed gives the same answer.

Odd states vanish at $x=0$, so they feel nothing from the delta at all. For a *pair* of delta wells separated by $2L$, even and odd combinations split a level: a toy model of a molecular bond.
"""),
  S(r"For $V=-\alpha\delta(x)$, the probability of finding the particle at $|x|>x_0$ is $e^{-2\kappa x_0}$. Find it for $x_0=\hbar^2/(m\alpha)$. (a number)", "exp(-2)", [], r"$e^{-2}\approx0.135$",
    r"$\kappa x_0=1$. Integrate $2\kappa\int_{x_0}^\infty e^{-2\kappa x}dx=e^{-2\kappa x_0}$."),
  R("The oscillator's differential equation", figs.oscillator() + r"""
$V=\tfrac12m\omega^2x^2$ has a natural length $\beta=\sqrt{\hbar/m\omega}$. With $u=x/\beta$ and $\mathcal E=2E/\hbar\omega$:

$$\frac{d^2\varphi}{du^2}=(u^2-\mathcal E)\varphi.$$

At large $u$, $\varphi\sim e^{-u^2/2}$. Writing $\varphi=h(u)e^{-u^2/2}$ and expanding in a series, the series has to **terminate**,
or else $h\sim e^{u^2}$ blows up. Termination forces $\mathcal E=2n+1$:

$$E_n=\hbar\omega\left(n+\tfrac12\right),\qquad n=0,1,2,\dots$$

The polynomials are Hermite polynomials, with $H_0=1$, $H_1=2u$, $H_2=4u^2-2$.

The states alternate parity, $\varphi_n(-x)=(-1)^n\varphi_n(x)$, and leak into the forbidden region past $x_{tp}=\beta\sqrt{2n+1}$.
"""),
  S(r"What is the classical turning point of the oscillator in its ground state? (in terms of hbar, m, omega)", "sqrt(hbar/(m omega))", "hbar m omega", r"$\beta=\sqrt{\hbar/m\omega}$",
    r"$\tfrac12m\omega^2x^2=\tfrac12\hbar\omega$."),
  ],
  quiz=[
  N("How many bound states does a single attractive delta potential have?", 1, why="The jump condition fixes $\\kappa$ uniquely, and odd states don't feel it.", qtype="conceptual"),
  N(r"For $V=-\alpha\delta(x)$, what's the ratio of the new bound-state energy to the old one when $\alpha\to2\alpha$?", 4,
    why=r"$E\propto\alpha^2$."),
  ]),

U("sho", P4, "Lectures 14–15", "Algebraic solution of the oscillator", "oscillator",
  "Ladder operators solve the oscillator without any differential equations, and make expectation values almost trivial.",
  [
  R("Factoring the Hamiltonian", r"""
Define

$$\hat a=\sqrt{\frac{m\omega}{2\hbar}}\left(\hat x+\frac{i\hat p}{m\omega}\right),\qquad\hat a^\dagger=\sqrt{\frac{m\omega}{2\hbar}}\left(\hat x-\frac{i\hat p}{m\omega}\right).$$

Then $[\hat a,\hat a^\dagger]=1$ and

$$\hat H=\hbar\omega\left(\hat a^\dagger\hat a+\tfrac12\right)=\hbar\omega\left(\hat N+\tfrac12\right).$$

Since $\hat N=\hat a^\dagger\hat a$ has $\langle N\rangle=\|a\psi\|^2\ge0$, the spectrum is bounded from below.

$[\hat N,\hat a]=-\hat a$ and $[\hat N,\hat a^\dagger]=\hat a^\dagger$ mean that $\hat a^\dagger$ raises $N$ by 1, and $\hat a$ lowers it.
The tower must stop at a state $\hat a\varphi_0=0$, whose energy is $\hbar\omega/2$.
"""),
  R("The ladder", r"""
$$\hat a^\dagger\varphi_n=\sqrt{n+1}\,\varphi_{n+1},\qquad\hat a\varphi_n=\sqrt n\,\varphi_{n-1},\qquad\varphi_n=\frac{(\hat a^\dagger)^n}{\sqrt{n!}}\varphi_0.$$

Solving $\hat a\varphi_0=0$ as a differential equation yields the Gaussian ground state
$\varphi_0=\left(\dfrac{m\omega}{\pi\hbar}\right)^{1/4}e^{-m\omega x^2/2\hbar}$.

To remember the factors: **the square root is always of the larger of the two levels involved**.
"""),
  N(r"What number multiplies $\varphi_4$ in $\hat a^\dagger\hat a^\dagger\varphi_2$?", (3*4)**0.5,
    why=r"$\sqrt3\sqrt4=\sqrt{12}\approx3.46$."),
  R("Computing expectation values", r"""
Express $\hat x$ and $\hat p$ with ladder operators, then count steps:

$$\hat x=\sqrt{\frac{\hbar}{2m\omega}}(\hat a+\hat a^\dagger),\qquad\hat p=i\sqrt{\frac{m\omega\hbar}{2}}(\hat a^\dagger-\hat a).$$

**Rule of thumb:** a term contributes to $\langle\varphi_m,\dots\varphi_n\rangle$ only if it has a net $m-n$ raising operators.
Odd powers of $\hat x$ have zero expectation in an eigenstate.

Results:

$$\langle x^2\rangle_n=\frac{\hbar}{2m\omega}(2n+1),\qquad\langle p^2\rangle_n=\frac{m\hbar\omega}{2}(2n+1).$$

So $\langle T\rangle=\langle V\rangle=E_n/2$ (the virial theorem), and $\Delta x\Delta p=\hbar(n+\tfrac12)$. Ground state saturates the bound.
"""),
  S(r"In the ground state, what's $\langle x^2\rangle$? (in terms of hbar, m, omega)", "hbar/(2 m omega)", "hbar m omega", r"$\dfrac{\hbar}{2m\omega}$",
    r"$\tfrac{\hbar}{2m\omega}\langle0|(a+a^\dagger)^2|0\rangle=\tfrac{\hbar}{2m\omega}$."),
  R("Time evolution and classical motion", r"""
$\Psi=\tfrac{1}{\sqrt2}(\varphi_0+\varphi_1)$ gives an oscillating $\langle x\rangle\propto\cos\omega t$. Only adjacent levels contribute to $\langle x\rangle$, since $\hat x$ changes $n$ by $\pm1$. So
$\langle x\rangle$ always oscillates at the classical frequency, in agreement with Ehrenfest.

A superposition of $\varphi_0$ and $\varphi_2$ has $\langle x\rangle=0$ for all time, while $|\Psi|^2$ itself oscillates at $2\omega$.
"""),
  ],
  quiz=[
  N(r"Evaluate $\langle\varphi_1|\hat a^\dagger\hat a|\varphi_1\rangle$.", 1, why=r"$\hat N\varphi_1=\varphi_1$."),
  M(r"A state $\tfrac{1}{\sqrt2}(\varphi_1+\varphi_4)$: is $\langle x\rangle$ time dependent?", ["Yes, at $\\omega$", "Yes, at $3\\omega$", "No, it's zero for all time", "No, but nonzero"], 2,
    r"$\hat x$ only connects levels that differ by 1, and 1 and 4 differ by 3, and diagonal terms vanish."),
  S(r"Find $\langle\varphi_0|\hat x^4|\varphi_0\rangle$. (in terms of hbar, m, omega)", "3 (hbar/(2 m omega))^2", "hbar m omega", r"$3\left(\dfrac{\hbar}{2m\omega}\right)^2$",
    r"$(a+a^\dagger)^4$ between ground states: paths $aaa^\dagger a^\dagger$ gives 2, and $aa^\dagger aa^\dagger$ gives 1, total 3."),
  ]),

U("step", P5, "Lecture 16", "Scattering states and the step potential", "scattering",
  "Energy eigenstates that aren't normalizable, reflection and transmission, and the surprise of quantum reflection.",
  [
  R("Scattering states", r"""
For $E$ above the asymptotic potential, solutions are plane waves, not normalizable. They become physical through wavepackets.
They carry a **current**, so we compare currents, not amplitudes. Coefficients:

$$R=\frac{J_{\text{ref}}}{J_{\text{inc}}},\qquad T=\frac{J_{\text{trans}}}{J_{\text{inc}}},\qquad R+T=1.$$

$E$ is continuous here, and degeneracy is now possible: two independent solutions per $E$ where both sides are open.
"""),
  R("Step, E > V₀", figs.step_T() + r"""
Let $V=0$ for $x<0$ and $V=V_0$ for $x>0$. Incident from the left:

$$\psi=\begin{cases}e^{ikx}+re^{-ikx},&x<0\\te^{ik'x},&x>0\end{cases},\quad k=\frac{\sqrt{2mE}}{\hbar},\ k'=\frac{\sqrt{2m(E-V_0)}}{\hbar}.$$

Continuity of $\psi$ and $\psi'$ give

$$r=\frac{k-k'}{k+k'},\qquad t=\frac{2k}{k+k'},\qquad R=r^2,\qquad T=\frac{k'}{k}t^2=\frac{4kk'}{(k+k')^2}.$$

**Note the factor of $k'/k$**: $T\neq|t|^2$ when velocities differ. Classically $R=0$ for $E>V_0$: this reflection is purely quantum,
and it's the same if the wave comes from the right.
"""),
  N(r"A step has $E=\tfrac{4}{3}V_0$. What is $R$?", (1-0.5)**2/(1+0.5)**2, tol=0.01,
    why=r"$k'/k=\sqrt{(E-V_0)/E}=\sqrt{1/4}=1/2$, so $R=\left(\frac{1-1/2}{1+1/2}\right)^2=\frac19$."),
  R("Step, E < V₀", r"""
Now the wave decays, $\psi=te^{-\kappa x}$ for $x>0$ with $\kappa=\sqrt{2m(V_0-E)}/\hbar$. Continuity gives $r=\frac{k-i\kappa}{k+i\kappa}$,
a pure phase: $R=1$. So all probability reflects, though the wavefunction penetrates a distance $\sim1/\kappa$.

A decaying exponential carries no current, which is why $T=0$. The phase of $r$ leads to a **time delay** for a reflected packet, which you find by stationary phase: delay is $\dfrac{2m}{\hbar k\kappa}$.
"""),
  R("Tunneling and the rectangular barrier", r"""
For a barrier of height $V_0$ and width $2a$ with $0<E<V_0$, the transmission is nonzero even though classically forbidden:

$$T^{-1}=1+\frac{V_0^2}{4E(V_0-E)}\sinh^2(2\kappa a),\qquad\text{so }T\sim e^{-4\kappa a}\text{ for a thick barrier}.$$

Thick barriers transmit exponentially little. For a delta barrier $V=g\delta(x)$:

$$T=\frac{1}{1+\dfrac{mg^2}{2\hbar^2E}}.$$

Waves from the left and right have the same $T$: this is a general property, called reciprocity, for any $V(x)$.
"""),
  ],
  quiz=[
  M("For a step with $E<V_0$, what is $J$ in the region $x>0$?", ["Positive", "Zero", "Negative", "Oscillates in time"], 1,
    "A real function times a constant has zero current, and the current must match with $1-R=0$ on the left."),
  S(r"For a delta barrier, what's $T$ when $E=mg^2/(2\hbar^2)$? (a number)", "1/2", [], r"$\tfrac12$", r"The ratio in the denominator is exactly 1."),
  M("When is a step's reflection the largest (for $E>V_0$)?", ["$E\\gg V_0$", "$E$ just above $V_0$", "$E=2V_0$", "It's independent of $E$"], 1, r"$k'\to0$ gives $r\to1$."),
  ]),

U("resonant", P5, "Lecture 17", "Resonant transmission and Ramsauer–Townsend", "scattering",
  "An attractive well can be perfectly transparent at special energies. See why, and how the effect shows up in real gases.",
  [
  R("Scattering off a well", figs.ramsauer() + r"""
For a well of depth $V_0$, width $2a$, and $E>0$, let $k_2=\sqrt{2m(E+V_0)}/\hbar$. Solving four boundary conditions gives

$$\frac1T=1+\frac{V_0^2}{4E(E+V_0)}\sin^2(2k_2a).$$

**$T=1$ whenever $\sin(2k_2a)=0$, that is, $2k_2a=n\pi$.** The well then holds a whole number of half wavelengths, so the reflections from the front and back cancel:
a thin-film interference effect. The energies are

$$E_n=\frac{n^2\pi^2\hbar^2}{2m(2a)^2}-V_0,$$

infinite-well levels with the bottom at $-V_0$. Note how $T\to0$ as $E\to0$, and $T\to1$ at high energies.
Lowest available $n$ for this formula needs $E_n>0$.
"""),
  S(r"Given the formula, find the minimum value of $T$ for a fixed $E$ as $a$ is varied. (in terms of E, V0)", "4 E (E+V0)/(4 E (E+V0)+V0^2)", "E V0", r"$\dfrac{4E(E+V_0)}{(2E+V_0)^2}$",
    r"Set $\sin^2=1$. And $4E(E+V_0)+V_0^2=(2E+V_0)^2$."),
  R("Ramsauer–Townsend effect", r"""
Slow electrons scattering from noble gas atoms show a striking minimum in the cross section near 1 eV: the atom becomes nearly invisible.
Noble gas atoms act as short-range attractive wells on electrons. So the effect comes from the same resonance physics, though the real problem's in 3D.

Why noble gases? Their closed shells keep the effective potential sharp-edged and short-range, as the model assumes.
"""),
  N(r"A well has $V_0=5$ eV and transmission resonances at $2k_2a=n\pi$. If $E_n+V_0$ for $n=1$ is 1 eV, what's $E+V_0$ for $n=4$, in eV?", 16, "eV", why=r"$E+V_0\propto n^2$, so $16\times1$ eV."),
  ],
  quiz=[
  M("At a resonant-transmission energy, what's the relationship between the well's width $L=2a$ and internal wavelength $\\lambda_2$?", [r"$L=n\lambda_2$", r"$L=n\lambda_2/2$", r"$L=(n+\tfrac12)\lambda_2$", r"$L=n\lambda_2/4$"], 1, r"$k_2L=n\pi$ means $2\pi L/\lambda_2=n\pi$."),
  M("Can a repulsive barrier with $E>V_0$ have $T=1$?", ["Never", "Yes, at special energies", "Only at infinite energy", "Only for delta barriers"], 1,
    r"Replace $V_0\to-V_0$ in the formula. There's still $\sin^2(2k_2a)=0$ with the barrier's $k_2$."),
  ]),

U("halfline", P5, "Lecture 18", "Scattering phase shifts and time delay", "phaseshift",
  "Scattering on a half-line reduces everything to one real function, the phase shift δ(k).",
  [
  R("The setup", r"""
Put a wall at $x=0$ and a potential of range $R$. There's no transmission: every wave returns, so all the information is in the **phase** of the reflected wave. With no potential:

$$\phi(x)=\sin kx=\frac{1}{2i}\left(e^{ikx}-e^{-ikx}\right).$$

With a potential, outside its range we keep the same incoming wave:

$$\psi(x)=\frac{1}{2i}\left(e^{ikx+2i\delta(k)}-e^{-ikx}\right)=e^{i\delta}\sin(kx+\delta),\qquad x>R.$$

Current conservation requires the outgoing phase to be pure, so $\delta(k)$ is real. Only $2\delta$ matters, and thus $\delta$ matters mod $\pi$.

Solving problems: find $\psi$ inside, match to $\sin(kx+\delta)$ at $x=R$, and read off $\delta$.
"""),
  R("Time delay", r"""
Build an incoming packet from $\int dk\,f(k)e^{-ikx-iE(k)t/\hbar}$, peaked at $k_0$. The outgoing one has an extra $e^{2i\delta(k)}$.

Stationary phase gives the outgoing motion $x=v_g(t-2\hbar\,\delta'(E))$:

$$\Delta t=2\hbar\left.\frac{d\delta}{dE}\right|_E=\frac{2m}{\hbar k}\frac{d\delta}{dk}.$$

If $\Delta t<0$, the packet returned early. In units of the free round-trip transit time $\bar\tau=2R/v$,

$$\frac{\Delta t}{\bar\tau}=\frac{1}{R}\frac{d\delta}{dk}.$$

An attractive potential speeds the particle up, so it arrives early. In the simple case of a hard wall moved in by $L$, you get $\delta=-kL$, which is an advance.
"""),
  S(r"An infinite wall at $x=L$ instead of $x=0$ means $\psi=\sin(k(x-L))$. What is $\delta(k)$? (in terms of k, L)", "-k L", "k L", r"$\delta=-kL$",
    r"Compare with $\sin(kx+\delta)$. Then $\Delta t=-2L/v$, exactly the shortened round trip."),
  R("The scattered wave", r"""
Define the scattered wave as the difference between actual and free solutions:

$$\psi=\phi+\psi_s,\qquad\psi_s=A_se^{ikx},\qquad A_s=e^{i\delta}\sin\delta.$$

So $|A_s|^2=\sin^2\delta$ is largest when $\delta=(n+\tfrac12)\pi$. Scattering is strongest at those phases, and vanishes when $\delta=n\pi$.

**Example.** A well of depth $V_0$ on $0<x<R$ next to a wall: $\psi=\sin k'x$ inside, with $k'^2=k^2+2mV_0/\hbar^2$. Matching log derivatives at $R$:

$$k'\cot k'R=k\cot(kR+\delta).$$

This one equation gives $\delta(k)$ implicitly.
"""),
  N(r"If $\delta=\pi/4$, what's the value of $|A_s|^2$?", 0.5, why=r"$\sin^2(\pi/4)=1/2$."),
  ],
  quiz=[
  S(r"With $\delta(k)=\arctan(c/k)$ for a positive constant $c$, what's $d\delta/dk$? (in terms of c, k)", "-c/(k^2+c^2)", "c k", r"$-\dfrac{c}{k^2+c^2}$",
    r"$\frac{d}{dk}\arctan(c/k)=\frac{1}{1+c^2/k^2}\cdot(-c/k^2)$."),
  M("Why is $\\delta$ real for a real potential in this setup?", ["Energy conservation only", "Probability current in equals out, since the wall blocks transmission", "Because $\\psi$ is normalizable", "Because $k$ is real"], 1,
    r"$|A_{\text{out}}|=|A_{\text{in}}|$ means the ratio's a pure phase."),
  ]),

U("levinson", P5, "Lecture 19", "Levinson's theorem and resonances", "phaseshift",
  "The phase shift counts bound states, and rapid phase growth signals a long-lived quasi-bound state.",
  [
  R("Levinson's theorem", r"""
Put the system in a big box to count states, and compare with no potential. Turning on a potential pulls states out of the continuum into bound states,
so the count of states relates to the phase. The result:

$$N_{\text{bound}}=\frac{1}{\pi}\left(\delta(0)-\delta(\infty)\right).$$

Attractive potentials hold bound states when strong enough. As the well deepens past a threshold, a new bound state appears and $\delta(0)$ jumps by $\pi$.
This relies on $\delta$ being chosen continuous in $k$, and you need a convention for $\delta(\infty)$ (usually 0).
"""),
  N(r"With continuous $\delta$, one finds $\delta(0)=3\pi$ and $\delta(\infty)=0$. How many bound states are there?", 3, why=r"$N=3\pi/\pi$.", qtype="conceptual"),
  R("Resonances", figs.resonance_delta() + r"""
A **resonance** is a rapid increase of $\delta$ by about $\pi$ near some $k_0$. A particle gets trapped behind a barrier for a long time, in a quasi-bound state.
The signatures are all equivalent:

* Rapid growth in $\delta$, so **large positive time delay** $\Delta t$.
* A **large amplitude inside** the potential.
* A peak in $\sin^2\delta$ near $\delta=\pi/2$ (mod $\pi$).

Near a resonance the phase behaves as $\tan(\delta-\delta_b)=\dfrac{\beta}{\alpha-k}$, so the scattering amplitude is approximately

$$A_s\propto\frac{\Gamma/2}{E_0-E-i\Gamma/2},\qquad|A_s|^2\propto\frac{1}{(E-E_0)^2+\Gamma^2/4}.$$

That's the **Breit–Wigner** shape: $\Gamma$ is the full width at half maximum.
"""),
  R("Lifetime", r"""
The time delay at the peak is $\Delta t=2\hbar\,d\delta/dE$. Near a resonance, $d\delta/dE$ peaks at $2/\Gamma$, so

$$\Delta t\Big|_{E_0}=\frac{4\hbar}{\Gamma},\qquad\tau=\frac{\hbar}{\Gamma}.$$

Here $\tau$ is the **lifetime** for the trapped probability to decay as $e^{-t/\tau}$. **Narrow resonance means a long lifetime**. It's an energy-time uncertainty relation.

A resonance corresponds to a pole of the amplitude at complex energy $E_0-i\Gamma/2$. It's a state with a decaying time factor $e^{-iE_0t/\hbar}e^{-\Gamma t/2\hbar}$, and this gives probability $\propto e^{-\Gamma t/\hbar}$.
"""),
  N(r"A resonance has width $\Gamma=6.6\times10^{-7}$ eV. With $\hbar=6.6\times10^{-16}$ eV·s, what's the lifetime in ns?", 1, "ns", why=r"$\tau=\hbar/\Gamma=10^{-9}$ s."),
  ],
  quiz=[
  C("Which signals a resonance?", ["Large positive time delay", "Rapid decrease of $\\delta$ with $k$", "Large inner amplitude", "A true bound state with $E<0$"], [0, 2],
    "Resonances have $\\delta$ *increasing* rapidly, and they're at positive energy (quasi-bound)."),
  S(r"At the peak of a Breit–Wigner, what's the time delay, in terms of the lifetime $\tau=\hbar/\Gamma$? (in terms of tau)", "4 tau", "tau", r"$4\tau$", r"$4\hbar/\Gamma$."),
  ]),

U("angular", P6, "Lectures 20–21", "Angular momentum and spherical harmonics", "angular",
  "Quantum mechanics in 3D: L operators, their commutators, and the eigenstates Y_lm.",
  [
  R("3D and the angular momentum operators", r"""
With $\hat{\vec p}=\frac\hbar i\nabla$, we have $[\hat x_i,\hat p_j]=i\hbar\delta_{ij}$. Angular momentum $\hat{\vec L}=\hat{\vec x}\times\hat{\vec p}$ gives $\hat L_z=\hat x\hat p_y-\hat y\hat p_x$, and cyclic permutations.

The essential algebra:

$$[\hat L_x,\hat L_y]=i\hbar\hat L_z\ \text{(and cyclic)},\qquad[\hat L^2,\hat L_i]=0.$$

So components **don't commute with each other**: you can't simultaneously know $L_x$ and $L_z$, unless the state has $\vec L=0$. **But** $L^2$ and one component, $L_z$ by convention, can be measured together.

For any central potential $V(r)$: $[\hat H,\hat L_i]=0$. So we label states by energy, $L^2$ and $L_z$.

Quick rule: $[\hat L_i,\hat x_j]=i\hbar\epsilon_{ijk}\hat x_k$, and the same with $\hat p_j$.
"""),
  M(r"What is $[\hat L_z,\hat x]$?", [r"$0$", r"$i\hbar\hat y$", r"$-i\hbar\hat y$", r"$i\hbar\hat z$"], 1,
    r"$[xp_y-yp_x,x]=-y[p_x,x]=i\hbar y$."),
  R("Eigenstates and spherical harmonics", r"""
Simultaneous eigenfunctions $Y_{\ell m}(\theta,\phi)$:

$$\hat L^2Y_{\ell m}=\hbar^2\ell(\ell+1)Y_{\ell m},\qquad\hat L_zY_{\ell m}=\hbar mY_{\ell m}.$$

With $\ell=0,1,2,\dots$ and $m=-\ell,\dots,\ell$ ($2\ell+1$ values). Since $\hat L_z=\frac\hbar i\partial_\phi$, $Y_{\ell m}\propto e^{im\phi}$, and single-valuedness forces integer $m$.

$$Y_{00}=\frac{1}{\sqrt{4\pi}},\quad Y_{10}=\sqrt{\frac{3}{4\pi}}\cos\theta,\quad Y_{1,\pm1}=\mp\sqrt{\frac{3}{8\pi}}\sin\theta\,e^{\pm i\phi}.$$

They're orthonormal over the sphere, with $d\Omega=\sin\theta\,d\theta\,d\phi$.

Note that $|m|\le\ell$ and $\sqrt{\ell(\ell+1)}>\ell$: the vector can't align fully with $z$, or else $L_x$ and $L_y$ would both be zero too.

**Ladder operators** $\hat L_\pm=\hat L_x\pm i\hat L_y$ shift $m$ by $\pm1$. The top state satisfies $\hat L_+Y_{\ell\ell}=0$, and $Y_{\ell\ell}\propto\sin^\ell\theta\,e^{i\ell\phi}$.
"""),
  S(r"A state has $\ell=2$. What's the magnitude $\sqrt{\langle L^2\rangle}$? (in terms of hbar)", "sqrt(6) hbar", "hbar", r"$\sqrt6\,\hbar$", r"$\ell(\ell+1)=6$."),
  R("Decomposing an angular state", r"""
To find $L_z$ outcomes, expand in $e^{im\phi}$. For example, $\psi\propto\sin\theta\cos\phi$ has $\cos\phi=\tfrac12(e^{i\phi}+e^{-i\phi})$, so it's a superposition of $m=\pm1$ with equal weights, and it has $\ell=1$.

$\sin^2\theta$ terms etc. may mix $\ell$, but the $\phi$ part alone gives you $m$.
"""),
  C(r"A particle on a sphere is in $\psi\propto\sin\theta\cos\phi$. Select all possible outcomes of measuring $L_z$.", [r"$+\hbar$", r"$0$", r"$-\hbar$", r"$2\hbar$"], [0, 2],
    r"$\cos\phi=\tfrac12(e^{i\phi}+e^{-i\phi})$."),
  ],
  quiz=[
  N(r"How many states share $\ell=4$?", 9, why=r"$2\ell+1$.", qtype="conceptual"),
  M(r"Can a nonzero-$\ell$ state be an eigenstate of both $\hat L_x$ and $\hat L_z$?", ["Yes, always", "Yes, when $m=\\ell$", "No, since $\\langle[\\hat L_x,\\hat L_y]\\rangle$-type constraints force $\\vec L=0$", "Only for even $\\ell$"], 2,
    r"Simultaneous eigenstates of two components must be annihilated by the third, and this implies $\ell=0$."),
  ]),

U("radial", P6, "Lectures 20–21", "Central potentials and the radial equation", "angular",
  "Separate r from angles. The radial problem looks like a 1D problem with an effective potential.",
  [
  R("Separation in central potentials", figs.veff() + r"""
With $V=V(r)$, write $\psi=\dfrac{u(r)}{r}Y_{\ell m}(\theta,\phi)$. The radial equation becomes a 1D-like problem:

$$\left[-\frac{\hbar^2}{2m}\frac{d^2}{dr^2}+V(r)+\frac{\hbar^2\ell(\ell+1)}{2mr^2}\right]u=Eu,\qquad V_{\text{eff}}(r)=V+\frac{\hbar^2\ell(\ell+1)}{2mr^2}.$$

The extra term is the **centrifugal barrier**. Note that the normalization simplifies to $\int_0^\infty|u|^2dr=1$. Key points:

* $m$ doesn't appear, so each $\ell$ has $2\ell+1$ degenerate states.
* Boundary condition at the origin: **$u(0)=0$**, and $u\sim r^{\ell+1}$.
* So $u$ for $\ell=0$ acts like an odd state in 1D. **A shallow 3D well may have no bound states at all**, unlike in 1D.
* $P(r)=|u|^2$ is the radial probability density.
"""),
  R("Free particle and spherical wells", r"""
For an **infinite spherical well** of radius $a$ with $\ell=0$, $u''=-k^2u$, with $u(0)=u(a)=0$:

$$u=\sqrt{\frac{2}{a}}\sin\frac{n\pi r}{a},\quad E=\frac{\hbar^2n^2\pi^2}{2ma^2},\ \text{so}\ \psi=\frac{1}{\sqrt{4\pi}}\frac{u}{r}.$$

Higher $\ell$ gives zeros of spherical Bessel functions. For fixed $\ell$, the levels are ordered by radial quantum number, and raising $\ell$ raises the energy.

A **finite spherical well** with $\ell=0$ is the same as an odd state in a 1D finite well. There's a bound state only if $z_0>\pi/2$.
"""),
  N(r"For $\ell=0$, a finite spherical well has $z_0^2=2mV_0a^2/\hbar^2$. What's the smallest $z_0$ with a bound state? (Give a number.)", 3.14159265/2, why=r"It's the odd condition: the first odd state appears at $z_0=\pi/2$."),
  S(r"What does $u$ behave like at small $r$ for $\ell=3$? Give the power $n$ in $u\sim r^n$. (a number)", "4", [], r"$4$", r"$u\sim r^{\ell+1}$."),
  R("Three-dimensional boxes and degeneracy", r"""
In Cartesian boxes, separate as $X(x)Y(y)Z(z)$, with $E=E_x+E_y+E_z$. A square box $L_x=L_y$ has degeneracy $(n_1,n_2)\leftrightarrow(n_2,n_1)$, since it's symmetric.

Degeneracies always signal a symmetry. **Lifting symmetry usually lifts degeneracy.** Accidental degeneracies, such as $5^2+5^2=1^2+7^2$, also occur.
"""),
  ],
  quiz=[
  M(r"Why's the requirement $u(0)=0$ imposed?", ["Otherwise $\\psi\\sim1/r$ is not a solution at the origin", "Because $E$ must be positive", "Because $V(r)$ is infinite at zero", "It's not needed for $\\ell=0$"], 0,
    r"$\nabla^2(1/r)\propto\delta^3(\vec r)$, which wouldn't be balanced in the TISE."),
  S(r"What's the ground state energy of a particle in a cubic box of side $L$? (in terms of hbar, m, L; use pi)", "3 pi^2 hbar^2/(2 m L^2)", "hbar m L", r"$\dfrac{3\pi^2\hbar^2}{2mL^2}$", r"$(1,1,1)$."),
  ]),

U("hydrogen", P6, "Lectures 21–22", "The hydrogen atom", "hydrogen",
  "The spectrum, its huge degeneracy, the wavefunctions, and how to compute with them.",
  [
  R("Scales and the spectrum", r"""
With $V=-Ze^2/r$ (Gaussian units), we find the length and energy scales:

$$a_0=\frac{\hbar^2}{m e^2}\approx0.529\text{ Å},\qquad\frac{e^2}{2a_0}\approx13.6\text{ eV},\qquad\alpha=\frac{e^2}{\hbar c}\approx\frac{1}{137}.$$

Energies:

$$E_n=-\frac{Z^2e^2}{2a_0n^2}=-\frac{13.6\ Z^2\text{ eV}}{n^2},\qquad a_0=\frac{\hbar}{m_ec\,\alpha},\qquad\frac{e^2}{2a_0}=\frac12\alpha^2m_ec^2.$$

Quantum numbers: $n=1,2,\dots$; $\ell=0,\dots,n-1$; $m=-\ell,\dots,\ell$. **The degeneracy is $n^2$** (or $2n^2$ with spin).

That's far beyond rotational symmetry alone, which would only give $2\ell+1$: different $\ell$ having the same energy is special to $1/r$ (a hidden symmetry related to the Runge–Lenz vector).
"""),
  N("What's the wavelength in nm of the photon emitted in the $n=3\\to2$ transition (H-alpha)? Use 13.6 eV and $hc=1240$ eV·nm.", 1240/(13.6*(1/4-1/9)), "nm",
    why=r"$\Delta E=13.6(1/4-1/9)=1.89$ eV, so $\lambda\approx656$ nm."),
  N(r"What's the degeneracy of hydrogen's $n=3$ level (ignoring spin)?", 9, why=r"$\ell=0,1,2$ gives $1+3+5$.", qtype="conceptual"),
  R("Wavefunctions", figs.hydrogen_radial() + r"""
The radial functions are

$$u_{1,0}=\frac{2r}{a_0^{3/2}}e^{-r/a_0},\qquad u_{2,0}=\frac{2r}{(2a_0)^{3/2}}\left(1-\frac{r}{2a_0}\right)e^{-r/2a_0},\qquad u_{2,1}=\frac{1}{\sqrt3}\frac{r}{(2a_0)^{3/2}}\frac{r}{a_0}e^{-r/2a_0}.$$

In general: $\psi_{n\ell m}=\dfrac{u_{n\ell}}{r}Y_{\ell m}$, $u_{n\ell}\sim r^{\ell+1}\times$(polynomial)$\times e^{-Zr/na_0}$, and the polynomial has **$n-\ell-1$ radial nodes**.

For the maximal $\ell=n-1$, there are no radial nodes: $P(r)\propto r^{2n}e^{-2r/na_0}$, which peaks at $r=n^2a_0$. These are the circular orbits.

Hydrogen-like ions: $a_0\to a_0/Z$, $E\to Z^2E$.
"""),
  S(r"Using $P(r)=|u_{1,0}|^2$, where's the most probable radius of $1s$? (in terms of a0)", "a0", "a0", r"$a_0$",
    r"$P\propto r^2e^{-2r/a_0}$, whose derivative vanishes at $r=a_0$."),
  R("Expectation values and time dependence", r"""
For a superposition $\sum c_{n\ell m}\psi_{n\ell m}$:

* $\langle H\rangle=\sum|c|^2E_n$, $\langle L^2\rangle=\sum|c|^2\hbar^2\ell(\ell+1)$, $\langle L_z\rangle=\sum|c|^2\hbar m$. All are constant in time, as $H,L^2,L_z$ commute.
* Results for $r$ depend on which states mix.
* The density oscillates at Bohr frequencies, e.g. $\omega_{21}=\frac{E_2-E_1}{\hbar}$.

Useful expectation values: $\langle r\rangle_{1s}=\tfrac32a_0$ and $\langle1/r\rangle_{n\ell}=\dfrac{Z}{a_0n^2}$.

**Virial theorem** for $V\propto1/r$: $\langle T\rangle=-\tfrac12\langle V\rangle=-E_n$. So 13.6 eV is the ground-state kinetic energy, and $\langle V\rangle=-27.2$ eV.
"""),
  ],
  quiz=[
  N(r"He$^+$ ($Z=2$) has what ground state energy, in eV?", -54.4, "eV", why=r"$-13.6Z^2$."),
  N(r"What's the ionization energy of hydrogen in its $n=2$ state, in eV?", 3.4, "eV", why=r"$13.6/4$."),
  M(r"How many radial nodes does the $3p$ state have?", ["0", "1", "2", "3"], 1, r"$n-\ell-1=3-1-1=1$."),
  ]),
]
