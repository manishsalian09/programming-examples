package main

import (
	"fmt"
	"strconv"
)

func main() {

	fmt.Println(gridTraveller(18, 18, map[string]int{}))
}

func gridTraveller(row int, col int, memo map[string]int) int {

	gridSize := strconv.Itoa(row) + "," + strconv.Itoa(col)
	
	if (memo[gridSize] != 0) {
		return memo[gridSize]
	}

	if row <= 0 || col <= 0 {
		return 0
	}

	if (row == 1 && col == 1) {
		return 1
	}

	memo[gridSize] = gridTraveller(row - 1, col, memo) + gridTraveller(row, col - 1, memo)

	return memo[gridSize]

}
