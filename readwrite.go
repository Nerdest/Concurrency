package main

import (
"fmt"
"math/rand"
"time"
)

var master = 5
func writer() {
	for i := 0; i < 10; i++ {
	fmt.Printf("the value of the number is %d\n",master)
	master = rand.Intn(300)
	//time.Sleep(time.Duration(rand.Intn(300)) * time.Millisecond)
	}
}

func reader(id string) {
	for i := 0; i < 10; i++ {
	fmt.Printf("reader %s sees the value as %d\n",id,master)
	time.Sleep(time.Duration(rand.Intn(300)) * time.Millisecond)
	}	
}
func main() {
rand.Seed( time.Now().UTC().UnixNano())
go reader("1")
go reader("2")
go reader("3")
go reader("4")
go writer()
time.Sleep(10000 * time.Millisecond)


}


