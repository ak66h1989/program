package main

import (
	"fmt"
	"strings"
)




type Point struct {
	X, Y int
}
var p Point
var m = make(map[string]string)

func a(){
	//pp:=&p
	//fmt.Println(*pp)
	//pp.X=10
	//pp.Y=20
	//point1 := &point
	//*point1="b"
	//fmt.Println(*point1)
	//fmt.Println(*pp)
	//m:=make(map[string]string)
	mm:=&m
	(*mm)["a"]="aa"
	(*mm)["b"]="bb"
	for _,v:=range *mm{
		fmt.Println(v)
	}
}
func b(){
	//m:=make(map[string]string)
	mm:=&m
	(*mm)["c"]="cc"
	for _,v:=range *mm{
		fmt.Println(v)
	}
}

var point string="a"

func Index(vs []string, t string) int {
	for i, v := range vs {
		if v == t {
			return i
		}
	}
	return -1
}

func Include(vs []string, t string) bool {
	return Index(vs, t) >= 0
}

func del(s []string, i int )[]string{
	var s1 []string
	s1=append(s1,s[:i]...)
	s1=append(s1,s[i+1:]...)
	return s1
}

func dels(s [][]string, i int ) [][]string{
	var s1 [][]string
	s1=append(s1,s[:i]...)
	s1=append(s1,s[i+1:]...)
	return s1
}

func remove(s []string, t string) []string{
	i:=Index(s, t)
	//r := append(a[:i], a[i+1:]...)
	//remove(a, i)
	var s1 []string
	s1=append(s1, s[:i]...)
	s1=append(s1, s[i+1:]...)
	return s1
}

func insert(s []string, i int, t string )[]string{
	var s1 []string
	s1=append(s1,s[:i]...)
	s1=append(s1,t)
	s1=append(s1,s[i:]...)
	return s1
}

func is (s , t string ) bool{
	if s == t{
		return true
	}else{
		return false
	}
}

func isNaT (s string) bool{
	if s == "NaT"{
		return true
	}else{
		return false
	}
}

func isnil (s string) bool{
	if s == "<nil>"{
		return true
	}else{
		return false
	}
}

func All(vs []string, f func(string) bool) bool {
	for _, v := range vs {
		if !f(v) {
			return false
		}
	}
	return true
}

func main() {
	//pp:=&p
	//pp.X=100
	//pp.Y=200
	//fmt.Println(*pp)
	  // {20, 20}
	b()
	a()
	var strs = []string{"peach", "apple", "pear", "plum"}
	//fmt.Println(strs[Index(strs, "pear")])
	//fmt.Println(point)
	//r:=delete(strs, "peach")
	//fmt.Println(r)
	//r1:=remove(strs, 1)
	//fmt.Println(r1)
	//
	//i:=1
	//
	//fmt.Println(append(strs[:i], strs[i+1:]...))
	//remove(strs, 1)
	//remove(strs,1)
	//c:=remove(strs,1)
	//fmt.Println(c)
	//remove(strs, 1)
	fmt.Println(strs)

	//src := []int{1, 2, 3, 4, 5}
	//dest := make([]int, len(src), (cap(src) + 1) * 2)
	//fmt.Println(copy(dest, src))  // 5
	//fmt.Println(src)              // [1 2 3 4 5]
	//fmt.Println(dest)
	strs=remove(strs, "apple")
	fmt.Println(strs)

	fmt.Println(append(strs, strs...))
	strs=del(strs, 1)
	fmt.Println(strs)
	strs=insert(strs,1, "abc")
	fmt.Println(strs)
	b:=Include(strs, "abc")
	fmt.Println(b)
	var strs1 [][]string
	s:= []string{"peach", "apple", "pear", "plum"}
	s1:= []string{"peach1", "apple1", "pear1", "plum1"}
	strs1=append(strs1, s)
	strs1=append(strs1, s1)

	fmt.Println(strs1)
	strs1=dels(strs1, 0)
	fmt.Println(strs1)
	strs2 := make([][]int, 3)
	//var strs2 [][]int
	strs2[0] = make([]int, 3)
	strs2[0][0]=1
	fmt.Println(strs2)
	//fmt.Println([]{"peach", "apple", "pear", "plum"})
	a:=is("a","a")
	fmt.Println(a)
	a=isNaT("NaT")
	fmt.Println(a)
	a=isnil("<nil>")
	fmt.Println(a)
	a=All(s, isnil)
	fmt.Println(a)

	fmt.Println(strings.Replace("peach", "z", "a", -1))
}

