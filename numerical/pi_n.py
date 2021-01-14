
def pi_n(n):
    """Print out the digits of pi to the `nth` digit.
    """

    LIMIT = 250

    k_1 = 545140134
    k_2 = 13591409
    k_3 = 640320
    k_4 = 100100025
    k_5 = 327843840
    k_6 = 53360

    denominator = 0
    i = 0

    while i >= 0:
        denominator += (-1)**i * (6*i)! * (k_2 + i*k_1)/(i!^ 3(3i)!())

    return pi
