#include  <iostream>
#include <fstream>
#include <vector>

using namespace std;

int N,K;
vector<int> diamonds(10000, 0);

int dims(int start){
    int res = 0;
    for(int i = 0; i < N; i++){
        if(diamonds[i] - start <= K && start <= diamonds[i]){
            res++;
        }
    }
    return res;
}

int main(){
    ifstream f;
    ofstream w;
    f.open("diamond.in");
    w.open("diamond.out");
    f >> N >> K;
    for(int i = 0; i < N; i++){
        f >> diamonds[i];
    }
    int maxes = -1;
    for(int i = 0; i < N; i++){
        maxes  = max(maxes, dims(diamonds[i]));
    }
    w << maxes;
    f.close();
    w.close();
}