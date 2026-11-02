"""Original mock exams and drills, written for this site in the style of past 8.04 exams."""
import math
from dsl import P, E, N, S, M, C, B
import figs

pi = math.pi
HC, HBC, ME, RY = 1240.0, 197.3, 0.511e6, 13.6
well_scale = 2 * ME * 0.1**2 / HBC**2  # z0^2 per eV for an electron with a = 0.1 nm

MID1A = E("m1a", "Midterm 1 · Mock A", "midterm", "Covers Lectures 1–9. Suggested time: 90 minutes.", [
P("Problem 1: Scales and quick estimates", "matterwaves", r"""
Use $\hbar c\simeq197.3$ MeV·fm, $hc\simeq1240$ eV·nm and $m_ec^2\simeq0.511$ MeV. A muon has $m_\mu c^2\simeq106$ MeV.
""", [
  N("**(a)** What's the muon's reduced Compton wavelength $\\hbar/m_\\mu c$, in fm?", HBC/106, "fm", why=r"$\hbar c/m_\mu c^2=197.3/106\approx1.86$ fm."),
  N("**(b)** A nonrelativistic electron has kinetic energy 25 eV. What's its de Broglie wavelength, in nm?", HC/(2*ME*25)**.5, "nm", why=r"$pc=\sqrt{2(5.11\times10^5)(25)}\approx5055$ eV, so $\lambda=1240/5055\approx0.245$ nm."),
  N("**(c)** An electron and a proton have the same kinetic energy, both nonrelativistic. What's $\\lambda_e/\\lambda_p$? (Use $m_pc^2=938$ MeV.)", (938/0.511)**.5, tol=.02, why=r"$\lambda\propto1/\sqrt m$, so $\sqrt{938/0.511}\approx42.8$."),
  M("**(d)** Which experiment most directly shows that photons carry momentum?", ["Photoelectric effect", "Compton scattering", "Davisson–Germer electron diffraction", "Two-slit interference"], 1, "The wavelength shift follows from energy and momentum conservation for a photon–electron collision."),
]),
P("Problem 2: Interferometer with a partial filter", "foundations", figs.mach_zehnder() + r"""
Take $\text{BS1}=\tfrac{1}{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}$ and $\text{BS2}=\tfrac{1}{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}$, with the photon entering as $\binom10$ and with D0 the upper output, D1 the lower output.

A filter in the lower branch absorbs each arriving photon with probability $1-T$ and otherwise passes it, multiplying that amplitude by $\sqrt T$, where $0\le T\le1$.
""", [
  S("**(a)** What's the probability that the photon is absorbed? (in terms of T)", "(1-T)/2", "T", r"$(1-T)/2$", r"After BS1 the lower amplitude is $1/\sqrt2$, so the photon arrives at the filter with probability 1/2.", ranges={"T": [.1, .9]}),
  S("**(b)** What's $P_0$? (in terms of T)", "(1+sqrt(T))^2/4", "T", r"$(1+\sqrt T)^2/4$", r"The final state is $\tfrac12\binom{1+\sqrt T}{-1+\sqrt T}$.", ranges={"T": [.1, .9]}),
  S("**(c)** What's $P_1$? (in terms of T)", "(1-sqrt(T))^2/4", "T", r"$(1-\sqrt T)^2/4$", r"Check: $P_0+P_1+P_{\text{abs}}=\tfrac{2+2T}{4}+\tfrac{1-T}{2}=1$.", ranges={"T": [.1, .9]}),
  B("**(d)** Explain the $T=0$ and $T=1$ limits physically. Why does a click at D1 require that the filter be able to absorb?",
    r"$T=1$: no filter, perfect interference, $P_1=0$. $T=0$: the filter fully blocks the branch, so there's no interference. $P_1=1/4$. D1 fires only if the two paths' amplitudes fail to cancel; absorbing changes the lower amplitude's magnitude, so the cancellation is incomplete."),
]),
P("Problem 3: A wavefunction with current", "schrodinger", r"""
At $t=0$, a particle of mass $m$ has $\Psi(x)=N(x+ib)e^{-x^2/2a^2}$, with real positive $N,a,b$.
""", [
  S(r"**(a)** Find the probability current $J(x,0)$. Treat $N$ as a variable. (in terms of hbar, m, N, b, x, a)", "-hbar b N^2 exp(-x^2/a^2)/m", "hbar m N b x a", r"$J=-\dfrac{\hbar b}{m}N^2e^{-x^2/a^2}$",
    r"With $f=x+ib$ and real $g$: $\Psi^*\Psi'=g(|f|^2g'+f^*f'g)$, and only $f^*f'=x-ib$ has an imaginary part: $\text{Im}=-b\,g^2$."),
  M("**(b)** At $t=0$, in what direction does probability flow, at every point?", ["Toward $+x$", "Toward $-x$", "Outward from the origin", "It doesn't flow"], 1, r"$J<0$ everywhere."),
  M(r"**(c)** How does $\partial\rho/\partial t$ behave at $x=0$, $t=0$?", ["Positive", "Negative", "Zero", "Can't tell"], 2, r"$\partial_t\rho=-\partial_xJ\propto-x\,e^{-x^2/a^2}$, which vanishes at $x=0$. Density falls for $x>0$ and rises for $x<0$, so the packet shifts left."),
]),
P("Problem 4: A moving Gaussian", "wavepackets", r"""
Let $\Psi(x)=\left(\dfrac{1}{\pi a^2}\right)^{1/4}e^{-x^2/2a^2}e^{ik_0x}$, for a free particle of mass $m$.
""", [
  S(r"**(a)** $\Delta x$? (in terms of a)", "a/sqrt(2)", "a", r"$a/\sqrt2$", r"$|\Psi|^2$ is a Gaussian with $\sigma^2=a^2/2$."),
  S(r"**(b)** $\langle\hat p\rangle$? (in terms of hbar, k0)", "hbar k0", "hbar k0", r"$\hbar k_0$", "The phase shifts the momentum, and a real Gaussian has none on its own."),
  S(r"**(c)** $\Delta p$? (in terms of hbar, a)", "hbar/(sqrt(2) a)", "hbar a", r"$\dfrac{\hbar}{\sqrt2a}$", r"$\Phi(k)\propto e^{-a^2(k-k_0)^2/2}$, so $\sigma_k=1/(\sqrt2a)$. The product saturates $\hbar/2$."),
  S(r"**(d)** $\langle\hat H\rangle$ for the free particle? (in terms of hbar, k0, a, m)", "hbar^2 (k0^2+1/(2 a^2))/(2 m)", "hbar k0 a m", r"$\dfrac{\hbar^2}{2m}\left(k_0^2+\dfrac{1}{2a^2}\right)$", r"$\langle p^2\rangle=\langle p\rangle^2+(\Delta p)^2$."),
  M("**(e)** After a long time $t$, which of $\\Delta x$, $\\Delta p$, $\\langle p\\rangle$ have changed?", ["Only $\\Delta x$", "$\\Delta x$ and $\\Delta p$", "All three", "None"], 0, r"$[\hat p,\hat H]=0$ for a free particle, so the momentum distribution is frozen."),
]),
P("Problem 5: Commutators and Ehrenfest", "operators", r"""
$\hat H=\dfrac{\hat p^2}{2m}+V(\hat x)$.
""", [
  S(r"**(a)** $[\hat x,\hat H]$? Write $\hat p$ as p. (in terms of hbar, p, m; use i)", "i hbar p/m", "hbar p m", r"$\dfrac{i\hbar\hat p}{m}$", r"$[x,p^2]=2i\hbar p$."),
  S(r"**(b)** For $V=\lambda x^4$, what's $[\hat p,\hat H]$? Write $\hat x$ as x. (in terms of hbar, lambda, x; use i)", "-4 i hbar lambda x^3", "hbar lambda x", r"$-4i\hbar\lambda\hat x^3$", r"$[p,f(x)]=-i\hbar f'$."),
  S(r"**(c)** For the same $V$, $\frac{d}{dt}\langle p\rangle$ is proportional to $\langle x^3\rangle$. What's the coefficient? (in terms of lambda)", "-4 lambda", "lambda", r"$-4\lambda$", "Ehrenfest."),
  M(r"**(d)** Does $\langle x\rangle$ exactly follow Newton's law for $V=\lambda x^4$?", ["Yes", "Only for even states", r"No, because $\langle x^3\rangle\ne\langle x\rangle^3$ in general", "No, because $\\hat x$ isn't Hermitian"], 2, "Newton's law would need $\\langle V'(x)\\rangle=V'(\\langle x\\rangle)$."),
]),
])

