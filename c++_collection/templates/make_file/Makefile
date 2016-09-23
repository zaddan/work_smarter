#--------- the most simple way (i think i should almost always use this----------
#--------- this doesn't cover the case were we want obj and src folder to be seperate and
#---------- we want to put the make file in the root directory (for this sceneario refer to OPTION2)
CC = g++
CFLAGS = -O3 -g -w -std=c++11 
main.exe: *.cpp
	$(CC) $(CCFLAGS) -o $@ $^

#--------------- OPTION 1----------------------#
# ---- note: the following requires a dependency defined for every object file (hard 
CC = g++
CFLAGS = -O3 -g -w -std=c++11 
all: main

main: src_file_1.o src_file_2.o 
	$(CC) $(CFLAGS) $^ -o main

src_file_1.o: src_file1.cpp
	$(CC) $(CFLAGS) -c src_file1.cpp -g

src_file_2.o: src_file2.cpp
	$(CC) $(CFLAGS) -c src_file2.cpp -g


#--------------- OPTION 2----------------------#
# ---- note: smart way of compiling all files 
#if you have src and obj folder do the following:
CPP_FILES := $(wildcard src/*.cpp)
OBJ_FILES := $(addprefix obj/,$(notdir $(CPP_FILES:.cpp=.o)))
CCFLAGS = -O3 -g -w -std=c++11 
main.exe: $(OBJ_FILES)
	g++ $(CCFLAGS) -o $@ $^
obj/%.o: src/%.cpp
	g++ $(CCFLAGS) -c -o $@ $<

#else:
CPP_FILES := $(wildcard *.cpp)
OBJ_FILES := $(addprefix ./,$(notdir $(CPP_FILES:.cpp=.o)))
CCFLAGS = -O3 -g -w -std=c++11 
main.exe: $(OBJ_FILES)
	g++ $(CCFLAGS) -o $@ $^
obj/%.o: src/%.cpp
	g++ $(CCFLAGS) -c -o $@ $<

clean:
	rm -f *.o main


