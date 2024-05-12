def print_lowest_scores(nested_list):
    if not nested_list:
        print("The list is empty.")
        return

    # Find the lowest score
    lowest_score = min(item[1] for item in nested_list)

    # Find names associated with the lowest score
    lowest_score_names = [item[0] for item in nested_list if item[1] == lowest_score]

    print("Names with the lowest score(s):", lowest_score_names)

# Example usage:
scores_list = [["Alice", 85], ["Bob", 70], ["Charlie", 90], ["Dave", 70], ["Eve", 80]]
print_lowest_scores(scores_list)
