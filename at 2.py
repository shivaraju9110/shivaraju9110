x=[]
lx=input("Enter x array len: ");
h=0;
for i=1:lx
  l=input("Enter lx: ");
  x=[x,l];
end
ly=input("Enter ly: ");
t=0:0.01:ly
for i=1:lx
  h+=x(i)*cos(2*pi*t*i);
end
plot(h)