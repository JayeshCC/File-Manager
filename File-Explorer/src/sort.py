from datetime import datetime
from functools import partial


def sort_col(col, reverse):
    global items
    l = [(items.set(k, col), k) for k in items.get_children("")]
    if col == "Name" or col == "Type":
        l.sort(reverse=reverse)
    elif col == "Date modified":
        l = sorted(l, key=sort_key_dates, reverse=reverse)
    elif col == "Size":
        l = sorted(l, key=sort_key_size, reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        items.move(k, "", index)

    # reverse sort next time
    items.heading(col, command=partial(sort_col, col, not reverse))

def sort_key_dates(item):
    return datetime.strptime(item[0], "%d-%m-%Y %I:%M")


def sort_key_size(item):
    num_size = item[0].split(" ")[0]
    if num_size != "":
        return int(num_size)
    else:
        return -1  # if it's a directory, give it negative size value, for sorting

