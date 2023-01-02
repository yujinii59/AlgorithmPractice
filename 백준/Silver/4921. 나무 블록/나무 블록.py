matched_block = {1:[4, 5], 2:[], 3:[4, 5], 4:[2, 3], 5:[8], 6:[2, 3], 7:[8], 8:[6, 7]}
i = 1
while True:
    num = input()
    if num == '0':
        break
    else:
        print(f'{i}. ', end='')
        nums = list(map(int, list(num)))
        if nums[0] != 1 or nums[-1] != 2:
            print('NOT')
        else:
            prev = nums[0]
            for num in nums[1:]:
                if num not in matched_block[prev]:
                    print('NOT')
                    break
                prev = num
            
            else:
                print('VALID')
        i += 1