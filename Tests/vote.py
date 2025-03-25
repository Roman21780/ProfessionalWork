def vote(votes):
    count = {}
    for num in votes:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    max_count = -1
    most_frequent = None
    for number, freq in count.items():
        if freq > max_count:
            max_count = freq
            most_frequent = number
    return most_frequent


if __name__ == '__main__':
    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))
