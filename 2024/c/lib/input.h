#ifndef FILE_READER_H
#define FILE_READER_H

char* read_file(const char *filename);
char** read_lines(const char *filename, int *line_count);
void free_lines(char **lines, int line_count);

#endif