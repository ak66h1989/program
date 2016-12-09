// ./main.go
package main

import (
	//"github.com/kataras/go-template/django"
	"gopkg.in/kataras/iris.v4"
	"fmt"
	"os"
	"github.com/astaxie/beego/orm"
	_ "github.com/jinzhu/gorm/dialects/sqlite" // import your required driver
	"strings"
	"strconv"
	"time"
	"github.com/kataras/go-template/django"
	"encoding/json"
	"regexp"
	"github.com/montanaflynn/stats"
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

var Tbdb = make(map[string]string)
var mops []string
var mysum []string
var summary []string
var tse []string
func IndexController(ctx *iris.Context){
	mops:=&mops
	*mops=dbtables("mops")
	mysum:=&mysum
	*mysum=dbtables("mysum")
	summary:=&summary
	*summary=dbtables("summary")
	tse:=&tse
	*tse=dbtables("tse")
	m := make(map[string]interface{})
	m["mops"] = *mops
	m["mysum"] = *mysum
	m["summary"] = *summary
	m["tse"] = *tse
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
	//for k, v :=range m{
	//	fmt.Println(k, v)
	//}

	ctx.Render("indexdj.html",m , iris.RenderOptions{"gzip": true})
}
type DbtableR struct{
	Dbtable string `form:"dbtable"`
}
var dbtable string
var fields []string
func ListfieldController(ctx *iris.Context) {
	for i,_:=range Tbdb{
		fmt.Println(i, Tbdb[i])
	}
	dbtable:=&dbtable
	req:=DbtableR{}
	err := ctx.ReadForm(&req)
	if err != nil {
		fmt.Println("Error when reading form: " + err.Error())
	}
	*dbtable = req.Dbtable
	fmt.Println(*dbtable)
	db:=Tbdb[*dbtable]
	fmt.Println(db)
	fields:=&fields
	*fields = columns(db, *dbtable)
	m := make(map[string]interface{})
	m["fields"] = *fields
	for i,v:=range columns(db, *dbtable){
		fmt.Println(i,v)
	}
	m["mops"] = mops
	m["mysum"] = mysum
	m["summary"] = summary
	m["tse"] = tse
	ctx.Render("indexdj.html",m , iris.RenderOptions{"gzip": true})
}

type Mline struct{
	J int
	Cols string
	Data string
	List1 [][]float64
	Y []string
	Ymd []string
	Width string
	Height string
	Rangeselector string
}

type MlineR struct{
	Cols []string `form:"cols"`
	Width string `form:"width"`
	Height string `form:"height"`
	Rangeselector string `form:"rangeselector"`
}

var mll, mll1 []Mline
var l, l1 [][]string
var i int = 0
var j int = 0
func MlineController(ctx *iris.Context) {
	jp:=&j
	*jp+=1
	req:=MlineR{}
	err := ctx.ReadForm(&req)
	if err != nil {
		fmt.Println("Error when reading form: " + err.Error())
	}
	fmt.Println(req.Cols)
	if Include(req.Cols, "年月日"){
		req.Cols=remove(req.Cols, "年月日")
		req.Cols=insert(req.Cols, 0, "年月日")
	}else{
		req.Cols=insert(req.Cols, 0, "年月日")
	}

	for _, col:=range req.Cols{
		println(col)
	}

	o := orm.NewOrm()
	o.Using(Tbdb[dbtable])
	var lists []orm.ParamsList
	sql := fmt.Sprintf("SELECT `%s` from `%s`", strings.Join(req.Cols,"`,`"), dbtable)
	fmt.Println(req.Cols)
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
			//fmt.Println(list[i])
		}
		//fmt.Println(list)

		const shortForm = "2006-01-02"
		var list1 [][]float64
		var ymd []string
		for  i := 0; i < len(lists); i++{
			t, _ := time.Parse(shortForm, list[i][0])
			ymd= append(ymd, strconv.FormatInt(t.Unix()*1000, 10))
			//fmt.Println(list[i][0], t.Unix())
			if (list[i][0]=="null")||(All(list[i][1:], isnull)){
				//list=dels(list, i)
				//fmt.Println("null")
			}else{
				//fmt.Println(list[i][0], t.Unix())
				list[i][0]=strconv.FormatInt(t.Unix()*1000, 10)
				list1= append(list1, Map(list[i], stof))
			}
		}

		data, _ := json.Marshal(list1)
		data1:=string(data)
		cols, _ := json.Marshal(req.Cols)
		cols1 := string(cols)
		fmt.Println(cols1)
		y:=req.Cols[1:]
		width:= req.Width
		height:= req.Height
		var rangeselector string
		if req.Rangeselector=="true"{
			rangeselector= req.Rangeselector
		}else{
			rangeselector= "false"
		}
		fmt.Println(rangeselector)

		st:=Mline{
			J:j,
			Cols:cols1,
			Data:data1,
			List1:list1,
			Y:y,
			Ymd:ymd,
			Width:width,
			Height:height,
			Rangeselector:rangeselector,

		}

		mllp:=&mll
		*mllp = append(*mllp, st)
		mll1p:=&mll1
		*mll1p = append(*mll1p, st)
		m := make(map[string]interface{})
		m["fields"] = fields
		m["mops"] = mops
		m["mysum"] = mysum
		m["summary"] = summary
		m["tse"] = tse
		m["mll"] = &mll

		m["tab"] = "#tabs-2"
		ctx.Render("indexdj.html",m , iris.RenderOptions{"gzip": true})
	}else{
		fmt.Println(0)
		//return nil
	}
	//for i, v :=range(mll){
	//	fmt.Println(i, v)
	//}

}

