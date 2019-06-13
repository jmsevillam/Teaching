#include<iostream>
#include<cmath>
double test(double x);
int main(int argc, char *argv[]){
std::cout<<"set term pdf"<<std::endl;
std::cout<<"set output 'a.pdf'"<<std::endl;
double dx=0.01;
std::cout<<"set xlabel 'x'"<<std::endl;
std::cout<<"set ylabel 'y'"<<std::endl;
std::cout<<"plot '-' t 'Legend of plot'"<<std::endl;
for(int i=0;i<1000;i++){
  std::cout<<i*dx<<' '<<test(i*dx)<<std::endl;
}
std::cout<<"e"<<std::endl;
std::cout<<"set term qt;"<<std::endl;
return 0;
}
double test(double x){
  return sin(10*x)*exp(-x);
}
