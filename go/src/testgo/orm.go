package main

import (
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/sqlite"
	"fmt"
	"os"
)
type Forweb struct {
	年月日 string
	證券代號 string
	time int
	收盤價 float64
}
//func (Forweb) TableName() string {
//	return "forweb"
//}

type Result struct {
	證券代號 string
	time int
	收盤價 float64
}

func main() {
	os.Chdir("C:/Users/ak66h_000/Documents/db/")
	db, err := gorm.Open("sqlite3", "mysum.sqlite3")
	//fmt.Println(err)
	//fmt.Println(db)
	//var forweb = Forweb{}
	//fmt.Println(db.Find(&forweb))
	var result Result
	db.Raw("SELECT [證券代號], [time], [收盤價] FROM forweb").Scan(&result)

	rows, err := db.Raw("select 年月日, 證券代號, time, 收盤價 from forweb").Rows()

	for rows.Next() {
		var 年月日 string
		var 證券代號 string
		var time int
		var 收盤價 float64
		err = rows.Scan(&年月日,&證券代號, &time, &收盤價)
		//err = rows.Scan(&證券代號, &time)
		fmt.Println(err)
	}


	fmt.Println(db.HasTable("forweb"))
	defer db.Close()
}
