#include<iostream>
using namespace std;
int large[500]={0};
int main(){
    int carry,temp;
    large[0]=1;
    for(int i=0;i<1000;i++){
        carry=0;
        for(int j=0;j<500;j++){
            temp=2*large[j]+carry;
            carry=0;
            if(temp>9){
                large[j]=temp%10;
                carry=temp/10;
            }
            else large[j]=temp;
        }
    }
    int sum=0;
    for(int i=0;i<500;i++){
        sum+=large[i];
    }
    cout<<sum<<"\n";
    return 0;
}
