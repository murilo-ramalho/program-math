#include <stdio.h>
#include <math.h>

//codigo C

double normal_cdf(double x) {
    return 0.5 * (1.0 + erf(x / sqrt(2.0)));
}

int main() {
    double z1 = 0.0;
    double z2 = 1.52;

    double prob = normal_cdf(z2) - normal_cdf(z1);

    printf("probabilidade: %.4f\n", prob);
    return 0;
 }
