#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* read_file(const char *filename) {
  FILE *file = fopen(filename, "r");
  if (file == NULL) {
    perror("Error opening file");
    return NULL;
  }

  fseek(file, 0, SEEK_END);
  long file_size = ftell(file);
  fseek(file, 0, SEEK_SET);

  char *content = (char*) malloc(file_size + 1);
  if (content == NULL) {
    perror("Memory allocation failed");
    fclose(file);
    return NULL;
  }

  fread(content, 1, file_size, file);
  content[file_size] = '\0';

  fclose(file);
  return content;
}

char** read_lines(const char *filename, int *line_count) {
  FILE *file = fopen(filename, "r");
  if (file == NULL) {
    perror("Error opening file");
    return NULL;
  }

  char **lines = NULL;
  char *line = NULL;
  size_t len = 0;
  ssize_t read;
  int count = 0;

  while ((read = getline(&line, &len, file)) != -1) {
    lines = (char **) realloc(lines, sizeof(char *) * (count + 1));
    if (lines == NULL) {
      perror("Memory allocation failed");
      fclose(file);
      free(line);
      return NULL;
    }

    lines[count] = (char *) malloc(read + 1);
    if (lines[count] == NULL) {
      perror("Memory allocation failed");
      fclose(file);
      free(line);
      free(lines);
      return NULL;
    }

    strncpy(lines[count], line, read);
    lines[count][read] = '\0';
    if (read > 0 && lines[count][read - 1] == '\n') {
      lines[count][read - 1] = '\0';
    }
    count++;
  }

  *line_count = count;
  fclose(file);
  free(line);
  return lines;
}

void free_lines(char **lines, int line_count) {
  if (lines != NULL) {
    for (int i = 0; i < line_count; i++) {
      free(lines[i]);
    }
    free(lines);
  }
}