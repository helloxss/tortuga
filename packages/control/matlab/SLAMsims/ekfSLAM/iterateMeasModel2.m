function C=iterateMeasModel2(state)
%    C=iterateMeasModel(x(:,t));

%rename state elements
x=state(1);
y=state(2);
dx=state(3);
dy=state(4);
x1=state(5);
y1=state(6);
x2=state(7);
y2=state(8);

temp1= ((x1-x)/(y1-y))^2;

c11= (1/(1+temp1)) * (-1/(y1-y));
c12= (1/(1+temp1)) * (x1-x)/((y1-y)^2);
c13= 0;
c14= 0;
c15= (1/(1+temp1)) * (1/(y1-y));
c16= (1/(1+temp1)) * (-(x1-x)/( (y1-y)^2));
c17= 0;
c18= 0;

temp2=  ((x2-x)/(y2-y))^2;
c21= (1/(1+temp2)) * (-1/(y2-y));
c22= (1/(1+temp2)) * (x2-x)/((y2-y)^2);
c23= 0;
c24= 0;
c25= 0;
c26= 0;
c27= (1/(1+temp2)) * (1/(y2-y));
c28= (1/(1+temp2)) * (-(x2-x)/((y2-y)^2));

C=[c11 c12 c13 c14 c15 c16 c17 c18;
   c21 c22 c23 c24 c25 c26 c27 c28];

