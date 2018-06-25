from ftplib import FTP

ftp=FTP()
ftp.connect("10.16.20.14",21)
ftp.login("lucc","lucc@tq123")
print(ftp.getwelcome())
ftp.dir()
ftp.mkd("ftp://10.16.20.14/dcpp_0621_2/DEM_2192/46006713-4947-49d5-8860-6c794461c004")
ftp.dir()
ftp.quit()
