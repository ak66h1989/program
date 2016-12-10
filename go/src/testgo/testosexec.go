package main

import(
	//"fmt"
	"os/exec"
	//"log"
	"fmt"
)

//func main(){
//	exec.Command("cmd", "cd %GOPATH%/src/irispro").Run()
//	exec.Command("cmd", "go build testiris.go").Run()
//	exec.Command("cmd", "testiris").Run()
//	//if err := c.Run(); err != nil {
//	//	fmt.Println("Error: ", err)
//	//}
//}


func main() {
	//out, err := exec.Command("cmd.exe","/C","dir").Output()
	////out, err := exec.Command("cmd.exe","/C","cd","C:/Users/ak66h_000/Dropbox/webscrap/go/src/irispro/","dir").Output()
	//
	//if err != nil {
	//	log.Fatal(err)
	//}
	//fmt.Println(out)
	//fmt.Println(string(out))
	//c := exec.Command("cmd", "/C", "dir")

	//exec.Command("cmd", "/C", "dir").Run()
	c := exec.Command("cmd", "/C", "cd","C:/Users/ak66h_000/Dropbox/webscrap/go/src/irispro/", "go","build", "testiris.go", "testiris")
	//exec.Command("cmd", "/C", "go","build", "testiris.go").Run()
	//exec.Command("cmd", "/C", "testiris").Run()
	if err := c.Run(); err != nil {
		fmt.Println("Error: ", err)
	}
}
