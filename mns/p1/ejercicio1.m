%pr 1.3 2x3 1eros 6 impartes

A = 1:2:5;
B = 7:2:11;

A = [A; B]

A(2, 3) = 0

B = A'

C = [B, eye(3)]

D = C(:, 1:2:length(A))

E = [C(1,3), C(1,5);
      C(2,3), C(2,5)]

F= [C(1, end-2:end);
   	C(2, end-2:end)]

G = diag(diag(D))

size(C)
 
