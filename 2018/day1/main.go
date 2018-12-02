package main

import (
	"bufio"
	"log"
	"os"
	"strconv"

	"go.uber.org/zap"
)

func main() {
	baselogger, err := zap.NewDevelopment()
	if err != nil {
		log.Fatalf("Error setting up zap logger: %v", err)
	}
	logger := baselogger.Sugar()
	var freq int64
	d := make(map[int64]int8)
	for {
		f, err := os.Open("input")
		if err != nil {
			logger.Fatalw("Could not open input", "err", err)
		}
		s := bufio.NewScanner(f)
		for s.Scan() {
			t := s.Text()
			i, err := strconv.Atoi(t)
			if err != nil {
				logger.Fatalw("Could not parse text to int", "text", t, "err", err)
			}
			//logger.Debugw("Parsed int", "int", i)
			freq += int64(i)
			d[freq]++
			if d[freq] > 1 {
				break
			}
		}
		if d[freq] > 1 {
			break
		}
		//logger.Debugw("Finished iteration", "freq", freq, "d.len", d)
	}
	logger.Infow("Finished run", "result", freq)
}
