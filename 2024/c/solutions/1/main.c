#include <stdio.h>
#include "input.h"

int main() {
  int line_count;
  char **lines = read_lines("input.txt", &line_count);
  if (lines == NULL) {
    fprintf(stderr, "Failed to read lines.");
    free_lines(lines, line_count);
    return 1;
  }
  for (int i = 0; i < line_count; i++) {
    printf("%s\n", lines[i]);
  }
  free_lines(lines, line_count);
  return 0;
}