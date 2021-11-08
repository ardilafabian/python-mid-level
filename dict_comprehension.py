def main():
    nums = {i:i**3 for i in range(1,101) if i%3!=0}

    print(nums)

main()