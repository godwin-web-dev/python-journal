nums = [2, 7, 11, 15]
target = 9
number_dict={}
for key,value in enumerate(nums):
    # print(key,value)
    remaining=target-value
    # print("target to conquer ",remaining)
    if remaining in number_dict:
        print("Yahoooooo the target is found in this ",number_dict[remaining],key)
        break
    number_dict[value]=key