func delmll(s []Mline, i int )[]Mline{
	var s1 []Mline
	s1=append(s1,s[:i]...)
	s1=append(s1,s[i+1:]...)
	return s1
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

type Scale struct{
	Dy string `form:"dy"`
}
func ScaleController(ctx *iris.Context) {
	m := make(map[string]interface{})
	m["fields"] = fields
	m["mops"] = mops
	m["mysum"] = mysum
	m["summary"] = summary
	m["tse"] = tse
	m["tab"] = "#tabs-2"
	mllp:=&mll
	mll1p:=&mll1
	req:=Scale{}
	err := ctx.ReadForm(&req)
	if err != nil {
		fmt.Println("Error when reading form: " + err.Error())
	}
	r, _ := regexp.Compile("([0-9]+)")
	j, err := strconv.Atoi(r.FindString(req.Dy))

	r, _ = regexp.Compile("([a-z]+)")
	fmt.Println(r.FindString(req.Dy))
	if r.FindString(req.Dy)=="raw"{
		for i, v :=range mll1{
			if v.J==j{
				(*mll1p)[i]=mll[i]
			}

		}

		m["mll"] = mll1
		ctx.Render("indexdj.html",m ,iris.RenderOptions{"gzip": true})
	}

	if r.FindString(req.Dy)=="normalize"{
		for i, v :=range mll1{
			if v.J==j{
				(*mll1p)[i].List1=normalize((*mll1p)[i].List1, 1)
				data, _ := json.Marshal((*mll1p)[i].List1)
				(*mll1p)[i].Data=string(data)
				fmt.Println((*mll1p)[i].List1)
			}

		}
		m["mll"] = mll1
		ctx.Render("indexdj.html",m ,iris.RenderOptions{"gzip": true})
	}


	if r.FindString(req.Dy)=="remove"{
		fmt.Println("remove")
		for i, v :=range mll1{
			if v.J==j{
				(*mllp)=delmll(mll, i)
				(*mll1p)=delmll(mll1, i)
			}

		}

		m["mll"] = mll1
		ctx.Render("indexdj.html",m ,iris.RenderOptions{"gzip": true})
	}

}

func main() {
	os.Chdir("C:/Users/ak66h_000/Dropbox/webscrap/go/src/irispro/")
	//iris.Get("/hi", hi)
	iris.UseTemplate(django.New()).Directory("./templates", ".html")

	iris.Get("/mypage", func(ctx *iris.Context) {
		s := make([]int, 2)
		s[0]=0
		s[0]=1
		m:=map[string]interface{}{"username": "iris", "is_admin": true, "num": 1, "s":s}
		ctx.Render("mypage.html",m , iris.RenderOptions{"gzip": true})
	})

	iris.Get("/hi", func(ctx *iris.Context) {

		ctx.Render("hi.html", map[string]interface{}{"Name": "iris", "name": "iris1"}, iris.RenderOptions{"gzip": true})
	})

	iris.Get("/", IndexController)
	iris.Post("/listfield", ListfieldController)
	iris.Post("/mline", MlineController)
	iris.Post("/scale", ScaleController)
	iris.Listen(":8080")
}
//func hi(ctx *iris.Context) {
//	ctx.MustRender("hi.html", struct{ Name string }{Name: "iris"})
//}
