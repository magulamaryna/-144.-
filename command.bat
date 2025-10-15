D:
cd P-144\Mykhalchych
md BP
md CRT
md DRS
cd BP
md BGI
md DVA
md UNITS
cd UNITS
echo привіт зпфк! > f1.txt
echo привіт світ! > f2.txt
echo привіт група! > f3.txt
type f1.txt
del f3.txt
cd ..\..
md TEMP
copy D:\P-144\Mykhalchych\BP\UNITS\*.txt TEMP\
cd TEMP
ren f1.txt file1.txt
ren f2.txt file2.txt
dir
copy file1.txt + file2.txt dmytro.txt
dir
echo %DATE%
echo %TIME%
ver