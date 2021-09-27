import sqlite3
	con = sqlite3.connect('hospital.db')
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS HOSPITAL ")
	hosp = """CREATE TABLE HOSPITAL(
	         Hospital_ID INTEGER PRIMARY KEY, 
	         Hospital_Name CHAR(20) NOT NULL,
	         Bed_Count INTEGER NOT NULL)"""
	cur.execute(hosp)
	con.execute("INSERT INTO HOSPITAL (Hospital_ID,Hospital_Name,Bed_Count) "
	                 "VALUES (1, 'Mayo Clinic',200)")
	con.execute("INSERT INTO HOSPITAL (Hospital_ID,Hospital_Name,Bed_Count) "
	                 "VALUES (2,'Cleveland Clinic',400 )")
	con.execute("INSERT INTO HOSPITAL (Hospital_ID,Hospital_Name,Bed_Count) "
	                 "VALUES (3,'Johns Hopkins', 1000)")
	con.execute("INSERT INTO HOSPITAL (Hospital_ID,Hospital_Name,Bed_Count) "
	                 "VALUES (4,'UCLA Medical Center', 1500)")
	con.commit()
	cur = con.execute("SELECT * from HOSPITAL")
	print(cur.fetchall())
	
	con1 = sqlite3.connect('hospital.db')
	cur1 = con1.cursor()
	cur1.execute("DROP TABLE IF EXISTS DOCTOR ")
	doct ="""CREATE TABLE DOCTOR(
	           Doctor_ID INTEGER PRIMARY KEY,
	           Doctor_Name CHAR(15) NOT NULL,
	           Hospital_ID INTEGER NOT NULL,
	           Joining_Date DATE FORMAT 'yyyy-mm-dd',
	           Speciality CHAR(15) NOT NULL,
	           Salary INTEGER NOT NULL,
	           Experience CHAR(5))"""
	cur1.execute(doct)
	con1.execute("INSERT INTO DOCTOR (Doctor_ID,Doctor_Name,Hospital_ID,Joining_Date,Speciality,Salary,Experience) "
	                 "VALUES (101, 'David',1,2005-02-10,'Pediatric',40000,'NULL')")
	con1.execute("INSERT INTO DOCTOR (Doctor_ID,Doctor_Name,Hospital_ID,Joining_Date,Speciality,Salary,Experience) "
	                 "VALUES (102,'Michael',1,2018-07-23,'Oncologist',20000,'NULL')")
	con1.execute("INSERT INTO DOCTOR (Doctor_ID,Doctor_Name,Hospital_ID,Joining_Date,Speciality,Salary,Experience) "
	                 "VALUES (103,'Susan',2,2016-05-19, 'Garnacologist',25000,'NULL')")
	con1.execute("INSERT INTO DOCTOR (Doctor_ID,Doctor_Name,Hospital_ID,Joining_Date,Speciality,Salary,Experience) "
	                 "VALUES (104,'Robert',2,2017-12-28, 'Pediatric',28000,'NULL')")
	con1.execute("INSERT INTO DOCTOR (Doctor_ID,Doctor_Name,Hospital_ID,Joining_Date,Speciality,Salary,Experience) "
	                 "VALUES (105,'Linda',3,2004-06-04, 'Garnacologist',42000,'NULL')")
	con1.execute("INSERT INTO DOCTOR (Doctor_ID,Doctor_Name,Hospital_ID,Joining_Date,Speciality,Salary,Experience) "
	                 "VALUES (106,'William',3,2012-09-11, 'Dermatalogist',30000,'NULL')")
	con1.execute("INSERT INTO DOCTOR (Doctor_ID,Doctor_Name,Hospital_ID,Joining_Date,Speciality,Salary,Experience) "
	                 "VALUES (107,'Richard',4,2014-08-21, 'Garnacologist',32000,'NULL')")
	con1.execute("INSERT INTO DOCTOR (Doctor_ID,Doctor_Name,Hospital_ID,Joining_Date,Speciality,Salary,Experience) "
	                 "VALUES (108,'Karen',4,2011-10-17, 'Radiologist',30000,'NULL')")
	con1.commit()
	cur1 = con1.execute("SELECT * from DOCTOR")
	print(cur1.fetchall())
	
	sp = input("Enter Speciality : ")
	sa = (input("Enter Salary : "))
	cur2 = con1.execute("SELECT * from DOCTOR where Speciality= '"+ sp + "' and Salary>= '"+ sa + "'")
	print(cur2.fetchall())
	
	hospital_id = 0
	hospital_id_list = []
	while True:
	    try:
	        hospital_id = int(input("Enter Hospital ID : "))
	    except ValueError:
	        print("Invalid Value!!!")
	        continue
	    cur1.execute("SELECT DISTINCT(Hospital_ID) FROM Doctor")
	    temp_list = cur1.fetchall()
	    for item in temp_list:
	        hospital_id_list.append(int(item[0]))
	    if hospital_id not in hospital_id_list:
	        print("Hospital Does not Exist!!!!")
	    else:
	        break
	query2 = "SELECT Doctor_Name,Hospital_Name FROM Hospital,Doctor WHERE Hospital.Hospital_ID=Doctor.Hospital_ID and Hospital.Hospital_ID=?"
	cur1.execute(query2, (hospital_id,))
	print(
	    "List of Doctors along with their Hospital Name\n")
	for item in cur1.fetchall():
	    print("{}\t{}".format(item[0], item[1]))
	
	con.close()
	con1.close()
