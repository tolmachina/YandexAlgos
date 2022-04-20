#include <iostream>
#include <string>
using namespace std;

struct person {
    string login;
    int problems;
    int fines;
};


// main() is where program execution begins.
int main() {
    int n_guys;
    cin >> n_guys;
    
    string names[n_guys];
    int prob[n_guys];
    int fines[n_guys];

    for(int i = 0; i < n_guys; i++){
        string login;
        int p_problems;
        int f_fines;

        cin >> login;
        cin >> p_problems;
        cin >> f_fines;

        names[i] = login;
        prob[i] = p_problems;
        fines[i] = f_fines;


    }

    cout << "Hello World \n"; // prints Hello World

    for(int i=0; i < n_guys; i++){
        cout << names[i] << endl;
        cout << prob[i] << endl;
    }


    return 0;
}