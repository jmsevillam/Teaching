#include<iostream>
#include<cmath>
double test(double x);
double test2(double x);
int main(int argc, char *argv[]){
  std::cout<<"set term pdf"<<std::endl;
  std::cout<<"set output 'a.pdf'"<<std::endl;
  double dx=0.01;
  std::cout<<"set xlabel 'x'"<<std::endl;
  std::cout<<"set ylabel 'y'"<<std::endl;
  std::cout<<"plot '-' u 1:2,'' u 1:3"<<std::endl;
  for(int i=0;i<1000;i++){
    std::cout<<i*dx<<' '<<test(i*dx)<<' '<<test2(i*dx)<<std::endl;
  }
  std::cout<<"e"<<std::endl;

  std::cout<<"plot '-' u 1:3"<<std::endl;
  for(int i=0;i<1000;i++){
    std::cout<<i*dx<<' '<<test(i*dx)<<' '<<test2(i*dx)<<std::endl;
  }
  std::cout<<"e"<<std::endl;
  std::cout<<"set term qt;"<<std::endl;
  return 0;
}
double test(double x){
  return sin(10*x)*exp(-x);
}
double test2(double x){
  return cos(10*x)*exp(-x);
}
