package main

import (
	_ "myproject/routers"
	"github.com/astaxie/beego"
	"github.com/astaxie/beego/orm"
	_ "github.com/jinzhu/gorm/dialects/sqlite" // import your required driver
	//"html/template"
	"fmt"
	"strings"
	"os"
)

//type MainController struct {
//	beego.Controller
//}
//
//func (this *MainController) Get() {
//	this.Ctx.WriteString("hello world")
//}

type Friend struct {
	Fname string
}

type Person struct {
	UserName string
	Emails   []string
	Friends  []*Friend
}

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

func columns(table string) []string{
	o := orm.NewOrm()
	var lists []orm.ParamsList

	num, err := o.Raw("SELECT sql FROM sqlite_master where name= ?",table).ValuesList(&lists)
	if err == nil && num > 0 {
		fmt.Println(lists[0][0]) // slene
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


func main() {
	l:=columns("forweb")
	for i,v:=range l{
		l[i]= strings.Trim(v, " ")
		fmt.Println(v)
	}
	mops:=dbtables("mops")
	fmt.Println(mops)
	mysum:=dbtables("mysum")
	fmt.Println(mysum)
	summary:=dbtables("summary")
	fmt.Println(summary)
	tse:=dbtables("tse")
	fmt.Println(tse)
	os.Chdir("C:/Users/ak66h_000/Dropbox/webscrap/go/src/myproject/")
	beego.Run()

}


