#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int N;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin>>N;
    vector<int> petals(N);
    for (int i = 0; i < N; i++){
        cin >> petals[i];
    }
    int ans = 0;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(i==j){continue;}
            int sum = 0;
            int len = 0;
            for(int k = i; k <= j; k++){
                sum += petals[k];
                len++;
            }
            float avg = (float)sum  / (float)len;
            /*if(i == 0 && j == 2){
                w << petals[0] << " " << petals[1] << " " << petals[2] << " " << sum << '\n';
                continue;
            }
            w << i << " " << j << " " << avg << "\n";*/
            for(int k = i; k <= j; k++){
                if((float)petals[k] == avg) {ans++; break;}
            }
        }
    }
    cout << ans+N;
}