MID1B = E("m1b", "Midterm 1 · Mock B", "midterm", "Covers Lectures 1–9. Suggested time: 90 minutes.", [
P("Problem 1: Reading photoelectric data", "matterwaves", r"""
A metal surface gives these stopping potentials: $V_s=2.96$ V for $\lambda=250$ nm, and $V_s=1.10$ V for $\lambda=400$ nm.
""", [
  N("**(a)** Use the two points to find $hc$, in eV·nm.", (2.96-1.10)/(1/250-1/400), why=r"$eV_s=hc/\lambda-W$, so $hc=\dfrac{1.86}{1/250-1/400}=1240$ eV·nm."),
  N("**(b)** What's the work function, in eV?", 2.0, "eV", why=r"$W=1240/250-2.96=2.0$ eV."),
  N("**(c)** What's the threshold wavelength, in nm?", 620, "nm", why=r"$\lambda_0=hc/W=620$ nm."),
  M("**(d)** Light of 700 nm is made 1000 times brighter. What happens?", ["Many electrons appear with low energy", "Electrons appear after a long delay", "No electrons emerge", "Same electrons as at 400 nm"], 2, "Each photon is below threshold, and intensity doesn't change single-photon energy."),
]),
P("Problem 2: Dispersion relations", "matterwaves", r"""
For each $\omega(k)$, find the group velocity. Assume $k>0$.
""", [
  S(r"**(a)** $\omega=\sqrt{gk}$ for gravity waves. Give $v_g$. (in terms of g, k)", "sqrt(g/k)/2", "g k", r"$\tfrac12\sqrt{g/k}$", r"That's half of the phase velocity."),
  S(r"**(b)** $\omega=\sqrt{Ak^3}$. Give $v_g/v_{ph}$. (a number)", "3/2", [], r"$\tfrac32$", r"$\omega\propto k^{s}$ gives $v_g/v_{ph}=s$."),
  S(r"**(c)** Lattice: $\omega=\omega_0\sin(ka/2)$ with $0<ka<\pi$. Give $v_g$. (in terms of w0, a, k)", "w0 a cos(k a/2)/2", "w0 a k", r"$\tfrac12\omega_0a\cos(ka/2)$", "It goes to zero at the edge of the zone."),
]),
P("Problem 3: Box in momentum space", "wavepackets", r"""
Take $\Phi(k)=\dfrac{1}{\sqrt{2K}}$ for $|k|<K$ and zero otherwise. Use the 8.04 Fourier convention.
""", [
  S(r"**(a)** $\Psi(0,0)$? (in terms of K)", "sqrt(K/pi)", "K", r"$\sqrt{K/\pi}$", r"$\Psi(x,0)=\dfrac{\sin Kx}{x\sqrt{\pi K}}$, which tends to $\sqrt{K/\pi}$ at the origin."),
  S(r"**(b)** Position of the first zero of $\Psi(x,0)$ for $x>0$? (in terms of K)", "pi/K", "K", r"$\pi/K$", r"Consistent with $\Delta x\Delta k\sim1$."),
  S(r"**(c)** $\langle\hat p^2\rangle$? (in terms of hbar, K)", "hbar^2 K^2/3", "hbar K", r"$\hbar^2K^2/3$", r"Average $k^2$ over the flat distribution."),
  S(r"**(d)** $\langle\hat H\rangle$ if it's a free particle? (in terms of hbar, K, m)", "hbar^2 K^2/(6 m)", "hbar K m", r"$\dfrac{\hbar^2K^2}{6m}$", r"$\langle p^2\rangle/2m$."),
]),
P("Problem 4: A polynomial state", "wavepackets", r"""
At $t=0$, a particle's in $\psi(x)=Nx(a-x)$ for $0<x<a$, and zero elsewhere.
""", [
  ("schrodinger", S(r"**(a)** Find $N^2$. (in terms of a)", "30/a^5", "a", r"$30/a^5$", r"$\int_0^ax^2(a-x)^2dx=a^5/30$.")),
  ("operators", S(r"**(b)** $\langle\hat p^2\rangle$? (in terms of hbar, a)", "10 hbar^2/a^2", "hbar a", r"$10\hbar^2/a^2$", r"$\hbar^2\int\psi'^2=\hbar^2N^2\int(a-2x)^2dx=\hbar^2N^2a^3/3$.")),
  ("operators", S(r"**(c)** $(\Delta x)^2$? (in terms of a)", "a^2/28", "a", r"$a^2/28$", r"$\langle x^2\rangle=2a^2/7$, $\langle x\rangle=a/2$.")),
  ("operators", N(r"**(d)** What's $\Delta x\Delta p/\hbar$?", (10/28)**.5, why=r"$\sqrt{10/28}\approx0.598$, safely above 1/2.")),
]),
P("Problem 5: Observables and measurement", "operators", r"""
$\hat Q$ is Hermitian, with normalized eigenstates $|1\rangle,|2\rangle$ and eigenvalues $+q,-q$. A system's in $\cos\theta|1\rangle+\sin\theta|2\rangle$.
""", [
  S(r"**(a)** $\langle Q\rangle$? (in terms of q, theta)", "q cos(2 theta)", "q theta", r"$q\cos2\theta$", r"$q(\cos^2\theta-\sin^2\theta)$."),
  S(r"**(b)** $\Delta Q$, for $0<\theta<\pi/2$? (in terms of q, theta)", "q sin(2 theta)", "q theta", r"$q\sin2\theta$", r"$Q^2=q^2$ on this space, so $(\Delta Q)^2=q^2(1-\cos^22\theta)$.", ranges={"theta": [.1, 1.4]}),
  M(r"**(c)** For which $\theta$ is $\Delta Q=0$?", [r"$\theta=\pi/4$", r"$\theta=0$ or $\pi/2$", "All $\\theta$", "None"], 1, "$\\Delta Q=0$ holds only in eigenstates."),
  C(r"**(d)** $\hat A,\hat B$ are Hermitian. Select the Hermitian operators.", [r"$\hat A^2$", r"$\hat A\hat B\hat A$", r"$i\hat A$", r"$\hat A+\hat B$"], [0, 1, 3], r"$(iA)^\dagger=-iA$."),
]),
P("Problem 6: Entanglement test", "foundations", r"""
Two particles are in $\tfrac12\big(|u\rangle|u\rangle+|u\rangle|v\rangle+|v\rangle|u\rangle-|v\rangle|v\rangle\big)$.
""", [
  M("**(a)** Is this entangled?", ["Yes", "No"], 0, r"$AD-BC=(1)(-1)-(1)(1)=-2\ne0$."),
  N("**(b)** The first particle is measured and found in $|u\\rangle$. What's the probability that the second is then found in $|v\\rangle$?", 0.5, why=r"After measurement, the state's $|u\rangle\tfrac{1}{\sqrt2}(|u\rangle+|v\rangle)$."),
  N("**(c)** The first is found in $|v\\rangle$. What's then the probability that the second is in $\\tfrac{1}{\\sqrt2}(|u\\rangle-|v\\rangle)$?", 1.0, why=r"That's precisely the collapsed state of particle 2."),
  B("**(d)** Why doesn't part (c) allow faster-than-light signaling?", "The person measuring particle 2 sees a random result regardless of what's done to particle 1. Correlations only appear when both records are compared, which needs an ordinary signal."),
]),
])

