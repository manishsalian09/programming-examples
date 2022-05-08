package main

import "fmt"

func main() {

	fmt.Println(howSum(7, []int{2,3}, map[int][]int{}))
}

func howSum(targetSum int, nums []int, memo map[int][]int) []int {

	if val, isPresent := memo[targetSum]; isPresent {
		return val
	}

	if targetSum == 0 {
		return []int{}
	}

	if targetSum < 0 {
		return nil
	}

	for i := 0; i < len(nums); i++ {
		rem := targetSum - nums[i]
		res := howSum(rem, nums, memo)

		if res != nil {
			memo[targetSum] = append(res, nums[i])
			return memo[targetSum]
		}
	}

	memo[targetSum] = nil
	return nil
}
