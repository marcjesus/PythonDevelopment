if __name__ == '__main__':
    n = input("Enter a number")
    result = ""
    for i in range(1,int(n)+1):
        result=str(i) + result
        print(f"Result = {str(i)} + {result}")
    
    reorder = result[::-1]
    print(reorder)