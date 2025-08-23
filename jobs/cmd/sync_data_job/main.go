package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Running sync data job")
	time.Sleep(10 * time.Second)
	fmt.Println("Sync data job completed")
}
