package main

import "fmt"

func main() {
	fmt.Println(recurFactorial(5))
}

func recurFactorial(n int) int {
	if n == 1 {
		return 1
	} else {
		return n * recurFactorial(n-1)
	}
}
