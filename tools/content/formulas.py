"""The formula sheet tab, in the course's notation."""
FORMULAS = r"""
## Constants
$\hbar c\simeq197.3$ MeV·fm $=197.3$ eV·nm, $\quad hc\simeq1240$ eV·nm, $\quad m_ec^2\simeq0.511$ MeV, $\quad m_pc^2\simeq938$ MeV, $\quad\hbar\simeq6.6\times10^{-16}$ eV·s, $\quad\alpha=e^2/\hbar c\simeq1/137$.

## Photons and matter waves
$$E=h\nu=\hbar\omega,\quad p=\frac h\lambda=\hbar k,\quad\lambda_C=\frac{h}{mc},\quad\Delta\lambda=\lambda_C(1-\cos\theta),\quad E_e=h\nu-W,\quad v_g=\frac{d\omega}{dk}.$$

## Schrödinger equation and probability
$$i\hbar\partial_t\Psi=\hat H\Psi,\quad\hat H=\frac{\hat p^2}{2m}+V,\quad\hat p=\frac\hbar i\partial_x,\quad\partial_t\rho+\partial_xJ=0,\quad J=\frac\hbar m\text{Im}(\Psi^*\partial_x\Psi).$$

## Fourier and Gaussians
$$\Psi(x)=\frac{1}{\sqrt{2\pi}}\int dk\,\Phi(k)e^{ikx},\quad\Phi(k)=\frac{1}{\sqrt{2\pi}}\int dx\,\Psi(x)e^{-ikx},\quad\int|\Psi|^2dx=\int|\Phi|^2dk.$$
$$\int_{-\infty}^\infty e^{-ax^2+bx}dx=\sqrt{\frac\pi a}e^{b^2/4a},\qquad\delta(k)=\frac{1}{2\pi}\int e^{ikx}dx,\qquad\text{shape preserved for }t\Delta v\lesssim\Delta x.$$

## Operators
$$[\hat x,\hat p]=i\hbar,\quad[A,BC]=[A,B]C+B[A,C],\quad[\hat p,f(\hat x)]=\frac\hbar if',\quad\int(K\Psi_1)^*\Psi_2=\int\Psi_1^*K^\dagger\Psi_2.$$
$$\langle Q\rangle=\int\Psi^*\hat Q\Psi,\quad\frac{d\langle Q\rangle}{dt}=\frac i\hbar\langle[\hat H,\hat Q]\rangle,\quad(\Delta Q)^2=\langle Q^2\rangle-\langle Q\rangle^2,\quad\Delta A\Delta B\ge\left|\frac{1}{2i}\langle[A,B]\rangle\right|.$$

## Stationary states and wells
$$\Psi=\psi(x)e^{-iEt/\hbar},\quad\Psi(x,t)=\sum_nc_ne^{-iE_nt/\hbar}\psi_n,\quad c_n=\int\psi_n^*\Psi(x,0)dx.$$
**Infinite well** on $0<x<a$: $\ \psi_n=\sqrt{2/a}\sin(n\pi x/a),\quad E_n=\hbar^2\pi^2n^2/2ma^2$.

**Finite well** $V=-V_0$ on $|x|<a$: $\ \eta^2+\xi^2=z_0^2,\quad z_0^2=2mV_0a^2/\hbar^2$; even $\xi=\eta\tan\eta$; odd $\xi=-\eta\cot\eta$.

**Delta well** $V=-\alpha\delta(x)$: $\ E=-m\alpha^2/2\hbar^2,\quad\psi=\sqrt\kappa e^{-\kappa|x|},\quad\kappa=m\alpha/\hbar^2$. Jump: $\psi'(0^+)-\psi'(0^-)=-\frac{2m\alpha}{\hbar^2}\psi(0)$.

## Harmonic oscillator
$$\hat H=\hbar\omega(\hat N+\tfrac12),\quad[\hat a,\hat a^\dagger]=1,\quad\hat a\varphi_n=\sqrt n\varphi_{n-1},\quad\hat a^\dagger\varphi_n=\sqrt{n+1}\varphi_{n+1},\quad\varphi_n=\frac{(\hat a^\dagger)^n}{\sqrt{n!}}\varphi_0.$$
$$\hat x=\sqrt{\frac{\hbar}{2m\omega}}(\hat a+\hat a^\dagger),\quad\hat p=i\sqrt{\frac{m\omega\hbar}{2}}(\hat a^\dagger-\hat a),\quad\varphi_0=\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-m\omega x^2/2\hbar}.$$

## Scattering
$$\psi=Ae^{ikx}+Be^{-ikx}:\ J=\frac{\hbar k}{m}(|A|^2-|B|^2),\qquad\text{Step, }E>V_0:\ R=\left(\frac{k-k'}{k+k'}\right)^2,\ T=\frac{4kk'}{(k+k')^2}.$$
$$\text{Well: }\frac1T=1+\frac{V_0^2}{4E(E+V_0)}\sin^2(2k_2a).\qquad\text{Delta: }T=\frac{1}{1+mg^2/2\hbar^2E}.$$
**Half-line.** $\ \psi=e^{i\delta}\sin(kx+\delta)$ for $x>R$. $\ A_s=e^{i\delta}\sin\delta$, $\ \Delta t=2\hbar\frac{d\delta}{dE}$, $\ N_{\text{bound}}=\frac1\pi[\delta(0)-\delta(\infty)]$, $\ \tau=\hbar/\Gamma$.

## Angular momentum
$$[\hat L_x,\hat L_y]=i\hbar\hat L_z,\ [\hat L^2,\hat L_i]=0,\ \hat L^2Y_{\ell m}=\hbar^2\ell(\ell+1)Y_{\ell m},\ \hat L_zY_{\ell m}=\hbar mY_{\ell m},\ \hat L_z=\frac\hbar i\partial_\phi.$$
$$Y_{00}=\frac{1}{\sqrt{4\pi}},\quad Y_{10}=\sqrt{\frac{3}{4\pi}}\cos\theta,\quad Y_{1,\pm1}=\mp\sqrt{\frac{3}{8\pi}}\sin\theta e^{\pm i\phi}.$$
**Radial.** $\ \psi=\frac urY_{\ell m}$, $\ \left[-\frac{\hbar^2}{2m}\partial_r^2+V+\frac{\hbar^2\ell(\ell+1)}{2mr^2}\right]u=Eu$, $\ u\sim r^{\ell+1}$.

## Hydrogen
$$E_n=-\frac{Z^2e^2}{2a_0n^2}\simeq-\frac{13.6Z^2}{n^2}\text{ eV},\quad a_0=\frac{\hbar^2}{me^2}\simeq0.529\text{ Å},\quad\ell=0,\dots,n-1,\quad\text{degeneracy }n^2.$$
$$u_{1,0}=\frac{2r}{a_0^{3/2}}e^{-r/a_0},\quad u_{2,0}=\frac{2r}{(2a_0)^{3/2}}\left(1-\frac{r}{2a_0}\right)e^{-r/2a_0},\quad u_{2,1}=\frac{1}{\sqrt3}\frac{r^2/a_0}{(2a_0)^{3/2}}e^{-r/2a_0}.$$
"""
