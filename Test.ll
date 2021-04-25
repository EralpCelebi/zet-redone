; ModuleID = "zet"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i8 @"main"() 
{
.2:
  %"a" = alloca i8
  %".3" = alloca i8
  %".4" = load i8, i8* %".3"
  store i8 %".4", i8* %"a"
  %"b" = alloca i8
  %".6" = load i8, i8* %"a"
  store i8 %".6", i8* %"b"
  %".8" = alloca i8
  %".9" = load i8, i8* %".8"
  store i8 %".9", i8* %"b"
}
