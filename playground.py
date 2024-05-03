if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_arr = sorted(arr,reverse=True)
    unique_sorted_arr = list(set(sorted_arr))
    print(unique_sorted_arr)
    print(f"second higest number is { unique_sorted_arr[1]}")
