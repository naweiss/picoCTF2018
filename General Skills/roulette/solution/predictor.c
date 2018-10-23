#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>

#define NUM_WIN_MSGS 10
#define MAX_WINS 16
#define ROULETTE_SIZE 36

void set_rand(long seed) {
  srand(seed);
}

void play_roulette() {
  printf("%d\n", (rand() % ROULETTE_SIZE)+1);
  for(int i = 0; i < MAX_WINS; i++) {
	  int spin = (rand() % ROULETTE_SIZE)+1;

	  printf("%d\n", spin);  
	  printf("%d\n", (rand() % ROULETTE_SIZE)+1);
  }
}

int main(int argc, char *argv[]) {
  setvbuf(stdout, NULL, _IONBF, 0);

  int seed = strtol(argv[1], NULL, 10);
  set_rand(seed);
  play_roulette();
  return 0;
}