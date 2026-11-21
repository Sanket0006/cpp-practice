def main():
    l = [-1,1,0,-3,3]


    soln(l)

def soln(nums:list):
        prefix_product = [1]
        suffix_product = [1]*(len(nums)+1)

        # suffix_product[len(nums)-1] = nums[-1]

        for i in range(len(nums)):
            prefix_product.append(nums[i]*prefix_product[-1])

        

        for i in range(len(nums)-1, -1, -1):
            suffix_product[i] = nums[i] * suffix_product[i+1]

        print(prefix_product, suffix_product)

        new = [1]*(len(nums))

        for i in range(0, len(nums)):
            new[i] = prefix_product[i]*suffix_product[i+1]

        print(new)

main()