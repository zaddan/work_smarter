import os
import subprocess
import sys

os.system("g++ -w -I/home/local/bulkhead/behzad/usr/local/lib/boost_1_55_0 -L/home/local/bulkhead/behzad/usr/local/lib/boost_1_55_0/stage/lib -lboost_iostreams -lboost_serialization copy_one_obj.cpp -o copy_one_obj")
os.system("g++ -w -I/home/local/bulkhead/behzad/usr/local/lib/boost_1_55_0 -L/home/local/bulkhead/behzad/usr/local/lib/boost_1_55_0/stage/lib -lboost_iostreams -lboost_serialization copy_vec.cpp -o copy_vec")


print "NOTE::remmeber to export the following library for the loader to be able to find the boos lib:"
print "     export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/local/bulkhead/behzad/usr/local/lib/boost_1_55_0/stage/lib"
