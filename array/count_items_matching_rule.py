def count_matches(items, rule_key, rule_value):
    matches_count = 0

    for item in items:
        if rule_key == 'type' and item[0] == rule_value:
            matches_count += 1
        elif rule_key == 'color' and item[1] == rule_value:
            matches_count += 1
        elif rule_key == 'name' and item[2] == rule_value:
            matches_count += 1

    return matches_count


print(count_matches([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
                    rule_key="color", rule_value="silver"))
print(count_matches([["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
                    rule_key="type", rule_value="phone"))
