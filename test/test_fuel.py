fract = input("Fraction: ")
def convert(fraction):
    print(fraction)
    try:
        numer, denom = fraction.split("/")
        # print(type(numer), type(denom))
        if not (numer.isdigit()) or not (denom.isdigit()):
            raise ValueError("Both numerator and denominator must be integers.")
        numer = int(numer)
        denom = int(denom)
        result = round((numer / denom) * 100)


        if denom == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        if numer > denom:
            raise ValueError("Numerator cannot be greater than denominator.")


    except ZeroDivisionError:
        raise ZeroDivisionError
    except ValueError:
        raise ValueError
    else:
        return result

res = convert(fract)
print(res)