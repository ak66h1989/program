package controllers

import (
	"github.com/astaxie/beego"
	"strings"
	"fmt"
	"github.com/astaxie/beego/orm"
	_ "github.com/jinzhu/gorm/dialects/sqlite"
	"os"
	"time"
	"strconv"
)

func init() {
	// register model
	//orm.RegisterModel(new(forweb))
	// set default database
	os.Chdir("C:/Users/ak66h_000/Documents/db/")
	orm.RegisterDriver("sqlite", orm.DRSqlite)
	orm.RegisterDataBase("default", "sqlite3", "mysum.sqlite3?charset=utf8")
	orm.RegisterDataBase("mops", "sqlite3", "mops.sqlite3?charset=utf8")
	orm.RegisterDataBase("mysum", "sqlite3", "mysum.sqlite3?charset=utf8")
	orm.RegisterDataBase("summary", "sqlite3", "summary.sqlite3?charset=utf8")
	orm.RegisterDataBase("tse", "sqlite3", "tse.sqlite3?charset=utf8")
}

func dbtables(db string) []string{
	o := orm.NewOrm()
	o.Using(db)
	var lists []orm.ParamsList
	var slice []string
	num, err := o.Raw("SELECT name FROM sqlite_master where type= 'table'").ValuesList(&lists)
	if err == nil && num > 0 {
		for i,v:=range lists{
			slice=append(slice, fmt.Sprintf("%v",v[0]))
			fmt.Println(slice[i])
		}
		return slice
	}
	return  nil
}

func columns(db string, table string) []string{
	o := orm.NewOrm()
	o.Using(db)
	var lists []orm.ParamsList

	num, err := o.Raw("SELECT sql FROM sqlite_master where name= ?",table).ValuesList(&lists)
	if err == nil && num > 0 {
		fmt.Println(lists[0][0])
		s := fmt.Sprintf("%v",lists[0][0])
		s=strings.Replace(s, "`", "", -1)
		s=strings.Split(s, "PRIMARY KEY")[0]
		fmt.Println(s)
		l:=strings.Split(s, ",")
		l=l[:len(l)-1]
		l[0]=strings.Split(l[0], "(")[1]
		//for i,v:=range l{
		//	l[i]= strings.Trim(v, " ")
		//	fmt.Println(v)
		//}
		return l

		//fmt.Printf(a)
		//s:=lists[0][0]
		//fmt.Printf("%q\n", strings.Split(s, ","))
		//fmt.Printf("%q\n", lists[0][0])
	}
	fmt.Println(0)
	return nil
}

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

