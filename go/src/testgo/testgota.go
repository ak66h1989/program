package main

import (
	//"github.com/kniren/gota/dataframe"
	"fmt"
	"github.com/montanaflynn/stats"
)

func main()  {
	//df := dataframe.LoadRecords(
	//	[][]string{
	//		[]string{"A", "B", "C", "D"},
	//		[]string{"a", "4", "5.1", "true"},
	//		[]string{"k", "5", "7.0", "true"},
	//		[]string{"k", "4", "6.0", "true"},
	//		[]string{"a", "2", "7.1", "false"},
	//	},
	//)
	//fmt.Println(df)
	//sel1 := df.Select([]int{0, 2})
	//sel2 := df.Select([]string{"A", "C"})
	//fmt.Println(sel1)
	//fmt.Println(sel2)
	s:=[][]float64{
		[]float64{1, 2, 3, 1},
		[]float64{5, 4, 5, 5},
		[]float64{6, 5, 7, 6},
		[]float64{6, 4, 6, 6},
		[]float64{7, 2, 7, 7},
	}
	fmt.Println(s)
	//t:=0.0




	//for i:=0;i<len(s[0]);i++{
	//	var sl []float64
	//	for _, j :=range s{
	//		sl=append(sl, j[1])
	//
	//	}
	//	mean, _ := stats.Mean(sl)
	//	//fmt.Println(mean)
	//	std, _ := stats.StdDevS(sl)
	//	//fmt.Println(std)
	//	for _, j :=range s{
	//		j[i]=(j[i]-mean)/std
	//	}
	//}
	//
	//
	//fmt.Println(s)

	s=normalize(s, 1)
	fmt.Println(s)
	//t=t/float64(len(s))
	//fmt.Println(t)
	//for _, j :=range s{
	//
	//	j[1]=j[1]-t
	//}
	//fmt.Println(s)
	//
	//var data = []float64{1, 2, 3, 4, 4, 5}
	//
	//Mean, _ := stats.Mean(data)
	//fmt.Println(Mean) // 3.5
	//
	//roundedMedian, _ := stats.Round(Mean, 0)
	//fmt.Println(roundedMedian) // 4

}

func normalize(s [][]float64, index int)[][]float64{
	for i:=index;i<len(s[0]);i++{
		var sl []float64
		for _, j :=range s{
			sl=append(sl, j[i])

		}
		mean, _ := stats.Mean(sl)
		//fmt.Println(mean)
		std, _ := stats.StdDevS(sl)
		//fmt.Println(std)
		for _, j :=range s{
			j[i]=(j[i]-mean)/std
		}
	}
	return s
}