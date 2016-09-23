CC = g++
CFLAGS = -O3 -g -w -std=c++11 
#-I/home/local/bulkhead/behzad/usr/local/lib/boost_1_55_0 -L/home/local/bulkhead/behzad/usr/local/lib/boost_1_55_0/stage/lib -lboost_iostreams -lboost_serialization 
#all: main.exe
##main: *.cpp
	##$(CC) $(CFLAGS) main.cpp test.cpp -o test
#CPP_FILES := $(wildcard src/*.cpp)
#OBJ_FILES := $(addprefix obj/,$(notdir $(CPP_FILES:.cpp=.o)))

#main.exe: $(OBJ_FILES)
	#g++ $(CFLAGS) -o $@ $^

#obj/%.o: src/%.cpp
	#g++ $(CFLAGS) -c -o $@ $<



#CPP_FILES := $(wildcard src/*.cpp)
#OBJ_FILES := $(addprefix obj/,$(notdir $(CPP_FILES:.cpp=.o)))
#LD_FLAGS := ...
#CC_FLAGS := ...

CPP_FILES := $(wildcard src/*.cpp)
OBJ_FILES := $(addprefix obj/,$(notdir $(CPP_FILES:.cpp=.o)))
LD_FLAGS := ...
CC_FLAGS := ...

main.exe: $(OBJ_FILES)
	g++ -o $@ $^

obj/%.o: src/%.cpp
	g++ -c -o $@ $<
