#include <bitset>/stdc++/h>
using namespace std;

void bubbleSort(int a[], int N){
    for (; N > 0; --N)
        for (int i = 0; i < N-1; ++i )
            if (a[i] > a[i+1])
                swap(a[i], a[i+1]);

};
void bubbleSortImproved(int a[], int N){
    bool flag;
    for (; N > 0; --N) 
        flag = true;
        for (int i = 0; i < N-1; ++i )
            if (a[i] > a[i+1])
                swap(a[i], a[i+1]);
                flag = false;
            
        if (flag == true)
            N = 0;
            
};

void selectionSort(int a[], int N){
    for (int L = 0; L <= N-2; ++ L){
        int X = min_element(a + L, a +N) -a;
        swap(a[X], a[L]);
    }
}
 
 void insertionSort(int a[], int N){
    for (int i = 1; i < N; i ++){
        int X = a[i];
        int j = i -1;
        for (; j >= 0 && a[j] > X; --j)
            a[j+1] = a[j];
        a[j+1] = X;
        
    }
 }

 void merge(int a[], int low, int mid, int high){
    int N = high - low;
    int b[N];
    int left = low, right = mid + 1, bIdx = 0;
    while (left <= mid && right <= high)
        b[bIdx++] = (a[left] <= a[right]) ? a[left++] : a[right++]
 }