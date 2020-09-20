#include<iostream>
#include<math.h>
#include<algorithm>
using namespace std;
int main(){
  long long int i;
  long long int ans=1;
  for(i=1;i<=20;i++){
    ans=(ans*i)/(__gcd(ans,i));
  }
  cout<<ans<<"\n";
  return 0;
}