func remove(s []string, t string)[]string{
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

func isnull (s string) bool{
	if s == "null"{
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

func stof(t string ) float64{
	f, _ := strconv.ParseFloat(t, 64)
	return f
}



func Map(vs []string, f func(string) float64) []float64 {
	vsm := make([]float64, len(vs))
	for i, v := range vs {
		vsm[i] = f(v)
	}
	return vsm
}

type MainController struct {
	beego.Controller
}

type IndexController struct {
	beego.Controller
}

type ListfieldController struct {
	beego.Controller
}

type MlineController struct {
	beego.Controller
}

var Tbdb = make(map[string]string)

func (c *MainController) Get() {
	c.Data["Website"] = "beego.me"
	c.Data["Email"] = "astaxie@gmail.com"
	c.Data["a"] = "beego.me"
	c.Data["b"] = 1
	c.TplName = "test.html"
}

var mops []string
var mysum []string
var summary []string
var tse []string
func (c *IndexController) Get() {
	//l:=columns("forweb")
	//for i,v:=range l{
	//	l[i]= strings.Trim(v, " ")
	//	fmt.Println(v)
	//}

	//var s [][]string
	//s:=append(mops[:3],summary[:10])
	//s:=summary[:10]
	//fmt.Println(mops)
	//fmt.Println(mysum)
	//fmt.Println(summary)
	//fmt.Println(tse)
	mops:=&mops
	*mops=dbtables("mops")
	mysum:=&mysum
	*mysum=dbtables("mysum")
	summary:=&summary
	*summary=dbtables("summary")
	tse:=&tse
	*tse=dbtables("tse")
	c.Data["mops"] = *mops
	c.Data["mysum"] = *mysum
	c.Data["summary"] = *summary
	c.Data["tse"] = *tse
	//c.Data["s"] = s
	tbdb:=&Tbdb

	for _,v:=range *mops{
		(*tbdb)[v]="mops"
	}
	for _,v:=range *mysum{
		(*tbdb)[v]="mysum"
	}
	for _,v:=range *summary{
		(*tbdb)[v]="summary"
	}
	for _,v:=range *tse{
		(*tbdb)[v]="tse"
	}

	//for _,v:=range mops{
	//	fmt.Println(v)
	//}
	//for _,v:=range mysum{
	//	fmt.Println(v)
	//}
	//for _,v:=range summary{
	//	fmt.Println(v)
	//}
	//for _,v:=range tse{
	//	fmt.Println(v)
	//}

	//for i,_:=range Tbdb{
	//	fmt.Println(Tbdb[i])
	//}
	//s:=[][]int{{1, 2, 3}, {4, 5, 6}}

	type Human struct {
		Name string
		Age int
		Weight int
	}
	var hs [] Human
	a:=24
	n:="Tom"
	h:=Human{Age:a, Name:n}
	hs=append(hs,h)
	c.Data["h"] = &h
	h=Human{Age:20, Name:"Tomy"}
	hs=append(hs,h)

	c.Data["hs"] = hs
	for i, v:=range hs{
		fmt.Println(i,v)
	}
	c.Data["a"] = "a"
	c.TplName = "test.html"

}

var dbtable string
var fields []string
func (c *ListfieldController) Post() {
	for i,_:=range Tbdb{
		fmt.Println(i, Tbdb[i])
	}
	dbtable:=&dbtable
	*dbtable = c.GetString("dbtable")
	fmt.Println(*dbtable)
	db:=Tbdb[*dbtable]
	fmt.Println(db)
	fields:=&fields
	*fields = columns(db, *dbtable)
	c.Data["fields"] = *fields
	for i,v:=range columns(db, *dbtable){
		fmt.Println(i,v)
	}
	c.Data["mops"] = mops
	c.Data["mysum"] = mysum
	c.Data["summary"] = summary
	c.Data["tse"] = tse
	c.TplName = "test.html"
}

type Mline struct{
	J int
	Cols []string
	List1 [][]float64
	Y []string
	Ymd []string
	Width string
	Height string
	Rangeselector string
}
var mll, mll1 []Mline
var l, l1 [][]string
var i int = 0
var j int = 0
func (c *MlineController) Post() {
	cols := c.GetStrings("cols")
	fmt.Println(cols)
	if Include(cols, "年月日"){
		cols=remove(cols, "年月日")
		cols=insert(cols, 0, "年月日")
	}else{
		cols=insert(cols, 0, "年月日")
	}

	for _, col:=range cols{
		println(col)
	}

	o := orm.NewOrm()
	o.Using(Tbdb[dbtable])
	var lists []orm.ParamsList
	sql := fmt.Sprintf("SELECT `%s` from `%s`", strings.Join(cols,"`,`"), dbtable)
	fmt.Println(cols)
	fmt.Println(sql)
	num, err := o.Raw(sql).ValuesList(&lists)
	fmt.Println(num, err)
	if err == nil && num > 0 {
		//fmt.Println(lists)
		fmt.Println(lists[0][0])
		fmt.Println(len(lists))

		list :=make([][]string, len(lists))
		for  i := 0; i < len(lists); i++{
			list[i]=make([]string, len(lists[i]))
			for j:= 0; j < len(lists[i]); j++{
				list[i][j]=fmt.Sprintf("%v",lists[i][j])
				list[i][j]=strings.Replace(list[i][j], "NaN", "null", -1)
				list[i][j]=strings.Replace(list[i][j], "<nil>", "null", -1)
				list[i][j]=strings.Replace(list[i][j], "'", "", -1)
			}
			fmt.Println(list[i])
		}
		//fmt.Println(list)

		const shortForm = "2006-01-02"
		var list1 [][]float64
		var ymd []string
		for  i := 0; i < len(lists); i++{
			t, _ := time.Parse(shortForm, list[i][0])
			ymd= append(ymd, strconv.FormatInt(t.Unix(), 10))
			//fmt.Println(list[i][0], t.Unix())
			if (list[i][0]=="null")||(All(list[i][1:], isnull)){
				//list=dels(list, i)

				//fmt.Println("null")
			}else{
				//fmt.Println(list[i][0], t.Unix())
				list[i][0]=strconv.FormatInt(t.Unix(), 10)
				list1= append(list1, Map(list[i], stof))

			}

		}

		y:=cols[1:]
		width:= c.GetString("width")
		height:= c.GetString("height")
		rangeselector:= c.GetString("rangeselector")
		fmt.Println(rangeselector)
		m:=Mline{
			J:j,
			Cols:cols,
			List1:list1,
			Y:y,
			Ymd:ymd,
			Width:width,
			Height:height,
			//Rangeselector:rangeselector,

		 }
		//width := c.GetString("width")
		//height := c.GetString("height")
		//rangeselector := c.GetString("rangeselector")
		//var mll [][][]string
		//var l[][]string
		//l = append(l, strconv.Itoa(j), cols, list1, cols, cols[1:], ymd, width, height, rangeselector)
		mll:=&mll
		*mll = append(*mll, m)
		c.Data["fields"] = fields
		c.Data["mops"] = mops
		c.Data["mysum"] = mysum
		c.Data["summary"] = summary
		c.Data["tse"] = tse
		c.Data["mll"] = &mll

		c.Data["a"] = "aa"
		//s := fmt.Sprintf("%v",lists[0][0])
		//s=strings.Replace(s, "`", "", -1)
		//s=strings.Split(s, "PRIMARY KEY")[0]
		//fmt.Println(s)
		//l:=strings.Split(s, ",")
		//l=l[:len(l)-1]
		//l[0]=strings.Split(l[0], "(")[1]
		////for i,v:=range l{
		////	l[i]= strings.Trim(v, " ")
		////	fmt.Println(v)
		////}
		//return l
		//
		////fmt.Printf(a)
		////s:=lists[0][0]
		////fmt.Printf("%q\n", strings.Split(s, ","))
		////fmt.Printf("%q\n", lists[0][0])
		//fmt.Println(list1)
	}else{
		fmt.Println(0)
		//return nil
	}
	//for i, v :=range(mll){
	//	fmt.Println(i, v)
	//}
	c.Data["tab"] = "#tabs-2"
	c.TplName = "test.html"
}
