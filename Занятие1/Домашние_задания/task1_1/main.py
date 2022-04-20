def zippa( keys: list) -> list:
    nums = [i for i in range(len(keys))]
    for num, key in zip(nums, keys):
        print(num, key)






if __name__ == "__main__":

    list_ = ["a", "b", "c"]
    zippa(list_)
