#!/bin/bash
cd ~/Documents/rust/ch8asm
cargo run -- -i ~/Documents/chip8/fib/fibonacci.asm8 -o ~/Documents/rust/Emu8O3/roms/fibtest.ch8
cd ~/Documents/rust/Emu8O3
cargo run -- --configuration ~/.config/emu8o3/config.toml -r roms/fibtest.ch8  --disable-timers --race 1075612 --comp