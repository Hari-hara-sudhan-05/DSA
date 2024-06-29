def stable_marriage(n, men_preferences, women_preferences):
    free_men = list(range(n))
    women_partners = [-1] * n
    men_next_proposal = [0] * n
    women_preferences_rank = [[0] * n for _ in range(n)]
    
    # Precompute the rank of each man in each woman's preference list
    for w in range(n):
        for rank in range(n):
            women_preferences_rank[w][women_preferences[w][rank]] = rank
    
    while free_men:
        man = free_men.pop(0)
        woman = men_preferences[man][men_next_proposal[man]]
        men_next_proposal[man] += 1
        
        if women_partners[woman] == -1:
            women_partners[woman] = man
        else:
            current_partner = women_partners[woman]
            if women_preferences_rank[woman][man] < women_preferences_rank[woman][current_partner]:
                women_partners[woman] = man
                free_men.append(current_partner)
            else:
                free_men.append(man)
    
    return women_partners


# Example usage
n = 4
men_preferences = [
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3]
]
women_preferences = [
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3]
]

print(stable_marriage(n, men_preferences, women_preferences))