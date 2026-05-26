def count_by_field(jobs, key):
    counts={}

    for job in jobs:
        value=job.get(key)

        if value is None:
            continue

        if value not in counts:
            counts[value] = 1

        else:
            counts[value] += 1

    return counts


def get_top_items(counts, top_n=5):
    sorted_items = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
    return sorted_items[:top_n]