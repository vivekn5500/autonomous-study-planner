def allocate_time(subjects, hours):
    per_subject = hours // len(subjects)
    return {sub: per_subject for sub in subjects}


def format_schedule(plan):
    output = ""
    for sub, time in plan.items():
        output += f"{sub}: {time} hours\n"
    return output