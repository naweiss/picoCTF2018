# The easiest way to understand assembly is running it ;)
# So, lets compile the assembly into executable and run it
nasm -f elf32 ../comp.nasm -o comp.o
gcc -m32 comp.o -o comp

./comp
# If you have 64-bit system and you can't run 32-bit files add "qemu-i386" before "./comp"

# Note: apparently the flag is broken (switch the '3' at the end with '}')