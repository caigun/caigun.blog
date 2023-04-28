% Constant stepsize-------------------------------------------
% init
tol = 1e-5;
gn = inf;
x = [0 0]';
itercount = 0;
alpha = 0.1;

f = @(x1,x2) exp(1-x1-x2)+exp(x1+x2-1)+x1.^2+x1*x2+x2.^2+x1-3*x2;

f2 = @(x) f(x(1),x(2));

figure(2); clf; fcontour(f,[-2 0.5 -0.5 3]); axis equal; hold on

while gn >= tol
    g = grad(x);
    gn = norm(g);

    xnew = x - alpha*g;

    plot([x(1) xnew(1)], [x(2) xnew(2)], 'k*-')
    refresh

    itercount = itercount +1;
    x = xnew;
end
x
fopt = f2(x)
itercount = itercount -1

% Backtracking method ----------------------------------------
% init
tol = 1e-5;
gn = inf;
x = [0 0]';
itercount = 0;
% dx = inf;
% dmin = 1e-6;

f = @(x1,x2) exp(1-x1-x2)+exp(x1+x2-1)+x1.^2+x1*x2+x2.^2+x1-3*x2;

f2 = @(x) f(x(1),x(2));

figure(1); clf; fcontour(f,[-2 0.5 -0.5 3]); axis equal; hold on

while gn >= tol
    g = grad(x);
    gn = norm(g);
    t = 1;

    while (f2(x - t*g) > f2(x) - (1/2)*t*g'*g)
        t = 0.5*t;
    end
    alpha = t;
    xnew = x - alpha*g;

    plot([x(1) xnew(1)], [x(2) xnew(2)], 'k*-')
    refresh

    itercount = itercount +1;
    x = xnew;
end
x
fopt = f2(x)
itercount = itercount -1


function g = grad(x)
    g = [-exp(1-x(1)-x(2))+exp(-1+x(1)+x(2))+2*x(1)+x(2)+1
    -exp(1-x(1)-x(2))+exp(-1+x(1)+x(2))+2*x(2)+x(1)-3];
end