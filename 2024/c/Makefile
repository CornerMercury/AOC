CC := gcc
CFLAGS := -Wall -Wextra -Werror -Wno-unused-variable -I./lib

SOURCES := $(wildcard solutions/*/*.c)
OBJECTS := $(SOURCES:.c=.o)
LIB_SOURCES := $(wildcard lib/*.c)
LIB_OBJECTS := $(LIB_SOURCES:.c=.o)

.PHONY: all
all:
	@echo "Usage: make <day>, where <day> is the solution day (e.g., make 1)"

# Compile and run the solution for a specific day
%:
	@make c$*
	@make r$*

c%: solutions/%/main.c $(OBJECTS) $(LIB_OBJECTS)
	@echo "Compiling solution for day $*..."
	@$(CC) $(CFLAGS) -o solutions/$*/solution solutions/$*/main.c $(LIB_OBJECTS) || { echo "Compilation failed."; exit 1; }

r%:
	@echo "Running solution for day $*..."
	@cd solutions/$*/ && ./solution | tee output.txt || { echo "Execution failed."; cd ../../; exit 1; }
	@cd ../../

clean:
	@rm -rf solutions/*/solution