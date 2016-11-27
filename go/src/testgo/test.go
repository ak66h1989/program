package main

import (
	"fmt"
	"database/sql"
	_ "github.com/mattn/go-sqlite3"
	"os"
)

func main() {
	os.Chdir("C:\\Users\\ak66h_000\\Documents\\db\\")
	db, err := sql.Open("sqlite3", "tse.sqlite3")
	fmt.Println(db)
	fmt.Println(err)
	rows, err := db.Query("SELECT 年月日, [收盤價] FROM [每日收盤行情(全部(不含權證、牛熊證))]")
	fmt.Println(rows)
	fmt.Println(err)
	fmt.Println("Hello, World!")
	fmt.Println(rows.Columns())
	for rows.Next() {
		var a string
		var 收盤指數 float64
		err = rows.Scan(&a, &收盤指數)
		fmt.Println(err)
		fmt.Println(a)
		fmt.Println(收盤指數)
		//fmt.Println(rows.Scan())
	}

}

