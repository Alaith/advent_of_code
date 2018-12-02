package main

import (
	"bufio"
	"log"
	"os"

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
	// VAR X int = 1
	var r bool

	// main input scan loop
ml:
	for s.Scan() {
		t := s.Text()
		_ = t
		break ml
	}
	logger.Infow("Finished run", "result", r)
}
