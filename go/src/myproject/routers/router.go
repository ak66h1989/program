package routers

import (
	"myproject/controllers"
	"github.com/astaxie/beego"
)

func init() {
	beego.Router("/", &controllers.IndexController{})
	beego.Router("/hello", &controllers.MainController{})
	beego.Router("/listfield", &controllers.ListfieldController{})
	beego.Router("/mline", &controllers.MlineController{})
}