MID2A = E("m2a", "Midterm 2 · Mock A", "midterm", "Covers Lectures 10–15. Suggested time: 90 minutes.", [
P("Problem 1: Uniform start in a box", "stationary", r"""
An infinite well on $0<x<a$ has the initial state $\Psi(x,0)=1/\sqrt a$.
""", [
  N(r"**(a)** What's the probability of measuring $E_1$?", 8/pi**2, why=r"$c_n=\dfrac{\sqrt2(1-(-1)^n)}{n\pi}$, so $|c_1|^2=8/\pi^2\approx0.81$."),
  N(r"**(b)** $E_2$?", 0, why="The initial state is even about $a/2$, and $\\psi_2$ is odd about it."),
  N(r"**(c)** $E_3$?", 8/(9*pi**2), why=r"$8/(9\pi^2)\approx0.090$."),
  M(r"**(d)** What's $\langle H\rangle$ in this state?", ["$E_1$", "$8E_1/\\pi^2$", "It diverges", "Zero"], 2, r"$\sum|c_n|^2E_n\propto\sum_{\text{odd}}1$ diverges: the jump at the walls costs infinite kinetic energy."),
]),
P("Problem 2: Sloshing in the box", "stationary", figs.infinite_well() + r"""
$\Psi(x,0)=\tfrac{1}{\sqrt2}(\psi_1+\psi_2)$, in an infinite well on $0<x<a$. You may use $\int_0^a\psi_1x\psi_2\,dx=-\dfrac{16a}{9\pi^2}$.
""", [
  S(r"**(a)** $\langle x\rangle$ at $t=0$? (in terms of a; use pi)", "a/2-16 a/(9 pi^2)", "a", r"$\dfrac a2-\dfrac{16a}{9\pi^2}$", "Diagonal terms give $a/2$, and the cross terms double."),
  S(r"**(b)** At what period does $\langle x\rangle$ oscillate? (in terms of m, a, hbar; use pi)", "4 m a^2/(3 pi hbar)", "m a hbar", r"$\dfrac{4ma^2}{3\pi\hbar}$", r"$\omega_{21}=3\pi^2\hbar/2ma^2$, and $T=2\pi/\omega_{21}$."),
  N(r"**(c)** At $t=T/2$, what's $\langle x\rangle/a$?", .5+16/(9*pi**2), why=r"$\cos$ flips sign: $0.5+0.180$."),
  M(r"**(d)** How does $\langle H\rangle$ vary?", ["It oscillates at $\\omega_{21}$", "Constant", "It decays", "It oscillates at $2\\omega_{21}$"], 1, "Conservation of energy expectation: $[\\hat H,\\hat H]=0$."),
]),
P("Problem 3: Designing a finite well", "wells", figs.graphical() + r"""
An electron is in a symmetric finite well of half-width $a=0.1$ nm, depth $V_0$. So $z_0^2=2mV_0a^2/\hbar^2$.
""", [
  N(r"**(a)** $z_0^2/V_0$ in units of eV$^{-1}$? ($\hbar c=197.3$ eV·nm, $m_ec^2=0.511\times10^6$ eV.)", well_scale, why=r"$2(5.11\times10^5)(0.01)/197.3^2\approx0.2625$."),
  N(r"**(b)** What's the minimum $V_0$ in eV for at least three bound states?", pi**2/well_scale, "eV", why=r"Need $z_0>\pi$, so $V_0>\pi^2/0.2625\approx37.6$ eV."),
  N(r"**(c)** If $z_0=2$, how many bound states does it have?", 2, why=r"$2z_0/\pi=1.27$, rounded up is 2."),
  M(r"**(d)** Suppose a hard wall is placed at $x=0$ and we keep only $x>0$, with $z_0=2$. How many bound states?", ["0", "1", "2", "3"], 1, r"Only the odd states survive; there's one for $\pi/2<z_0<3\pi/2$."),
  M("**(e)** Compared to the infinite well with the same width, what do the finite-well levels do?", ["They lie lower, measured from the bottom", "They lie higher", "They match exactly", "They only differ for even states"], 0, "Penetration lengthens the effective wavelength."),
]),
P("Problem 4: Delta function next to a wall", "wells", figs.delta_state() + r"""
$V=\infty$ for $x\le0$ and $V=-\alpha\delta(x-L)$ for $x>0$. For a bound state $\psi=A\sinh\kappa x$ for $0<x<L$ and $\psi=Ce^{-\kappa x}$ for $x>L$.
""", [
  B(r"**(a)** Write the boundary conditions at $x=L$ and find the quantization condition.",
    r"Continuity: $A\sinh\kappa L=Ce^{-\kappa L}$. Jump: $\psi'(L^+)-\psi'(L^-)=-\frac{2m\alpha}{\hbar^2}\psi(L)$, giving $-\kappa\sinh\kappa L-\kappa\cosh\kappa L=-\frac{2m\alpha}{\hbar^2}\sinh\kappa L$. So $\kappa(1+\coth\kappa L)=\dfrac{2m\alpha}{\hbar^2}$.", qtype="computational"),
  S(r"**(b)** What's the minimum $L$ for a bound state? (in terms of hbar, m, alpha)", "hbar^2/(2 m alpha)", "hbar m alpha", r"$\dfrac{\hbar^2}{2m\alpha}$", r"As $\kappa\to0$, $\kappa\coth\kappa L\to1/L$, so $1/L=2m\alpha/\hbar^2$."),
  S(r"**(c)** As $L\to\infty$, $\kappa\to$? (in terms of m, alpha, hbar)", "m alpha/hbar^2", "m alpha hbar", r"$m\alpha/\hbar^2$", r"$\coth\to1$. It's the isolated delta result."),
  M("**(d)** Which physical statement explains part (b)?", ["The wall forces $\\psi(0)=0$, costing kinetic energy that a weak delta can't pay for", "Delta functions need $E>0$", "Wall gives a repulsive delta", "Nothing: the formula is unphysical"], 0, "The same reasoning shows that half-wells need $z_0>\\pi/2$."),
]),
P("Problem 5: Ladder-operator computations", "oscillator", figs.oscillator() + r"""
A 1D oscillator with $\hat x=\sqrt{\frac{\hbar}{2m\omega}}(\hat a+\hat a^\dagger)$, $\hat p=i\sqrt{\frac{m\hbar\omega}{2}}(\hat a^\dagger-\hat a)$. Let $\ell^2\equiv\hbar/2m\omega$.
""", [
  S(r"**(a)** $\langle\varphi_1|\hat x^2|\varphi_1\rangle$? (in terms of hbar, m, omega)", "3 hbar/(2 m omega)", "hbar m omega", r"$\dfrac{3\hbar}{2m\omega}$", r"$\ell^2(2n+1)$ with $n=1$."),
  S(r"**(b)** $\langle\varphi_3|\hat x|\varphi_2\rangle$? (in terms of hbar, m, omega)", "sqrt(3 hbar/(2 m omega))", "hbar m omega", r"$\sqrt{\dfrac{3\hbar}{2m\omega}}$", r"Only $a^\dagger$ contributes, with $\sqrt3$."),
  S(r"**(c)** $\langle\varphi_0|\hat x^6|\varphi_0\rangle$? (in terms of L, where $L^2=\hbar/2m\omega$)", "15 L^6", "L", r"$15L^6$", r"Gaussian moment: $(6-1)!!=15$ with variance $L^2$."),
  S(r"**(d)** For $\Psi(0)=\tfrac{1}{\sqrt2}(\varphi_0+\varphi_1)$: $\langle x\rangle(t)$? (in terms of hbar, m, omega, t)", "sqrt(hbar/(2 m omega)) cos(omega t)", "hbar m omega t", r"$\sqrt{\dfrac{\hbar}{2m\omega}}\cos\omega t$", r"Cross terms with relative phase $e^{-i\omega t}$."),
  S(r"**(e)** For that state, $\langle p\rangle(t)$? (in terms of hbar, m, omega, t)", "-sqrt(m hbar omega/2) sin(omega t)", "hbar m omega t", r"$-\sqrt{\dfrac{m\hbar\omega}{2}}\sin\omega t$", r"It equals $m\,d\langle x\rangle/dt$, consistent with Ehrenfest."),
  S(r"**(f)** A wall at $x=0$ is added. What's the energy of the first excited state? (in terms of hbar, omega)", "7 hbar omega/2", "hbar omega", r"$\tfrac72\hbar\omega$", r"Only odd $n$ survive, with $n=1,3,\dots$. The first excited is $n=3$."),
]),
P("Problem 6: Deduce the potential", "stationary", r"""
$\psi(x)=Ax\,e^{-x^2/2b^2}$ is an energy eigenstate of a particle on the full line, in a potential with $V(0)=0$.
""", [
  S(r"**(a)** What's $E$? (in terms of hbar, m, b)", "3 hbar^2/(2 m b^2)", "hbar m b", r"$\dfrac{3\hbar^2}{2mb^2}$", r"$\psi''/\psi=x^2/b^4-3/b^2$; at $x=0$, $V=0$ yields $E$."),
  S(r"**(b)** What's $V(x)$? (in terms of hbar, m, b, x)", "hbar^2 x^2/(2 m b^4)", "hbar m b x", r"$\dfrac{\hbar^2x^2}{2mb^4}$", r"It's an oscillator with $\omega=\hbar/mb^2$."),
  M("**(c)** Which state is this?", ["Ground state", "First excited state", "Second excited state", "Not a bound state"], 1, "One node, by the node theorem."),
  B("**(d)** Sketch $\\psi$ and $V$, and mark the classical turning points.", r"$\psi$ is odd, zero at the origin, with peaks at $x=\pm b$, and decays as a Gaussian. $V$ is a parabola. Turning points: $E=V$ at $x=\pm\sqrt3b$, which are inflection points of $\psi$ (check: $\psi''=0$ when $x^2=3b^2$)."),
]),
])

