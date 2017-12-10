clear all
close all
y(1)=0; % meter
v(1)=0; %meter/second
a(1)=0; %meter/second2
t(1)=0; %second
dt=0.1; %second 
mp(1)=4 ; %kilogram propellant mass
mr=18; %kilogram rocket mass
Ft=1725 ;%newton thrust
g=9.81 ; %meter/second2
k=0.0113; %drag coefficient
b_t=5;  %burn time
dm= mp / b_t; %kilogram/second  delta mass flow rate 
M=(mr+(mp(1)-dm*dt));
i=1;
while mp>0
i=i+1;
t(i)=t(i-1)+dt;
mp(i)=mp(i-1)-(dm*dt);
a=((Ft-M*g-(k*v(i-1).^2))-dm*v(i-1))/M;
v(i)=v(i-1)+a*dt;
y(i)=y(i-1)+(v(i)*dt)+(0.5*a*(dt^2));
end
TI = Ft*b_t; toplam impulse
i=2;
while v>0
  
    t=t+dt
    a = (-(M*g) - (k*(v(i-1).^2)))/ M
    v(i) = v(i-1)+(a*dt)
    y(i) = y(i-1)+(v(i)*dt)-(0.5*a*((dt)^2))
      i=i+1;
end
