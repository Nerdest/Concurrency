package main

import (
"container/list"
"fmt"
"math/rand"
"time"
)

var c = make(chan int, 3)

func Producer() {
	fmt.Printf("start prod\n")
	for i := 0; i < 10; i++ {
		r := rand.Intn(1000000)
		c<-r
		fmt.Printf("Producer added %d\n",r)
		//time.Sleep(time.Duration(rand.Intn(10)) * time.Millisecond)
	}
}
func Consumer1() {
	fmt.Printf("start con 1\n")
	for i := 0; i < 10; i++ {
		r  := <-c
		fmt.Printf("consumer 1 removed %d\n",r)
		time.Sleep(time.Duration(rand.Intn(300)) * time.Millisecond)
	}
}
func Consumer2() {
	fmt.Printf("start con 2\n")
	for i := 0; i < 10; i++ {
		r := <-c
		fmt.Printf("consumer 2 removed %d\n",r)
		time.Sleep(time.Duration(rand.Intn(300)) * time.Millisecond)
	}
}
func main() {
	rand.Seed( time.Now().UTC().UnixNano())
	go Producer()
	go Consumer1()
	go Consumer2()
	time.Sleep(10000 * time.Millisecond)
}