MID2B = E("m2b", "Midterm 2 · Mock B", "midterm", "Covers Lectures 10–15. Suggested time: 90 minutes.", [
P("Problem 1: Particle on a circle", "stationary", r"""
A particle's on a circle with circumference $L$, in $\Psi(x,0)=N\cos^2(2\pi x/L)$. Eigenstates: $\psi_n=e^{2\pi inx/L}/\sqrt L$.
""", [
  S(r"**(a)** Find $N^2$. (in terms of L)", "8/(3 L)", "L", r"$8/(3L)$", r"$\int_0^L\cos^4=3L/8$."),
  N("**(b)** Probability that $n=0$?", 2/3, why=r"$\cos^2=\tfrac12+\tfrac14(e^{4\pi ix/L}+e^{-4\pi ix/L})$. Then $|c_0|^2=N^2L/4=2/3$."),
  N("**(c)** Probability that momentum is $+4\\pi\\hbar/L$?", 1/6, why=r"That's $n=2$, with $N^2L/16=1/6$."),
  S(r"**(d)** $\langle H\rangle$? (in terms of hbar, m, L; use pi)", "8 pi^2 hbar^2/(3 m L^2)", "hbar m L", r"$\dfrac{8\pi^2\hbar^2}{3mL^2}$", r"$E_{\pm2}=8\pi^2\hbar^2/mL^2$ with total weight 1/3."),
  S(r"**(e)** Period of $|\Psi(x,t)|^2$? (in terms of m, L, hbar; use pi)", "m L^2/(4 pi hbar)", "m L hbar", r"$\dfrac{mL^2}{4\pi\hbar}$", r"$\omega=E_2/\hbar$, since $n=\pm2$ are degenerate."),
]),
P("Problem 2: A 1×2 box", "stationary", r"""
A particle's in a 2D infinite box with $L_x=L$ and $L_y=2L$. Write $E=\epsilon\,(n_x^2+n_y^2/4)$ with $\epsilon=\pi^2\hbar^2/2mL^2$.
""", [
  N(r"**(a)** Ground state in units of $\epsilon$?", 1.25, why=r"$(1,1)$."),
  N(r"**(b)** First excited in units of $\epsilon$?", 2.0, why=r"$(1,2)$: $1+1=2$."),
  N(r"**(c)** Lowest *degenerate* level, in units of $\epsilon$?", 5.0, why=r"$(1,4)$ and $(2,2)$ both give 5."),
  M(r"**(d)** Is this degeneracy due to a geometric symmetry?", ["Yes, reflection", "Yes, rotation by 90°", "No, it's accidental for this aspect ratio", "No, it's forbidden"], 2, r"A $1\times2$ box lacks the 90° rotation. So it's an accidental consequence of the ratio."),
  M(r"**(e)** Why doesn't this contradict 'no degeneracy for 1D bound states'?", ["That theorem's only for 1D, and this is 2D", "The levels aren't truly degenerate", "A box isn't a bound state", "Only even states count"], 0, "Non-degeneracy relies on the 1D Wronskian argument."),
]),
P("Problem 3: General properties", "wells", r"""
A particle moves on the real line in a smooth potential $V(x)$ with a minimum and $V\to0$ as $|x|\to\infty$, having a few bound states.
""", [
  C("**(a)** Select all that are true for bound states.", ["They can be chosen real", "They're non-degenerate", "The ground state has no interior nodes", "They must have definite parity"], [0, 1, 2], "Definite parity needs an even $V$."),
  M(r"**(b)** At a point where $E<V(x)$ and $\psi>0$:", [r"$\psi''<0$", r"$\psi''>0$", r"$\psi''=0$", r"$\psi'=0$"], 1, r"Curving away from the axis."),
  M(r"**(c)** At a classical turning point, $\psi$ has:", ["A node", "An inflection point (unless it's zero there)", "A kink", "A maximum"], 1, r"$\psi''\propto(V-E)\psi$ changes sign."),
  B("**(d)** Explain why an energy below $V_{\\min}$ is impossible for a normalizable state.", r"Then $\psi''$ has the same sign as $\psi$ everywhere, so $\psi$ curves away from the axis at all $x$ and can't decay at both ends. Equivalently, $\langle H\rangle=\langle T\rangle+\langle V\rangle>V_{\min}$."),
]),
P("Problem 4: Two delta wells", "wells", r"""
$V=-\alpha[\delta(x-L)+\delta(x+L)]$. Let $\kappa_0=m\alpha/\hbar^2$. The bound states satisfy $\kappa=\kappa_0(1\pm e^{-2\kappa L})$.
""", [
  M("**(a)** Which sign belongs to the even state, the ground state?", ["$+$", "$-$"], 0, "It's bound more tightly, so it has a larger $\\kappa$."),
  S(r"**(b)** What's the minimum $L$ for an odd bound state? (in terms of hbar, m, alpha)", "hbar^2/(2 m alpha)", "hbar m alpha", r"$\dfrac{\hbar^2}{2m\alpha}$", r"For small $\kappa$, $\kappa\approx\kappa_0\cdot2\kappa L$, so $2\kappa_0L=1$. Same as a delta next to a wall, since the odd state has a node at 0."),
  S(r"**(c)** For large $L$, find $(E_{\text{odd}}-E_{\text{even}})/|E_0|$, where $E_0=-\hbar^2\kappa_0^2/2m$. (in terms of k0, L)", "4 exp(-2 k0 L)", "k0 L", r"$4e^{-2\kappa_0L}$", r"$\kappa_\pm^2\approx\kappa_0^2(1\pm2e^{-2\kappa_0L})$. The difference is $4e^{-2\kappa_0L}\kappa_0^2$."),
  B("**(d)** Connect this with chemical bonding in a sentence or two.", "When two wells share a particle, the even state has lower kinetic energy than the isolated well because it's spread over both wells. So bringing wells closer lowers the energy, an effective attraction, and the splitting grows exponentially as the wells overlap."),
]),
P("Problem 5: Oscillator in a uniform force", "oscillator", r"""
$\hat H=\dfrac{\hat p^2}{2m}+\tfrac12m\omega^2\hat x^2+F\hat x$, for a constant $F$.
""", [
  S(r"**(a)** Where's the center of the shifted parabola, $x_0$? (in terms of F, m, omega)", "-F/(m omega^2)", "F m omega", r"$-\dfrac{F}{m\omega^2}$", "Complete the square."),
  S(r"**(b)** What's $E_n$? (in terms of hbar, omega, n, F, m)", "hbar omega (n+1/2)-F^2/(2 m omega^2)", "hbar omega n F m", r"$\hbar\omega(n+\tfrac12)-\dfrac{F^2}{2m\omega^2}$", "It's the same oscillator, shifted down by a constant."),
  S(r"**(c)** $F$ is switched on suddenly, with the particle in the original ground state. What's the probability it stays in the new ground state? (in terms of x0, b, where $b^2=\hbar/m\omega$)", "exp(-x0^2/(2 b^2))", "x0 b", r"$e^{-x_0^2/2b^2}$", r"Gaussian overlap: $\int\varphi_0(x)\varphi_0(x-x_0)dx=e^{-x_0^2/4b^2}$."),
  M("**(d)** After the switch, how does $\\langle x\\rangle$ behave?", ["Stays at 0", "Moves to $x_0$ and stays", "Oscillates about $x_0$ at $\\omega$, between $0$ and $2x_0$", "Grows without bound"], 2, "Ehrenfest gives classical motion for quadratic potentials."),
]),
P("Problem 6: Operator algebra", "oscillator", r"""
Define $\hat b=\hat a^2$ and $\hat N=\hat a^\dagger\hat a$.
""", [
  S(r"**(a)** $[\hat b,\hat b^\dagger]$ acting on $\varphi_n$ gives a number times $\varphi_n$. What number? (in terms of n)", "4 n+2", "n", r"$4n+2$", r"$[a^2,a^{\dagger2}]=4N+2$."),
  S(r"**(b)** $[\hat H,\hat b]=\epsilon\,\hat b$. What's $\epsilon$? (in terms of hbar, omega)", "-2 hbar omega", "hbar omega", r"$-2\hbar\omega$", r"$b$ lowers by two levels."),
  S(r"**(c)** At $t=0$, in $\tfrac{1}{\sqrt2}(\varphi_0+\varphi_1)$, what's $(\Delta x)^2$? (in terms of hbar, m, omega)", "hbar/(2 m omega)", "hbar m omega", r"$\dfrac{\hbar}{2m\omega}$", r"$\langle x^2\rangle=\ell^2\cdot\tfrac12(1+3)=2\ell^2$ and $\langle x\rangle^2=\ell^2$."),
  M(r"**(d)** What does $[\hat H,\hat J]=\epsilon\hat J$ tell you about a spectrum?", ["Nothing", "If $E$ is an eigenvalue and $\\hat J\\psi\\neq0$, then $E+\\epsilon$ is one too", "All energies equal $\\epsilon$", "$\\hat J$ is Hermitian"], 1, r"$\hat H(\hat J\psi)=(E+\epsilon)\hat J\psi$."),
]),
])

