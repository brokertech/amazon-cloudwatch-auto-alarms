from typing import Union

def formatBytes(num: Union[int, float]) -> str:
    assert isinstance(num, (int, float)), "num must be an int or float"

    unit_labels = ["B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    last_label = unit_labels[-1]
    unit_step = 1024
    unit_step_thresh = unit_step - 0.05

    is_negative = num < 0
    if is_negative:
        num = abs(num)

    for unit in unit_labels:
        if num < unit_step_thresh:
            break
        if unit != last_label:
            num /= unit_step

    return "{}{:.1f} {}".format("-" if is_negative else "", num, unit)