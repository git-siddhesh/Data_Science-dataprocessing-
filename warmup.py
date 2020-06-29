
#Case 1: Create a Single tier Architect enviroment for php application on AWS Insatnce

+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +

#Server Configure Details:

#AWS Instance Type: t2.micro

#AMI or Server OS: CentOS 7 (x86_64) - with Updates HVM

Disk Layout: 

#	-- Disk1: 8GB for / ( for the root volume )

#	-- Attach 1 more encrypted Volume ( Disk 2 ) with disk accidental termination policy at least 4GB Size of volume when you lauched your instance 

#	-- Attach one Elastic IP to your instance 

#	-- Now wait for aws running status and logged into server using your keys

#+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +  


###############################################################################################
								Prerequisite

#1. Check all things like server version, disk size of root volume & extra disk, RAM, CPU

#2. Update server packages

#3. Format disk and mount

	-- Make disk2 volume LVM type for future app data size grow requirement 
	
	-- Format with xfs file system 
	
	-- Disk2: 4GB for Home ( For web data, mount this on /home2 with "no execution binary" security flag)
	
	-- Note that, both volume will be mounted automaticlly whenever you reboot your server

4. Disable Selinux 

5. Set timezone of Server to IST

6. Install basic utility like netstat, wget, vim, git

7. Reboot your server to verify and test all things.

8. Congiure your motd file on server so i can get more infomatin dynamically about server whenever we logged in and you can find out format of motd through  https://adhocnw.org/motd.txt

###############################################################################################

Now start server setup, configuration, test and deploy 

1. Packages:

	-- > Install Apache 2.4.x server with SSL and proxy module support
	
	-- > Install PHP v7.x with essential php modules like php-mysql, php-devel, php-mbstring etc which is required by Application. In our case we need php module as below:

		-- Packages Name: rh-php70-php rh-php70-php-common rh-php70-php-cli rh-php70-php-devel rh-php70-php-gd rh-php70-php-json rh-php70-php-mbstring rh-php70-php-mysqlnd rh-php70-php-opcache rh-php70-php-zip sclo-php70-php-mcrypt rh-php70-php-xml rh-php70-php-intl

	**** By Default Centos 7.x provide PHP 5.4.x upport so use Software Collection repository for official php 7.x support in CentOS 7
	

Note: Make your services automatically restart whenever server reboot in future [ Try to reboot server to check services ]


2. User Setup:

	-- > Create one user blu with passwordless login and bluboy user home directory should be /home2
	-- > Create public_html folder under user blu home directory 
	-- > Use this public_html folder for web files and that will be your document root in Apache  

3. VirtualHost Configuration:

	-- > Create two virtualhost configuration under /etc/httpd/conf.d as blu-php.conf for better management rather than /etc/httpd/httpd.conf as follows:

		-- ServerName will be blu.adhocnw.com in your apache virtual hosting

		-- Also setup seprate error_log file 

		--  you can test your application to write domain dns inforamtion in /etc/hosts file

4. Now you server is ready to serve php applications. Setup phpinfo page and your file name will phpinfo.php that will be access by http://bluboy.adhocnw.com url 

5. Test your application using /etc/hosts and  point bluboy.adhocnw.com to your Instance IP

6. Update your server Packages to fix packages vunlerabilty and reboot the server and recheck all things 

7. Most Important:

Create a document for your process and submit to linux@linux.com and ashutoshh@linux.com

Docs for Reference:

1. https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/system_administrators_guide/index#s1-sysinfo-filesystems
2. https://wiki.centos.org/AdditionalResources/Repositories/SCL
-------------------------------------


#1. Check all things like server version, disk size of root volume & extra disk, RAM, CPU

cat /etc/os-release
free -m

#2. Update server packages

yum update -y

#3. Format disk and mount


#4. Disable Selinux
------------------------------


    1 - Catchall for general errors
    2 - Misuse of shell builtins (according to Bash documentation)
    126 - Command invoked cannot execute
    127 - “command not found”
    128 - Invalid argument to exit
    128+n - Fatal error signal “n”
    130 - Script terminated by Control-C
    255\* - Exit status out of range









###############################################################
#                 Authorized access only!                     # 
# Disconnect IMMEDIATELY if you are not an authorized user!!! #
#         All actions Will be monitored and recorded          #
###############################################################
+++++++++++++++++++++++++++++++ SERVER INFO ++++++++++++++++++++++++++++++++
	CPU: Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz
	Memory: 1024M
	Swap: 1024M
	Disk: 10G
	Distro: CentOS Linux release 7.6.1810 (Core) with 3.10.0-957.1.3.el7.x86_64
	CPU Load: 0.00, 0.01, 0.05 
	Free Memory: 207M
	Free Swap: 128M
	Free Disk: 8G
	Public Address: 13.234.101.240 
	Private Address: 172.31.25.253
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

