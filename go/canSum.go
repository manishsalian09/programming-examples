package main

import "fmt"

func main() {

	fmt.Println(canSum(300, []int{1, 2, 3 ,4, 5, 6, 7, 8, 9}, map[int]bool{}))
}

func canSum(targetSum int, num []int, memo map[int]bool) bool {

	if val, ok := memo[targetSum]; ok {
		return val
	}

	if targetSum == 0 {
		return true
	}

	if targetSum < 0  {
		return false
	}

	for i:=0; i<len(num); i++ {
		memo[targetSum] = canSum(targetSum - num[i], num, memo)
		if memo[targetSum] {
			return true
		}
	}

	return false

}
