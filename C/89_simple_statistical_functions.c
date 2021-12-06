#include <stdio.h>
#include <math.h>

size_t d_len;

void mean(int data[]) {
    float sum = 0.0;
    for (size_t i = 0; i<d_len; i++) {
        sum += data[i];
    }
    printf("Mean: %.2f\n", sum / d_len);
}

void variance(int data[]) {

}

void standard_deviation(int data[]){
    float sum = 0.0, SD = 0.0, mean;
    for (int i = 0; i < d_len; i++) {
        sum += data[i];
    }
    mean = sum / d_len;
    for (int i = 0; i < d_len; i++) {
        SD += pow(data[i] - mean, 2);
    }

    printf("%.2f\n", pow(SD / 10, 0.5));
}

void main(){
    int data[] = {3, 4, 5, 2, 6, 7, 3, 5, 3};
    d_len = sizeof(data) / sizeof(data[0]);
    mean(data);

}