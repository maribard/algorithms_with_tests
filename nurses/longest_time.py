import string


def find_nurse_with_longest_slot(slots):
    nurse_number = slots[0][0]
    nurse_time = slots[0][1]

    times_per_nurse = {nurse_number: nurse_time}

    for slot in range(1, len(slots)):
        if slots[slot][0] not in times_per_nurse:
            nurse_number = slots[slot][0]
            nurse_time = slots[slot][1] - slots[slot-1][1]
            times_per_nurse[nurse_number] = nurse_time
        else:
            nurse_number = slots[slot][0]
            additional_nurse_time = slots[slot][0] - slots[slot - 1][0]
            if additional_nurse_time > times_per_nurse[nurse_number]:
                times_per_nurse[nurse_number] = additional_nurse_time

    sorted_times_per_nurse = sorted(times_per_nurse.items(), key=lambda x: x[1], reverse=True)

    nurse_ids = list(string.ascii_lowercase)
    return nurse_ids[sorted_times_per_nurse[0][0]]


for i in range(1, 1):
    print(5)
