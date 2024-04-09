using namespace std;
void bubbleSort(int a[], int N){
    for (; N > 0; --N)
        for (int i = 0; i < N-1; ++i )
            if (a[i] > a[i+1])
                swap(a[i], a[i+1]);

};
 int main (){

 }