FILE(REMOVE_RECURSE
  "CMakeFiles/myapp.dir/my_src/test1.cpp.o"
  "CMakeFiles/myapp.dir/my_src/test2.cpp.o"
  "myapp.pdb"
  "myapp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang CXX)
  INCLUDE(CMakeFiles/myapp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
