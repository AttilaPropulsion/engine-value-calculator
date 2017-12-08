y=0 #height
v=0 #velocity
a=0 #acceleration
t=0 #time elapsed
g=9.81 #gravitational acceleration
k=0.00517 #drag coeff

dt=float(input('Define value of dt')) #infinitesimal time interval
mr=float(input('Enter mass excluding propellant (dry mass)')) #mass w/o propellant
mp=float(input('Enter propellant mass')) #initial propellant mass
Ft = float(input('Enter a value for Thrust'))
b_t=float(input('Define burn-time'))
dm= mp / b_t #propellant mass flow rate -> approximated to a constant


M=mr+(mp-(dm*dt)) #M as a fn. of time M(t)

print('------BOOST PHASE------')
while mp>0:

    t=t+dt
    print ('time=', t)

    mp = mp - (dm * dt)
    print('current propmass=', mp)

    a = ((Ft - (M * g) - (k * (v ** 2)) - (dm * v))) / M
    print('acceleration=', a)

    v = v + (a * dt)
    print('speed=', v)

    y=y+(v*dt)+(0.5*a*((dt)**2))
    print ('height=', y)

    print('-------------------------')

TI = Ft*b_t

print('Total Impulse =', TI)

print('-------------------------')
print('------COAST PHASE------')

while v>0:
    t=t+dt
    print ('time =', t)

    a = (-(M * g) - (k * (v**2))) / M
    print('acceleration =', a)

    v = v + (a * dt)
    print('speed =', v)

    y = y + (v * dt) - (0.5 * a * ((dt) ** 2))
    print('height =', y)

    print('-------------------------')
