import numpy as np

def relative_error(approx, exact):
    return np.abs(approx - exact) / np.abs(exact)

def main():
    # Перший вираз
    exact_sqrt_9_8 = np.sqrt(9.8)
    approx_sqrt_9_8 = 3.13

    # Другий вираз
    exact_fraction_23_15 = 23 / 15
    approx_fraction_23_15 = 1.53

    # Обчислення відносних похибок
    rel_error_sqrt = relative_error(approx_sqrt_9_8, exact_sqrt_9_8)
    rel_error_fraction = relative_error(approx_fraction_23_15, exact_fraction_23_15)

    # Порівняння точності
    if rel_error_sqrt < rel_error_fraction:
        print(f"Рівність √9.8 = 3.13 точніша з відносною похибкою: {rel_error_sqrt:.5f}")
    elif rel_error_fraction < rel_error_sqrt:
        print(f"Рівність 23/15 = 1.53 точніша з відносною похибкою: {rel_error_fraction:.5f}")
    else:
        print(f"Обидві рівності мають однакову точність з відносною похибкою: {rel_error_sqrt:.5f}")

if __name__ == "__main__":
    main()