FINALA = E("fa", "Final · Mock A", "final", "Cumulative, weighted to the later lectures. Suggested time: 3 hours.", [
P("Problem 1: Short answer on a stepped potential", "stationary", figs.pot([(0, 2.5), (0, -1), (1, -1), (1, 1), (2.5, 1)], (-.5, 2.5), (-1.3, 2.5), "Hard wall at x=0, then V=−V₀ for 0<x<L, then V=V₁ for x>L.") + r"""
Take the potential above: $V=\infty$ for $x<0$, $V=-V_0$ on $0<x<L$, and $V=V_1>0$ for $x>L$.
""", [
  C(r"**(a)** For $-V_0<E<V_1$, select all that are true of solutions that are physically allowed.", ["The energies are discrete", "They're non-degenerate", "They're normalizable", "They carry nonzero current"], [0, 1, 2], "These are bound states."),
  C(r"**(b)** For $E>V_1$, select all that are true.", ["Energies are continuous", "They're doubly degenerate", "The eigenstates are non-normalizable", "They can be chosen real"], [0, 2, 3], "The wall closes one side, so there's one solution per $E$: a standing wave, real up to a phase, with zero net current."),
  M("**(c)** What's the current in part (b)'s states?", ["Positive", "Negative", "Zero", "Depends on $E$"], 2, "A real wavefunction has $J=0$. The wall reflects everything."),
  M("**(d)** Can $V_1\\to\\infty$ remove all the bound states?", ["Yes", "No, it becomes an infinite well, with infinitely many"], 1, "It's an infinite well of width $L$."),
]),
P("Problem 2: The quantum Zeno polarizer", "foundations", r"""
A photon polarized along $x$ passes $N$ ideal polarizers, each rotated by $\theta=\pi/2N$ relative to the previous one, ending along $y$. Passing each has probability $\cos^2\theta$.
""", [
  S(r"**(a)** What's the probability of passing all $N$? (in terms of N; use pi)", "cos(pi/(2 N))^(2 N)", "N", r"$\cos^{2N}(\pi/2N)$", r"Each measurement collapses the state to the new axis.", ranges={"N": [5, 20]}),
  N("**(b)** Evaluate for $N=10$.", math.cos(pi/20)**20, why=r"$\approx0.78$."),
  S(r"**(c)** For large $N$, what's the leading loss probability $1-P$? (in terms of N; use pi)", "pi^2/(4 N)", "N", r"$\dfrac{\pi^2}{4N}$", r"$\cos^{2N}\epsilon\approx1-N\epsilon^2$, with $\epsilon=\pi/2N$.", ranges={"N": [500, 2000]}),
  B("**(d)** Without the intermediate polarizers, the probability's 0. Explain how adding absorbers can help.", "Each polarizer's measurement resets the state to its axis. Small rotations mean each step almost surely passes, and the state is dragged along. Without them $x$ and $y$ are orthogonal."),
]),
P("Problem 3: Electrons at a step", "scattering", r"""
Electrons with $E=4$ eV meet a step of height $V_0=3$ eV.
""", [
  N("**(a)** What's $R$?", 1/9, why=r"$k'/k=\sqrt{1/4}=1/2$."),
  N("**(b)** What's $T$?", 8/9, why=r"$1-R$, or $\frac{4kk'}{(k+k')^2}$."),
  N(r"**(c)** What's $|t|^2$? (Note it's not $T$.)", (2/1.5)**2, why=r"$t=2k/(k+k')=4/3$, so $|t|^2=16/9>1$. $T=\frac{k'}{k}|t|^2$."),
  N("**(d)** Same electrons with $E=1$ eV, same step: what's the penetration length $1/\\kappa$, in nm?", HBC/(2*ME*2)**.5, "nm", why=r"$\hbar c/\sqrt{2m_ec^2(V_0-E)}\approx197.3/1430\approx0.138$ nm."),
  N("**(e)** What's $R$ for an electron with $E=1$ eV that goes *down* a 3 eV step?", 1/9, why=r"$k'/k=2$. $R=\left(\frac{1-2}{1+2}\right)^2=1/9$. Reflection is symmetric, and there's reflection even though the potential drops."),
]),
P("Problem 4: Delta next to a wall, scattering", "phaseshift", r"""
$V=\infty$ for $x<0$ and $V=g\delta(x-L)$, with $g>0$. Inside, $\psi=A\sin kx$. Outside, $\psi=\sin(kx+\delta)$ up to a phase. Let $\beta=2mg/\hbar^2$.
""", [
  B(r"**(a)** Derive $\cot(kL+\delta)=\cot kL+\beta/k$.", r"Continuity: $A\sin kL=\sin(kL+\delta)$. Jump: $k\cos(kL+\delta)-Ak\cos kL=\beta A\sin kL$. Divide by $k\sin(kL+\delta)$.", qtype="computational"),
  S(r"**(b)** Take $kL=\pi/2$ and $\beta/k=1$. Give $\delta$, with $-\pi/2<\delta<\pi/2$. (a number)", "-pi/4", [], r"$-\pi/4$", r"$\cot(\pi/2+\delta)=-\tan\delta=1$."),
  N(r"**(c)** For (b), what's $|A_s|^2$?", 0.5, why=r"$\sin^2\delta$."),
  S(r"**(d)** Take $g\to\infty$: what's $\delta(k)$? (in terms of k, L)", "-k L", "k L", r"$-kL$", "It's a wall at $L$. The scattering then has $\\Delta t=-2L/v$."),
  M(r"**(e)** What's $\delta$ when $kL=n\pi$, for any $g$?", ["$0$ (mod $\\pi$)", r"$\pi/2$", "It depends on $g$", "Undefined"], 0, r"$\psi(L)=0$ there, so the delta has no effect."),
]),
P("Problem 5: Counting states with Levinson", "phaseshift", r"""
A wall at $x=0$, and a well $V=-V_0$ on $0<x<R$, zero beyond, with $z_0^2=2mV_0R^2/\hbar^2$.
""", [
  N("**(a)** For $z_0=5$, how many bound states does it have?", 2, why=r"States at $(2n-1)\pi/2<z_0$: $1.57$ and $4.71$ count, $7.85$ doesn't."),
  S(r"**(b)** So $\delta(0)-\delta(\infty)$ is? (a number; use pi)", "2 pi", [], r"$2\pi$", "Levinson."),
  M(r"**(c)** As $V_0$ grows through a threshold, what happens to $\delta(k\to0)$?", ["It falls by $\\pi$", "It rises by $\\pi$", "It doesn't change", "It's undefined"], 1, r"A new bound state means one more unit of $\pi$."),
  S(r"**(d)** Time delay in terms of $d\delta/dk$? (in terms of m, hbar, k, D, where $D=d\delta/dk$)", "2 m D/(hbar k)", "m hbar k D", r"$\dfrac{2m}{\hbar k}\dfrac{d\delta}{dk}$", "From stationary phase."),
]),
P("Problem 6: Hydrogen superposition", "hydrogen", figs.hydrogen_radial() + r"""
At $t=0$, $\psi=\tfrac{1}{\sqrt6}\big(2\varphi_{100}+\varphi_{211}-i\varphi_{21,-1}\big)$. Use $E_1=-13.6$ eV and $\hbar=6.6\times10^{-16}$ eV·s.
""", [
  N(r"**(a)** $\langle H\rangle$, in eV?", -10.2, "eV", why=r"$\frac46E_1+\frac26\frac{E_1}{4}=\frac34E_1$."),
  S(r"**(b)** $\langle L^2\rangle$? (in terms of hbar)", "2 hbar^2/3", "hbar", r"$\tfrac23\hbar^2$", r"Weight 1/3 at $\ell=1$, with $2\hbar^2$."),
  N(r"**(c)** $\langle L_z\rangle$ in units of $\hbar$?", 0, why=r"$\frac16(+1)+\frac16(-1)$."),
  N(r"**(d)** Period of the density's oscillation, in units of $10^{-16}$ s?", 2*pi*6.6/10.2, tol=.03, why=r"$T=2\pi\hbar/(E_2-E_1)=2\pi(6.6\times10^{-16})/10.2\approx4.07\times10^{-16}$ s."),
  M(r"**(e)** $L_z$ is measured and gives $+\hbar$. What's the state?", [r"$\varphi_{211}$", r"$\varphi_{100}$", r"The same", r"$\tfrac{1}{\sqrt2}(\varphi_{211}+\varphi_{100})$"], 0, "Collapse keeps only components with $m=1$."),
  C("**(f)** Select those constant in time, before measurement.", [r"$\langle H\rangle$", r"$\langle L^2\rangle$", r"$\langle L_z\rangle$", r"The density $|\psi(\vec r,t)|^2$"], [0, 1, 2], "All commute with $\\hat H$. Density has beats."),
]),
P("Problem 7: Angular momentum", "angular", r"""
A rigid rotor has $\hat H=\hat L^2/2I$.
""", [
  S(r"**(a)** Energy levels? (in terms of hbar, l, I)", "hbar^2 l (l+1)/(2 I)", "hbar l I", r"$\dfrac{\hbar^2\ell(\ell+1)}{2I}$", "Eigenvalues of $\\hat L^2$."),
  S(r"**(b)** Gap between $\ell=1$ and $\ell=2$? (in terms of hbar, I)", "2 hbar^2/I", "hbar I", r"$2\hbar^2/I$", r"$(6-2)\hbar^2/2I$."),
  S(r"**(c)** In $Y_{\ell m}$, $\langle L_x^2\rangle$? (in terms of hbar, l, m)", "hbar^2 (l (l+1)-m^2)/2", "hbar l m", r"$\tfrac12\hbar^2[\ell(\ell+1)-m^2]$", r"By symmetry, $\langle L_x^2\rangle=\langle L_y^2\rangle$, and these add to $\langle L^2-L_z^2\rangle$."),
  N(r"**(d)** A state $\propto\sin\theta\cos\phi$. Probability of $L_z=+\hbar$?", 0.5, why=r"$\cos\phi$ has equal $e^{\pm i\phi}$ weights."),
  M(r"**(e)** $[\hat L_z,\hat x^2+\hat y^2]$?", ["0", r"$2i\hbar xy$", r"$i\hbar$", r"$\hat L_z$"], 0, "A rotation about $z$ leaves $x^2+y^2$ unchanged."),
]),
])

