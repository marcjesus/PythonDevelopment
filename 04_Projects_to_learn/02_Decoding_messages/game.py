def decode(message_file):
    # Step 1: Read the input file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Step 2: Parse the lines to get numbers and corresponding words
    num_word_dict = {}
    for line in lines:
        parts = line.strip().split()
        num = int(parts[0])
        word = " ".join(parts[1:])
        num_word_dict[num] = word

    # Step 3: Determine the numbers at the end of each pyramid level
    level_end_nums = []
    level = 1
    current_num = 0
    while current_num < max(num_word_dict.keys()):
        current_num += level
        level_end_nums.append(current_num)
        level += 1

    # Step 4: Collect words for these numbers to form the decoded message
    message_words = [num_word_dict[num] for num in level_end_nums if num in num_word_dict]

    # Step 5: Return the decoded message
    return " ".join(message_words)

# Example usage:
# Assuming the input file is named 'message.txt' and contains the provided example content
decoded_message = decode('example2.txt')
print(decoded_message)  # Output should be: "I love computers"
