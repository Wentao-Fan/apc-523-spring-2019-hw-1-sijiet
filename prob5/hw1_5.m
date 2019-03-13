error = 1;
elist = [];
n = 1;
i = 1;
elist(1) = (1+1/n)^n;
while error >= 10^(-13)
    n = n*10;
    i = i+1;
    elist(i) = (1+1/n)^n;
    error = abs(elist(i)-elist(i-1));
end
    