FINALB = E("fb", "Final · Mock B", "final", "Cumulative. Suggested time: 3 hours.", [
P("Problem 1: Virial relation", "operators", r"""
For an energy eigenstate $\psi$, $\langle[\hat H,\hat Q]\rangle_\psi=0$ for any $\hat Q$. Use $\hat Q=\hat x\hat p$ with $\hat H=\hat p^2/2m+V$. This gives $2\langle T\rangle=\langle xV'\rangle$.
""", [
  B(r"**(a)** Explain why $\langle[\hat H,\hat Q]\rangle_\psi=0$.", r"$\langle\psi|HQ-QH|\psi\rangle=E\langle Q\rangle-E\langle Q\rangle=0$, moving $\hat H$ onto $\psi$ on the left by Hermiticity."),
  S(r"**(b)** For $V=\lambda x^4$: $\langle T\rangle/\langle V\rangle$? (a number)", "2", [], r"$2$", r"$xV'=4V$."),
  S(r"**(c)** For $V=\lambda x^4$: $\langle V\rangle$ in terms of $E$. (in terms of E)", "E/3", "E", r"$E/3$", r"$E=\langle T\rangle+\langle V\rangle=3\langle V\rangle$."),
  S(r"**(d)** For $V\propto|x|$: $\langle T\rangle/\langle V\rangle$? (a number)", "1/2", [], r"$\tfrac12$", r"$xV'=V$."),
  M(r"**(e)** Which potential would have $\langle T\rangle=-\langle V\rangle/2$?", [r"$x^2$", r"$-1/|x|$", r"$|x|$", r"$x^4$"], 1, r"$xV'=-V$. It matches the 3D Coulomb result."),
]),
P("Problem 2: Delta barrier and its pole", "scattering", r"""
For $V=g\delta(x)$, take $\psi=e^{ikx}+re^{-ikx}$ for $x<0$ and $\psi=te^{ikx}$ for $x>0$. Let $\beta=mg/\hbar^2k$.
""", [
  S(r"**(a)** $t$? (in terms of b, where $b=\beta$; use i)", "1/(1+i b)", "b", r"$\dfrac{1}{1+i\beta}$", r"Continuity: $1+r=t$. Jump: $ikt-ik(1-r)=\frac{2mg}{\hbar^2}t$."),
  S(r"**(b)** $r$? (in terms of b; use i)", "-i b/(1+i b)", "b", r"$\dfrac{-i\beta}{1+i\beta}$", r"$r=t-1$."),
  S(r"**(c)** $T$? (in terms of b)", "1/(1+b^2)", "b", r"$\dfrac{1}{1+\beta^2}$", r"$|t|^2$, equal velocities."),
  M("**(d)** At high energies:", [r"$T\to0$", r"$T\to1$", r"$T\to\tfrac12$", r"$T$ oscillates"], 1, r"$\beta\to0$."),
  S(r"**(e)** $t$ has a pole at $k=i\kappa$. For $g<0$, what's $\kappa$? (in terms of m, G, hbar, where $G=|g|$)", "m G/hbar^2", "m G hbar", r"$m|g|/\hbar^2$", r"Exactly the delta well's bound state! Poles of $t$ on the positive imaginary axis are bound states."),
  M(r"**(f)** Does reversing $g\to-g$ change $T$?", ["No", "Yes, $T$ grows", "Yes, $T$ falls", "It depends on $k$"], 0, r"$T$ depends on $g^2$."),
]),
P("Problem 3: Reflection delay", "scattering", figs.step_T() + r"""
A step with $0<E<V_0$. $r=\dfrac{k-i\kappa}{k+i\kappa}$.
""", [
  N(r"**(a)** $|r|^2$?", 1, why="It's a pure phase."),
  M(r"**(b)** For $E=V_0/2$, what's $r$?", [r"$1$", r"$-1$", r"$i$", r"$-i$"], 3, r"$\kappa=k$, so $r=(1-i)/(1+i)=-i$."),
  S(r"**(c)** Time delay of the reflected packet at $E=V_0/2$? (in terms of hbar, V0)", "2 hbar/V0", "hbar V0", r"$2\hbar/V_0$", r"$\Delta t=\frac{2m}{\hbar k\kappa}=\frac{2m}{\hbar k^2}=\frac{\hbar}{E}$."),
  M(r"**(d)** As $V_0\to\infty$ with $E$ fixed:", ["$r\\to+1$, delay goes to 0", "$r\\to-1$, delay goes to 0", "$r\\to-1$, delay diverges", "$r\\to i$"], 1, r"$\psi(0)=0$ forces a node at the wall."),
]),
P("Problem 4: Spherical box", "angular", r"""
A particle's in a spherical infinite well of radius $a$, with $\ell=0$: $u=\sqrt{2/a}\sin(\pi r/a)$.
""", [
  S(r"**(a)** Ground state energy? (in terms of hbar, m, a; use pi)", "pi^2 hbar^2/(2 m a^2)", "hbar m a", r"$\dfrac{\pi^2\hbar^2}{2ma^2}$", r"$u$ solves a 1D well with width $a$."),
  N(r"**(b)** Probability that $r<a/2$?", 0.5, why=r"$|u|^2$ is symmetric about $a/2$."),
  S(r"**(c)** $\psi(r=0)^2$? (in terms of a; use pi)", "pi/(2 a^3)", "a", r"$\dfrac{\pi}{2a^3}$", r"$\psi=\dfrac{u}{r\sqrt{4\pi}}$ and $u/r\to\sqrt{2/a}\,\pi/a$."),
  M("**(d)** For the finite spherical well with $\\ell=0$:", ["Always has a bound state", "Needs $z_0>\\pi/2$", "Needs $z_0>\\pi$", "Has none"], 1, r"It's the odd sector of a 1D well."),
]),
P("Problem 5: Energy–time", "stationary", r"""
$\Psi(0)=\tfrac{1}{\sqrt2}(\psi_1+\psi_2)$, with $E_2-E_1=\Omega\hbar$.
""", [
  S(r"**(a)** $\Delta E$? (in terms of hbar, Omega)", "hbar Omega/2", "hbar Omega", r"$\hbar\Omega/2$", r"Two equally weighted values: half their spread."),
  S(r"**(b)** At what first time is $\Psi(t)$ orthogonal to $\Psi(0)$? (in terms of Omega; use pi)", "pi/Omega", "Omega", r"$\pi/\Omega$", r"$\langle\Psi(0)|\Psi(t)\rangle\propto1+e^{-i\Omega t}$."),
  S(r"**(c)** Product $\Delta E\cdot T$? (in terms of hbar; use pi)", "pi hbar/2", "hbar", r"$\pi\hbar/2$", r"It respects $\Delta E\Delta t\gtrsim\hbar/2$."),
  M("**(d)** A state with definite energy has what timescale for change?", ["Infinite: it doesn't change", "Zero", "$\\hbar/E$", "It depends on $V$"], 0, r"Stationary state."),
]),
P("Problem 6: Hydrogen numbers", "hydrogen", figs.veff() + r"""
Use $13.6$ eV, $a_0=0.0529$ nm and $hc=1240$ eV·nm.
""", [
  N(r"**(a)** Most probable radius in $2p$, in units of $a_0$?", 4, why=r"$P\propto r^4e^{-r/a_0}$."),
  N(r"**(b)** $\langle r\rangle_{2p}$, in units of $a_0$?", 5, why=r"$\frac{1}{24}\int_0^\infty r^5e^{-r}dr=120/24$."),
  N(r"**(c)** $\langle V\rangle_{2p}$, in eV?", -6.8, "eV", why=r"Virial: $\langle V\rangle=2E_2=-6.8$ eV."),
  N(r"**(d)** Probability in the $1s$ state that $r>a_0$?", 5*math.exp(-2), why=r"$\int_1^\infty4r^2e^{-2r}dr=5e^{-2}\approx0.677$."),
  N(r"**(e)** Longest wavelength that can ionize from $n=1$, in nm?", 1240/13.6, "nm", why=r"$\approx91$ nm."),
  N(r"**(f)** Muonic hydrogen with $m_\mu/m_e\approx207$: ground-state binding energy in keV? (Ignore reduced mass.)", 207*13.6/1000, "keV", why=r"$E\propto m$: $207\times13.6$ eV."),
  N(r"**(g)** Degeneracy of $n=4$ (no spin)?", 16, why=r"$n^2$.", qtype="conceptual"),
  M(r"**(h)** Why does the same $E$ across different $\ell$ happen in hydrogen?", ["Rotational symmetry alone", "A hidden symmetry special to $1/r$", "Spin", "Parity"], 1, r"Rotations only explain $2\ell+1$."),
]),
P("Problem 7: Resonance data", "phaseshift", figs.resonance_delta() + r"""
A resonance is observed with a peak near $E_0=2$ eV and a width $\Gamma=1.32\times10^{-3}$ eV. Take $\hbar=6.6\times10^{-16}$ eV·s.
""", [
  N(r"**(a)** Lifetime $\tau=\hbar/\Gamma$, in ps?", 6.6e-16/1.32e-3*1e12, "ps", why=r"$5\times10^{-13}$ s $=0.5$ ps."),
  N(r"**(b)** Time delay at peak, in ps?", 4*6.6e-16/1.32e-3*1e12, "ps", why=r"$4\tau$."),
  M("**(c)** At the peak, $\\delta$ has increased through approximately what?", [r"$\pi/2$ of its rise, with $\sin^2$ near max (for small background)", "It's at a minimum", "Zero", r"$-\pi$"], 0, r"It rises by $\pi$ in total, and has done half of that at $E_0$."),
  B("**(d)** Describe how to tell a resonance from a bound state, in terms of energy and normalizability.", "Bound states have $E<0$ and are truly normalizable; they live forever. Resonances have $E>0$, with outgoing waves at large $x$, so they're quasi-bound and decay with a lifetime $\\hbar/\\Gamma$."),
]),
P("Problem 8: Better bomb testing", "foundations", figs.mach_zehnder(True) + r"""
Use $\text{BS1}=\begin{pmatrix}c&-s\\s&c\end{pmatrix}$, $\text{BS2}=\begin{pmatrix}c&s\\-s&c\end{pmatrix}$, with $c=\cos\theta$, $s=\sin\theta$. The input is $\binom10$. A live bomb is in the lower branch.
""", [
  S(r"**(a)** Explosion probability? (in terms of s)", "s^2", "s", r"$s^2$", "The lower amplitude after BS1 is $s$.", ranges={"s": [.1, .9]}),
  S(r"**(b)** $P(\text{D1})$? (in terms of s, c)", "s^2 c^2", "s c", r"$s^2c^2$", r"No explosion leaves $(c,0)$, and BS2 sends this to $(c^2,-sc)$.", ranges={"s": [.1, .9], "c": [.1, .9]}),
  S(r"**(c)** Fraction of live bombs certified intact, with repeats on D0? (in terms of c)", "c^2/(1+c^2)", "c", r"$\dfrac{c^2}{1+c^2}$", r"$\dfrac{s^2c^2}{s^2c^2+s^2}$."),
  N(r"**(d)** Evaluate at $\theta=\pi/4$.", 1/3, why=r"Standard 50/50 result."),
  N(r"**(e)** What's the supremum as $\theta\to0$?", 0.5, why=r"$c\to1$. Better requires multi-pass schemes."),
]),
])


