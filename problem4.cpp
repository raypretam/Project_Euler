#include<iostream>
#include<limits.h>
#include<math.h>
using namespace std;
typedef long long int int64;
bool palindrom(int64 n){
  int s=0,r,t=n;
  while(t){
    r=t%10;
    s=s*10+r;
    t=t/10;
  }
  if(s==n)
    return true;
  else
    return false;
}
int main(){
  int64 maxr=INT_MIN;
  int i,j;
  for(i=100;i<=999;i++){
    for(j=100;j<=999;j++){
      if(palindrom(i*j)){
        if((i*j)>=maxr)
          maxr=(i*j);
        }
    }
  }
  cout<<maxr<<"\n";
  return 0;
}
