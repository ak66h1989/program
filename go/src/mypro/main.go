package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
	"strings"
	//"os"
	"github.com/astaxie/beego/orm"
	_ "github.com/jinzhu/gorm/dialects/sqlite"
	"os"
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

func sayhelloName(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()       //解析url传递的参数，对于POST则解析响应包的主体（request body）
	//注意:如果没有调用ParseForm方法，下面无法获取表单的数据
	fmt.Println(r.Form) //这些信息是输出到服务器端的打印信息
	fmt.Println("path", r.URL.Path)
	fmt.Println("scheme", r.URL.Scheme)
	fmt.Println(r.Form["url_long"])
	for k, v := range r.Form {
		fmt.Println("key:", k)
		fmt.Println("val:", strings.Join(v, ""))
	}
	fmt.Fprintf(w, "Hello astaxie!") //这个写入到w的是输出到客户端的
}

func login(w http.ResponseWriter, r *http.Request) {
	fmt.Println("method:", r.Method) //获取请求的方法
	r.ParseForm()
	if r.Method == "GET" {
		t, _ := template.ParseFiles("views/login.html")
		log.Println(t.Execute(w, nil))
	} else {
		//请求的是登陆数据，那么执行登陆的逻辑判断
		fmt.Println("username:", r.Form["username"])
		fmt.Println("password:", r.Form["password"])
	}
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
	os.Chdir("C:/Users/ak66h_000/Dropbox/webscrap/go/src/mypro/") //need to change dir back

	http.HandleFunc("/", sayhelloName)       //设置访问的路由
	http.HandleFunc("/login", login)         //设置访问的路由
	err := http.ListenAndServe(":9090", nil) //设置监听的端口
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
