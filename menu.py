import os
import getpass
os.system("tput setaf 14")
print ("\t\t\t Welcome to Menu!!!")
os.system("tput setaf 12")
print("\t\t\t-----------------------")

passwd = getpass.getpass("Enter password")
if passwd != "divya":
	print("password incorrect")
	exit()

print ("Entering local device")
while True:
  os.system("tput setaf 2")
  print("""
  \n
  System Operations:
  ------------------
  Press 1: Date
  Press 2: Calender
  Press 3: System configuration settings
  Press 4: View system profile
  Press 5: To install a package
  Press 6: To see a package info 
  Press 7: Check service status
  Press 8: Veiw installed software
  Press 9: Veiw a software info
  Press 10: Add new user
  Press 11: Delete a user
  Press 12: Configure web
  
  Docker:
  -------
  Press 13: Configure Docker
  Press 14: List Docker images stored locally
  Press 15: Pull an image from registry
  Press 16: Push an image to registry
  Press 17: Delete an image from local image store
  Press 18: Build an image from dockerfile
  Press 19: Run a container from docker image
  Press 20: List the networks
  Press 21: List the running containers
  Press 22: Delete all containers

  Hadoop:
  -------
  Press 23: To list all the hadoop files/directories
  Press 24: To display the content of a hdfs file
  Press 25: Copy file in hdfs from local file system
  Press 26: Copy file in local file system from hdfs

  AWS Cloud:
  -----------
  Press 27: Create a key-pair  
  Press 28: Create security-group
  Press 29: Launch EC2 instance
  Press 30: Create and attach a volume to EC2 instance
  Press 31: Exit
  """)
  os.system("tput setaf 11")
  ch = input ("Enter your choice:")
  print(ch)
  os.system("tput setaf 15")
  if int(ch) == 1:
    os.system("date")
  elif int(ch) == 2:
    os.system("cal")
  elif int(ch) == 3:
    os.system("gnome-control-center")
  elif int(ch) == 4:
    os.system("lscpu")
  elif int(ch) == 5:
    name = input("enter package name:")
    os.system("yum install {} -y".format(name))
  elif int(ch) == 6:
    name = input ("enter package name:")
    os.system("yum info {}".format(name))
  elif int(ch) == 7:
    num = input ("enter the service name:")
    os.system("systemctl status {}".format(num))
  elif int(ch) == 8:
    os.system("rpm -qa")
  elif int(ch) == 9:
    name = input ("enter software name:")
    os.system("yum info {}".format(name))
  elif int(ch) == 10:
    new_uswer = input ("enter name of the new user:")
    os.system("sudo useradd {}".format(new_user))
    os.system("id -u {}".format(new_user))
  elif int(ch) == 11:
    name = input ("enter name of the user:")
    os.system("sudo userdel {}".format(name))
  elif int(ch) == 12:
    os.system("yum install httpd -y")
    os.system("systemctl start httpd")
  elif int(ch) == 13:
    os.system("yum install docker-ce -y")
    os.system("systemctl start docker")
  elif int(ch) == 14:
    os.system("docker image ls")
  elif int(ch) == 15:
    name = input ("enter image name with version:")
    os.system("docker pull {}".format(name))
  elif int(ch) == 16:
    name = input ("enter image name: ")
    os.system("docker push {}".format(name))
  elif int(ch) == 17:
    name = input ("enter image name:")
    os.system("docker image rm {}".format(name))
  elif int(ch) == 18:
    name = input ("enter image name:")
    os.system("docker build -t {}".format(name))
  elif int(ch) == 19:
    img_name = input ("enter name of the image:")
    port = input ("enter port:")
    con_name = input ("enter container name:")
    os.system("docker container run --name {} -p {} {}".format(con_name, port, img_name))
  elif int(ch) == 20:
    os.system("docker network ls")
  elif int(ch) == 21:
    os.system("docker container ls")
  elif int(ch) == 22:
    os.system("docker container rm -f $(docker ps -aq)")
  elif int(ch) == 23:
    os.system("hdfs dfs -ls /")
  elif int(ch) == 24:
    name = input ("enter file name:")
    os.system("hdfs dfs -cat /hadoop/{}".format(name))
  elif int(ch) == 25:
    name = input ("enter file along with path:")
    os.system("hdfs dfs -put {} /hadoop".format(name))
  elif int(ch) == 26:
    name = input ("enter file along with path:")
    os.system("hdfs dfs -get {} /hadoop".format(name))
  elif int(ch) == 26:
    name = input ("enter file along with path:")
    os.system("hdfs dfs -get {} /hadoop".format(name))
  elif int(ch) == 27:
    name = input ("enter key-pair name:")
    os.system("aws ec2 create-key-pair --key-name {}".format(name))
  elif int(ch) == 28:
    name = input ("enter security groupe name:")
    des=input("Write description:")
    os.system("aws ec2 create-security-group --group-name {} --description {}".format(name,des))
  elif int(ch) == 29:
    name = input ("enter image id:")
    sg=input("Security group id:")
    subnet= input("Subnet id:")
    key= input("key name:")
    os.system("aws ec2 run-instances --image-id {} --instance-type t2.micro --security-group-ids {} --subnet-id {} --key-name {}".format(name,sg,subnet,key))
  elif int(ch) == 30:
    az = input ("enter availability zone:")
    vtype=input("Volume type:")
    insid=input("enter instance id to which you want to attach")
    vid= input("Enter volume id which is to be attached")	
    os.system("aws ec2 create-volume --availability-zone {} --size 1 --volume-type {}".format(az, vtype))
    os.system("aws ec2 attach-volume --device xvdh --instance-id {} --volume-id {}".format(insid, vid))
  elif int(ch) == 31:
    print("Exiting...")
    exit()
  else:
    print("Not supported")

  input ("Press enter to continue")
  os.system("clear")
