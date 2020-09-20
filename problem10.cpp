#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
long long int sieve(long long int n){
  long long int sum=2;
  bool mark[n+1];
  memset(mark,true,sizeof(mark));
  for(int i=1;i*i<=(n-1)/2;i++){
    if(mark[i]==true){
      for(int j=2*i*(i+1);j<=n;j=j+(2*i+1)){
        mark[j]=false;
      }
    }
  }
  for(int i=1;i<=(n-1)/2;i++){
    if(mark[i])
      sum=sum+(2*i+1);
  }
  return sum;
}

int main(){
  long long int n;
  cin>>n;
  long long int ans=sieve(n);
  cout<<ans<<"\n";
  return 0;
}
