package main

import "fmt"

func main() {

	fmt.Println(fibo(1000, map[float64]float64{}))
}

func fibo(num float64, memo map[float64]float64) float64 {

	if memo[num] != 0 {
		return memo[num]
	}

	if num <= 2 {
		return 1
	}

	memo[num] = fibo(num - 1, memo) + fibo(num - 2, memo)

	return memo[num]
}
