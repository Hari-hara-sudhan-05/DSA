def knapsack_greedy(items, max_weight):
    # Sort items by value-to-weight ratio
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    total_weight = 0
    selected_items = []

    for weight, value in items:
        if total_weight + weight <= max_weight:
            selected_items.append((weight, value))
            total_weight += weight
            total_value += value
        else:
            # If adding the whole item exceeds max_weight, add fraction of it
            remaining_weight = max_weight - total_weight
            fraction = remaining_weight / weight
            selected_items.append((remaining_weight, value * fraction))
            total_value += value * fraction
            break

    return total_value, selected_items

# Example usage
items = [(7, 42), (3, 12), (4, 40) ,(5,25)]  # (weight, value)
max_weight = 10
total_value, selected_items = knapsack_greedy(items, max_weight)
print(f"Total value in the knapsack: {total_value}")
print(f"Selected items: {selected_items}")