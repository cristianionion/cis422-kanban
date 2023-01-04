# cis422-kanban
CIS422 Group Project at University of Oregon

Authors: Brad Bailey, Tiana Cook, Brandon Dodd, Cristian Ion, Wanrong Qi


# How to Run:

1. Establish a connection with MySQL\
  -I use [XAMPP Control Panel](https://www.apachefriends.org/download.html)  \
          -To use XAMPP: run XAMPP, start MySQL \
   -To see DBs in browser, also start Apache, and then click "Admin" for MySQL
2. Make sure that your MySQL password and the one in line 26 of database.py match (or else connection will fail)
3. In terminal, once in the cis422-kanban folder, run "python3 .\main.py"


# How to Use:
**Note that login functionality is not implemented, on login screen either select Student or Instructor then login**
## Instructor: 
1. Select instructor on login screen, (entering name is optional)
2. You can create 2 types of Kanban boards
   - Default boards consist of 3 categories: Not Started, In Progress, and Completed
   - Custom boards allow you to create your own categories (buckets)
     - custom board will show the right buckets AFTER closing and restarting program
4. As an instructor, you can create cards with descriptions that go onto kanban boards, move those cards, and can also delete boards

## Student:
1. Select Student on login screen, (entering name is optional)
2. Students can only select boards that an instructor created, and move the cards that an instructor created
