function [ x ] = remontada( A, b )
%calcula la solucion de un sistema triangular superior
%   Detailed explanation goes here
if ~istriu(A)
    ME = MException('A no es triangular');
    throw(ME)
end

n  = length(b);
x = [];
x(n) = b(n)/A(n, n);
for k=n:-1:1
    v = b(k);
    for l=n:-1:k
       v = v - A(k, l)*x(l);
    end
    x(k) = v/A(k, k);
end

end

