FILE(REMOVE_RECURSE
  "CMakeFiles/\$FAB.dir/my_src/test1.cpp.o"
  "CMakeFiles/\$FAB.dir/my_src/test2.cpp.o"
  "\$FAB.pdb"
  "\$FAB"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang CXX)
  INCLUDE(CMakeFiles/$FAB.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
