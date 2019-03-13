x=linspace(1,10,1001);
%n is the number of iteration
n = 49;
for i = 1:n
    x = sqrt(x);
end
for i = 1:n
    x = x.^2;
end
plot(linspace(1,10,1001),x,'b');
hold on;
plot(linspace(1,10,1001),linspace(1,10,1001),'r');