package main

import "fmt"
import (
	"testpackage/math"
)

func main() {
	xs := []float64{1,2,3,4}
	avg := math1.Average(xs)
	fmt.Println(avg)
}
