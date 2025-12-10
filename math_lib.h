#ifndef MATH_LIB_H
#define MATH_LIB_H

#ifdef _WIN32
#define EXPORT_DLL __declspec(dllexport)
#else
#define EXPORT_DLL
#endif

extern "C" {
    EXPORT_DLL double calculate_circle_area(double radius);
}

#endif // MATH_LIB_H#pragma once
