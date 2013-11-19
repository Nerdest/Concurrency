package main

import (
"fmt"
"math/rand"
"time"
)

var master = []int{0,1}
var c = make(chan int,1)
var count = 0
func writer() {
	<-c
	fmt.Printf("The first value of the array before writing is %d\n",master[0])
	master[0] += 1
	fmt.Printf("The second value of the array before writing is %d\n",master[1])
	master[1] += 1
	c<-1
		time.Sleep(time.Duration(rand.Intn(300)) * time.Millisecond)

	
}

func reader(id string) {
	if(count < 1){<-c}
	count += 1
	fmt.Printf("reader %s sees %d  as the value for element 1 \n",id,master[0])
	fmt.Printf("reader %s sees %d  as the value for element 2 \n",id,master[1])
	count -= 1 
	if(count < 1){c<-1}
	time.Sleep(time.Duration(300000) * time.Millisecond)

}
func main() {
rand.Seed( time.Now().UTC().UnixNano())
c <- 1
for i := 0; i < 10; i++ {
	go reader("1")
	go writer()
	go reader("2")
	go reader("3")
	go reader("4")
	}
time.Sleep(time.Duration(1000) * time.Millisecond)
}


