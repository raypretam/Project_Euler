#include<iostream>
using namespace std;
typedef long long int int64;
int main(){
    int m,n;
    cin>>m>>n;
    int64 arr[m+1][n+1];
    for(int i=0;i<=m;i++)
        arr[i][0]=1;
    for(int j=0;j<=n;j++)
        arr[0][j]=1;
    for(int i=1;i<=m;i++){
        for(int j=1;j<=n;j++){
            arr[i][j]=arr[i-1][j]+arr[i][j-1];
        }
    }
    cout<<arr[m][n]<<"\n";
    return 0;
}
