#include "math_lib.h"
#include <cmath>

#define PI 3.14159265358979323846

double calculate_circle_area(double radius) {
    if (radius < 0) {
        return 0.0;
    }
    return PI * radius * radius;
}