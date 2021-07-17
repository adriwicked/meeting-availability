def get_available_time_blocks(cal1, cal2, meeting_duration):
    meetings = cal1['meetings'] + cal2['meetings']

    meetings.sort(key=lambda m: time_to_minutes(m[0]))

    meetings = flat_overlapping_meetings(meetings)

    bounds = merge_bounds(cal1['bounds'], cal2['bounds'])
    print('bounds', bounds)
    available_time = get_available_time(meetings, bounds)

    available_time = list(filter(
        lambda time_block: is_block_long_enough(time_block, meeting_duration),
        available_time
    ))

    return available_time


def time_to_minutes(str_time):
    hours, minutes = str_time.split(':')
    return int(hours) * 60 + int(minutes)


def flat_overlapping_meetings(meetings):
    start_time = meetings[0][0]
    end_time = meetings[0][1]
    merged_meetings = []

    for i in range(1, len(meetings)):
        if compare_times(end_time, meetings[i][0]) < 0:
            merged_meetings.append([start_time, end_time])
            start_time = meetings[i][0]
            end_time = meetings[i][1]
        else:
            if compare_times(end_time, meetings[i][1]) <= 0:
                end_time = meetings[i][1]
            # else:
                # Next block start should be checked here
                #merged_meetings.append([start_time, end_time])

    return merged_meetings


def compare_times(t1, t2):
    return time_to_minutes(t1) - time_to_minutes(t2)


def merge_bounds(b1, b2):
    start_bound = b1[0] if compare_times(b1[0], b2[0]) > 0 else b2[0]
    end_bound = b1[1] if compare_times(b1[1], b2[1]) < 0 else b2[1]
    return [start_bound, end_bound]


def get_available_time(meetings, bounds):
    available_time = []

    if compare_times(bounds[0], meetings[0][0]) < 0:
        available_time.append([bounds[0], meetings[0][0]])

    for i in range(len(meetings) - 1):
        available_time.append([meetings[i][1], meetings[i+1][0]])

    if compare_times(bounds[1], meetings[len(meetings) - 1][1]) > 0:
        available_time.append([meetings[len(meetings) - 1][1], bounds[1]])

    return available_time


def is_block_long_enough(block, duration):
    return time_to_minutes(block[1]) - time_to_minutes(block[0]) >= duration
