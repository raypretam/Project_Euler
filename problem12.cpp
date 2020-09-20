#include<iostream>
#include<math.h>
using namespace std;
int countDivisors(long long n)
{
    int cnt = 0;
    for (int i = 1; i <= sqrt(n); i++) {
        if (n % i == 0) {
            // If divisors are equal,
            // count only one
            if (n / i == i)
                cnt++;

            else // Otherwise count both
                cnt = cnt + 2;
        }
    }
    return cnt;
}
int main(){
  int n=1,ans;
  long long tn;
  while(true){
    tn=((n+1)*n)/2;
    ans=countDivisors(tn);
    if(ans>=500)
      break;
    else n=n+1;
  }
  cout<<tn<<"\n";
  return 0;
}
