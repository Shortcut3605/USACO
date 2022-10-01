#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

vector<int> v(1000,0);

int solve(int* x,int* y,int* z,int curr){
    if(v[curr] != 0){
        return v[curr];
    }
    if(curr + *x > *z){
        v[curr] = curr;
        return curr;
    }
    else if(curr + *x == *z){
        v[curr] = curr + *x;
        return curr + *x;
    }
    if(curr + *y < *z){
        v[curr] = max(solve(x,y,z,curr + *y),solve(x,y,z,curr+*x));
        return v[curr];
    }
    v[curr] = solve(x,y,z,curr+*x);
    return v[curr];
}


int main(){
    ifstream of;
    of.open("pails.in");
    ofstream write;
    write.open("pails.out");
    int x,y,z;
    of>>x>>y>>z;

    write <<   solve(&x,&y,&z,0);
    write.close();
    of.close();
}