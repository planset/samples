package main

import (
	"fmt"
	"log"
	"net/http"
	"os/exec"
)

func nextHandler(w http.ResponseWriter, r *http.Request) {
	out, err := exec.Command("/bin/cat", "bin/next").Output()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s", out)
	fmt.Fprintf(w, "OK: %s", out)
}

func backHandler(w http.ResponseWriter, r *http.Request) {
	out, err := exec.Command("/bin/cat", "bin/back").Output()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s", out)
	fmt.Fprintf(w, "OK: %s", out)
}

func main() {
	fmt.Printf("Starting server ... 0.0.0.0:18888\n")
	http.HandleFunc("/next", nextHandler)
	http.HandleFunc("/back", backHandler)
	http.ListenAndServe("0.0.0.0:18888", nil)
}
