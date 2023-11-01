def get_loss(w1, w2, w3, w4):
    try:
        warning_operation_result = w1 // w2
    except ZeroDivisionError:
        return "деление на ноль"
    else:
        y = 10 * (warning_operation_result) - 5 * w2 * w3 + w4
        return y
