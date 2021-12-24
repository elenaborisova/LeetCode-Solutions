def get_milestone_days(revenues, milestones):
    days = []

    for milestone in milestones:
        revenue_sum = 0

        for day, revenue in enumerate(revenues, start=1):
            revenue_sum += revenue
            if revenue_sum >= milestone:
                days.append(day)
                break

    return days


# Test cases:
print(get_milestone_days([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [100, 200, 500]) == [4, 6, 10])
print(get_milestone_days([100, 200, 300, 400, 500], [300, 800, 1000, 1400]) == [2, 4, 4, 5])
print(get_milestone_days([700, 800, 600, 400, 600, 700], [3100, 2200, 800, 2100, 1000]) == [5, 4, 2, 3, 2])
