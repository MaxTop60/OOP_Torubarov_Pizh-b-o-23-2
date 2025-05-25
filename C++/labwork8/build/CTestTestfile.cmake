# CMake generated Testfile for 
# Source directory: D:/University/Dev/C++/labwork8
# Build directory: D:/University/Dev/C++/labwork8/build
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
if(CTEST_CONFIGURATION_TYPE MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
  add_test(bst_test "D:/University/Dev/C++/labwork8/build/Debug/bst_test.exe")
  set_tests_properties(bst_test PROPERTIES  _BACKTRACE_TRIPLES "D:/University/Dev/C++/labwork8/CMakeLists.txt;18;add_test;D:/University/Dev/C++/labwork8/CMakeLists.txt;0;")
elseif(CTEST_CONFIGURATION_TYPE MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
  add_test(bst_test "D:/University/Dev/C++/labwork8/build/Release/bst_test.exe")
  set_tests_properties(bst_test PROPERTIES  _BACKTRACE_TRIPLES "D:/University/Dev/C++/labwork8/CMakeLists.txt;18;add_test;D:/University/Dev/C++/labwork8/CMakeLists.txt;0;")
elseif(CTEST_CONFIGURATION_TYPE MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
  add_test(bst_test "D:/University/Dev/C++/labwork8/build/MinSizeRel/bst_test.exe")
  set_tests_properties(bst_test PROPERTIES  _BACKTRACE_TRIPLES "D:/University/Dev/C++/labwork8/CMakeLists.txt;18;add_test;D:/University/Dev/C++/labwork8/CMakeLists.txt;0;")
elseif(CTEST_CONFIGURATION_TYPE MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
  add_test(bst_test "D:/University/Dev/C++/labwork8/build/RelWithDebInfo/bst_test.exe")
  set_tests_properties(bst_test PROPERTIES  _BACKTRACE_TRIPLES "D:/University/Dev/C++/labwork8/CMakeLists.txt;18;add_test;D:/University/Dev/C++/labwork8/CMakeLists.txt;0;")
else()
  add_test(bst_test NOT_AVAILABLE)
endif()
subdirs("libs/googletest")
