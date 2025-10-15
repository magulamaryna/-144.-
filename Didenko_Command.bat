cd E:
md P144
cd E:\P144
md GAMES
cd E:\P144\GAMES
md SGAMES
md UFORUS
cd E:\P144\GAMES\SGAMES
md WOL
md DOO
md SIM
md WIN
md 1f.txt
echo Поставте 10. > 1f.txt
md 2f.txt
echo Будь ласка. > 2f.txt
md 3f.txt
type 1f.txt
del 3f.txt
cd E:\P-144_didenko
dir | more
md E:\P-144_didenko\TEMP
cd TEMP
copy 1f.txt TEMP
copy 2f.txt TEMP
ren 1f.txt file1.txt
ren 2f.txt file2.txt
dir E:\P-144_didenko\TEMP
copy file1.txt + file2.txt Kirill.txt
dir E:\P-144_didenko
date /t
time /t
ver