package main

import (
	_ "myproject/routers"
	"github.com/astaxie/beego"
	_ "github.com/jinzhu/gorm/dialects/sqlite" // import your required driver
	//"html/template"
	"os"
)

//type MainController struct {
//	beego.Controller
//}
//
//func (this *MainController) Get() {
//	this.Ctx.WriteString("hello world")
//}


func main() {
	//x="b"
	//a()

	os.Chdir("C:/Users/ak66h_000/Dropbox/webscrap/go/src/myproject/")
	beego.Run()
}


