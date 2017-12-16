y=0 #height -> initially 0
v=0 #velocity -> initially 0
a=0 #acceleration -> initially 0
t=0 #time elapsed -> initially 0
g=9.81 #gravitational acceleration

#--------------------------------------

T0=273 + 27 #Temperature at 0 in KELVIN --->Can be defined as the temperature of the place
P0=97325 #Pressure at Las Crucos where we'll launch (1.100m above sea-level) in Pascal (sea-level=101325Pa)
rho0=1.225 #air density at 0 in Kg/m^3
alpha=0.0065 #temperature change in K/m
n=5.2561 #significant number for defining rho(y) and P(y)

#--------------------------------------

T_y = T0 - (alpha * y)
P_y = P0 * ((T_y / T0) ** n)
rho_y = rho0 * ((T_y / T0) ** (n - 1))

dt=float(input('Define value of dt')) #infinitesimal time interval
mr=float(input('Enter mass excluding propellant (dry mass)')) #mass w/o propellant
mp=float(input('Enter propellant mass')) #initial propellant mass
Ft=float(input('Enter a value for Thrust')) #desired thrust value for testing
b_t=float(input('Define burn-time')) #burntime of the motor

dm= mp / b_t #propellant mass flow rate -> approximated to a constant
M= mr+(mp-(dm*dt)) #M as a fn. of time -> M(t)


print('--------PHASE 1: BOOST--------')
while mp>0:

    t=t+dt
    print ('time=', t)

    mp = mp - (dm * dt)
    print('current propmass=', mp)

    k = (0.5 * rho_y * 0.75 * 0.0113)  # drag coef.
    print('k(drag force coef) =', k)

    Fd = (k * (v ** 2))
    print('Fd=',Fd)

    print(' ')

    a = (Ft - (M * g) - (Fd) - (dm * v)) / M
    print('*acceleration=', a)

    v = v + (a * dt)
    print('*speed=', v)

    y=y+(v*dt)+(0.5*a*((dt)**2))
    print ('*height=', y)

    print(' ')

    T_y = T0 - (alpha * y)
    print('Temperature @ this height=', T_y)

    P_y = P0 * ((T_y / T0) ** n)
    print('Air Pressure @ this height=', P_y)

    rho_y = rho0 * ((T_y / T0) ** (n - 1))
    print('rho(y)=', rho_y)

    print('------------------------')

TI = Ft*b_t
print('Total Impulse During Boost =', TI)

prcd= input('Do you want to proceed to PHASE 2: COAST?')

if (prcd == 'YES'):

    print('--------PHASE2:COAST--------')

    while v>0:
        t=t+dt
        print ('time =', t)

        k = (0.5 * rho_y * 0.75 * 0.0113)  # drag coef.
        print('k(drag force coef) =', k)

        Fd = (k * (v ** 2))
        print('Fd=', Fd)

        print(' ')

        a = (-(M * g) - Fd) / M
        print('*acceleration =', a)

        v = v + (a * dt)
        print('*speed =', v)

        y = y + (v * dt) - (0.5 * a * ((dt) ** 2))
        print('*height =', y)

        print(' ')

        T_y = T0 - (alpha * y)
        print('Temperature @ this height=', T_y)

        P_y = P0 * ((T_y / T0) ** n)
        print('Air Pressure @ this height=', P_y)

        rho_y = rho0 * ((T_y / T0) ** (n - 1))
        print('rho(y)=', rho_y)

        print('------------------------')

else:
    print('JOBS DONE!')
