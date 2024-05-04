# find the starting number under one million
# which produces the longest chain

start_num = 2
longest_num = 0
longest_terms = 0

while start_num < 1000000:
    count_terms = 0
    cur_num = start_num
    while cur_num != 1:
        if cur_num % 2 == 0:
            cur_num = cur_num // 2
        else:
            cur_num = 3 * cur_num + 1
        count_terms += 1
    if count_terms > longest_terms:
        longest_num = start_num
        longest_terms = count_terms
    start_num += 1
print(longest_num, longest_terms)