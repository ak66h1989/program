package main

import (
	"fmt"

	"gopkg.in/kataras/iris.v4"
	//"github.com/kataras/go-template/django"
)

type Visitor struct {
	Username string
	Mail     string
	Data     []string `form:"mydata"`
}

func main() {
	//iris.UseTemplate(django.New()).Directory("./templates", ".html")
	iris.Get("/", func(ctx *iris.Context) {
		ctx.Render("form.html", nil)
	})

	iris.Post("/form_action", ind)

	iris.Listen(":8080")
}

func ind(ctx *iris.Context) {
	visitor := Visitor{}
	err := ctx.ReadForm(&visitor)
	if err != nil {
		fmt.Println("Error when reading form: " + err.Error())
	}
	fmt.Printf("\n Visitor: %v", visitor)
	fmt.Printf("\n Visitor: %v", visitor.Data)
	fmt.Printf("\n Visitor: %v", visitor.Data[0])
	fmt.Printf("\n Visitor: %v", visitor.Data[1:])
	visitor.Data=visitor.Data[1:]
	fmt.Println(visitor)
}
