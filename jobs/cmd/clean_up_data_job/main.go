package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Running cleanup data job")
	time.Sleep(10 * time.Second)
	fmt.Println("Cleanup data job completed")
}
