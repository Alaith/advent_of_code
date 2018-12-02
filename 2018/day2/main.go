package main

import (
	"bufio"
	"log"
	"os"
	"strings"

	"go.uber.org/zap"
)

func main() {
	// Set up logging
	baselogger, err := zap.NewDevelopment()
	if err != nil {
		log.Fatalf("Error setting up zap logger: %v", err)
	}
	logger := baselogger.Sugar()
	// Open input
	f, err := os.Open("input")
	if err != nil {
		logger.Fatalw("Could not open input", "err", err)
	}
	// scan input
	s := bufio.NewScanner(f)
	// setup vars
	lines := make([]string, 0, 100)
	var r string
	//
ml:
	for s.Scan() {
		t := s.Text()
		for _, l := range lines {
			if chardiff(l, t) == 1 {
				var res strings.Builder
				for i := range l {
					if l[i] == t[i] {
						res.WriteByte(l[i])
					}
				}
				r = res.String()
				break ml
			}
		}
		lines = append(lines, t)
	}
	logger.Infow("Finished run", "result", r)
}

func chardiff(a string, b string) int {

	diffs := len(a)
	for i := range a {
		if a[i] == b[i] {
			diffs--
		}
	}
	return diffs
}
