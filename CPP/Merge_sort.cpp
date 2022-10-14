#include <bits/stdc++.h>
using namespace std;

// Merge two sub array in main array.
void merge(int arr[], int start, int end, int const size)
{
    int mid = (end + start) / 2;
    int i = start;
    int j = mid + 1;
    int k = start;

    int *tArr = new int[size];

    while (i <= mid && j <= end)
    {
        if (arr[i] < arr[j])
        {
            tArr[k] = arr[i];
            i++;
        }
        else
        {
            tArr[k] = arr[j];
            j++;
        }
        k++;
    }

    while (i <= mid)
    {
        tArr[k] = arr[i];
        i++;
        k++;
    }
    while (j <= end)
    {
        tArr[k] = arr[j];
        k++;
        j++;
    }

    for (int i = start; i <= end; i++)
    {
        arr[i] = tArr[i];
    }
    free(tArr);
}

// Divide array into two sub array.
void mergeSort(int arr[], int start, int end, int const size)
{
    // mid is the point where two sub array is divided.
    int mid = (start + end) / 2;

    if (start >= end)
        return;

    mergeSort(arr, start, mid, size);
    mergeSort(arr, mid + 1, end, size);
    merge(arr, start, end, size);
}

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main()
{
    int size;

    cout << "Enter the size of array" << endl;
    cin >> size;

    int *arr = new int[size];

    cout << "Enter array of size " << size << endl;

    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }

    mergeSort(arr, 0, size - 1, size);
    printArray(arr, size);
    
    free(arr);
    return 0;
}