DRILL = E("drill", "Conceptual drill", "drill", "Quick conceptual questions across the whole course, with no heavy computation.", [
P("Drill 1: Measurement and states", "foundations", "Answer without calculating anything long.", [
  M("**(a)** Which of these is a physically meaningful difference?", ["Overall phase", "Relative phase", "Both", "Neither"], 1, "Only relative phases show up in probabilities."),
  ("operators", M(r"**(b)** You repeat a position measurement immediately after the first. The result:", ["Is the same (idealized)", "Is uniformly random", r"Follows the original $|\Psi|^2$", "Is always zero"], 0, "The state collapsed to near that position, and it has no time to spread.")),
  ("operators", M(r"**(c)** $\psi_1,\psi_2$ have different momenta. Is $\psi_1+\psi_2$ a momentum eigenstate?", ["Yes", "No", "Only if the momenta are opposite", "Only for a free particle"], 1, "An eigenstate must have one eigenvalue.")),
  ("stationary", M(r"**(d)** A superposition of two states of the *same* energy:", ["Is stationary", "Oscillates", "Isn't allowed", "Must be normalized differently"], 0, "Both acquire the same phase.")),
  ("operators", M(r"**(e)** $\hat A$ and $\hat B$ commute. Then:", ["All eigenstates of $\\hat A$ are eigenstates of $\\hat B$", "There's a basis of simultaneous eigenstates", "$\\hat A=\\hat B$", "$\\Delta A\\Delta B$ is never zero"], 1, "Degenerate eigenstates of $\\hat A$ needn't be eigenstates of $\\hat B$ individually.")),
  ("schrodinger", M(r"**(f)** $\Psi$ is real at $t=0$ and $V$ is real. At later times:", ["It stays real", "It generally becomes complex", "It vanishes", "It's imaginary"], 1, "The equation has an explicit $i$.")),
]),
P("Drill 2: Sketching logic", "wells", r"""
Think about curvature, nodes and parity.
""", [
  M("**(a)** How many nodes does the 4th excited state have?", ["3", "4", "5", "Depends on $V$"], 1, r"4th excited is $n=5$, which has 4 nodes."),
  M("**(b)** Compare the amplitude of $\\psi$ where $V$ is low with where $V$ is high (both allowed).", ["Larger where $V$ is low", "Larger where $V$ is high", "Equal", "Unrelated"], 1, "More time spent where it's slower."),
  M("**(c)** Same comparison, for local wavelength:", ["Longer where $V$ is low", "Longer where $V$ is high", "Equal", "Unrelated"], 1, r"$\lambda=2\pi\hbar/\sqrt{2m(E-V)}$."),
  M("**(d)** At a finite jump in $V$:", ["$\\psi$ jumps", "$\\psi'$ jumps", "$\\psi''$ jumps", "All jump"], 2, r"$\psi''\propto(V-E)\psi$ inherits the jump."),
  M("**(e)** At a hard wall:", ["$\\psi=0$, $\\psi'$ can be nonzero", "$\\psi'=0$", "Both vanish", "$\\psi$ diverges"], 0, "If both vanished, $\\psi$ would be identically zero."),
  M("**(f)** A symmetric potential's 3rd excited state is:", ["Even", "Odd", "Neither", "Depends"], 1, r"Parity alternates, and $n=4$ is odd."),
  ("oscillator", M(r"**(g)** $\hat a\hat a^\dagger\varphi_n$ equals:", [r"$n\varphi_n$", r"$(n+1)\varphi_n$", r"$\varphi_{n+1}$", r"$\sqrt n\varphi_{n-1}$"], 1, r"$\hat a\hat a^\dagger=\hat N+1$.")),
  ("oscillator", M(r"**(h)** To engineer levels at 1, 3 and 5 meV, you'd choose:", ["An infinite well", "A finite well", r"An oscillator with $\hbar\omega=2$ meV", "A delta"], 2, "Equally spaced with an offset of half the spacing.")),
]),
P("Drill 3: Scattering logic", "scattering", r"""
No algebra is needed for these.
""", [
  M("**(a)** $T$ for a particle coming from the left vs. right in any 1D potential:", ["The same", "Always bigger from the left", "Depends on V's shape", "Sum is 1"], 0, "Reciprocity."),
  M("**(b)** A particle with $E>V_0$ meets a well or barrier: classically $R=0$. Quantum:", ["$R=0$ too", "$R$ is generally nonzero", "$R=1$", "$R<0$"], 1, "Reflection comes from any sudden change."),
  M("**(c)** Why isn't $T=|t|^2$ for a step?", ["Normalization", "Current includes the velocity factor", "Reflection", "Phase"], 1, r"$J\propto k|t|^2$."),
  ("phaseshift", M(r"**(d)** A large positive $d\delta/dk$ means:", ["The packet returns early", "The packet returns late", "No effect", "Absorption"], 1, "Long dwell time.")),
  ("phaseshift", M(r"**(e)** Levinson's theorem relates phase shift differences to:", ["Resonance widths", "The number of bound states", "Energy gaps", "Transit time"], 1, r"$N=[\delta(0)-\delta(\infty)]/\pi$.")),
  ("angular", M(r"**(f)** For a central potential, which set can be simultaneously definite?", [r"$E,L^2,L_z$", r"$E,L_x,L_z$", r"$x,p_x$", r"$L_x,L_y,L_z$"], 0, "These commute mutually.")),
  ("hydrogen", M(r"**(g)** $\ell=n-1$ states in hydrogen have how many radial nodes?", ["0", "1", "$n$", "$\\ell$"], 0, r"$n-\ell-1=0$.")),
  ("angular", M(r"**(h)** What makes a shallow 3D well able to have *no* bound state, unlike in 1D?", ["The Coulomb force", "$u(0)=0$ makes it like the odd sector", "Spin", "Angular momentum must be nonzero"], 1, "The odd sector in 1D has a threshold.")),
]),
])

EXAMS = [MID1A, MID1B, MID2A, MID2B, FINALA, FINALB, DRILL]
