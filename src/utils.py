from typing import Union

def formatWithSuffix(num: Union[int, float]) -> str:
    assert isinstance(num, (int, float)), "num must be an int or float"

    labels = ["", "k", "M", "G", "T", "P", "E", "Z", "Y"]
    last_label = labels[-1]
    unit_step = 1000
    unit_step_thresh = unit_step - 0.05

    is_negative = num < 0
    if is_negative:
        num = abs(num)

    for unit in labels:
        if num < unit_step_thresh:
            break
        if unit != last_label:
            num /= unit_step

    return "{}{:.1f}{}".format("-" if is_negative else "", num, unit)