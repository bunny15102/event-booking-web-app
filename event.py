#import the required libraries
import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade
import sys
import MySQLdb
#connect to mysql database
conn = MySQLdb.connect(host="localhost",user="root",passwd="home",db="management")
#create a cursor
cursor = conn.cursor()



class ManagementGUI:	
	def __init__(self):
		#Set the Glade file
		self.gladefile = "eventgui.glade"
		self.wTree = gtk.glade.XML(self.gladefile)

		#Get the widgets in the widget tree
		self.window = self.wTree.get_widget('MainWindow')
		self.eventWindow = self.wTree.get_widget('EventWindow')
		self.organizerWindow = self.wTree.get_widget('OrganizerWindow')
		self.volunteerWindow = self.wTree.get_widget('VolunteerWindow')
		self.visitorWindow = self.wTree.get_widget('VisitorWindow')

		self.eventname = self.wTree.get_widget('eventname')
		self.eventdate = self.wTree.get_widget('eventdate')
		self.eventduration = self.wTree.get_widget('eventduration')
		self.eventplace = self.wTree.get_widget('eventplace')
		self.eventweb = self.wTree.get_widget('eventwebsite')
		
		self.eventUpdatedlg = self.wTree.get_widget('eveUpdlg')
		self.eventUpdateEntry = self.wTree.get_widget('eveUpdateEntry')

		self.eventSearchdlg = self.wTree.get_widget('eveSearchDlg')
		self.eventSearchEntry = self.wTree.get_widget('eveSearchEntry')
		
		self.eventSearchReportdlg = self.wTree.get_widget('eveSearchRepDlg')
		self.eventSearchReport = self.wTree.get_widget('eveSearchReport')
		
		self.eventDeletedlg = self.wTree.get_widget('eveDelDlg')
		self.eventDeleteEntry = self.wTree.get_widget('eveDelEntry')

		self.eventReportdlg = self.wTree.get_widget('evedlgReport')
		self.eventtxtReport = self.wTree.get_widget('evetxtReport')
		

		self.orgevename = self.wTree.get_widget('orgevename')
		self.orgname = self.wTree.get_widget('orgname')
		self.orgaddress = self.wTree.get_widget('orgaddress')
		self.orgcontact = self.wTree.get_widget('orgcontact')
		self.orgemail = self.wTree.get_widget('orgemail')
		self.orgrole = self.wTree.get_widget('orgrole')
		
		self.orgUpdatedlg = self.wTree.get_widget('orgUpdlg')
		self.orgUpdateEntry = self.wTree.get_widget('orgUpdateEntry')

		self.orgSearchdlg = self.wTree.get_widget('orgSearchDlg')
		self.orgSearchEntry = self.wTree.get_widget('orgSearchEntry')

		self.orgSearchReportdlg = self.wTree.get_widget('orgSearchRepDlg')
		self.orgSearchReport = self.wTree.get_widget('orgSearchReport')
		
		self.orgDeletedlg = self.wTree.get_widget('orgDelDlg')
		self.orgDeleteEntry = self.wTree.get_widget('orgDelEntry')

		self.orgReportdlg = self.wTree.get_widget('orgdlgReport')
		self.orgtxtReport = self.wTree.get_widget('orgtxtReport')

		self.volevename = self.wTree.get_widget('volevename')
		self.volname = self.wTree.get_widget('volname')
		self.voladdress = self.wTree.get_widget('voladdress')
		self.volcontact = self.wTree.get_widget('volcontact')
		self.volemail = self.wTree.get_widget('volemail')
		self.volrole = self.wTree.get_widget('volrole')

		self.volUpdatedlg = self.wTree.get_widget('volUpdlg')
		self.volUpdateEntry = self.wTree.get_widget('volUpdateEntry')

		self.volSearchdlg = self.wTree.get_widget('volSearchDlg')
		self.volSearchEntry = self.wTree.get_widget('volSearchEntry')

		self.volSearchReportdlg = self.wTree.get_widget('volSearchRepDlg')
		self.volSearchReport = self.wTree.get_widget('volSearchReport')
		
		self.volDeletedlg = self.wTree.get_widget('volDelDlg')
		self.volDeleteEntry = self.wTree.get_widget('volDelEntry')

		self.volReportdlg = self.wTree.get_widget('voldlgReport')
		self.voltxtReport = self.wTree.get_widget('voltxtReport')

				
		self.visevename = self.wTree.get_widget('visevename')
		self.visname = self.wTree.get_widget('visname')
		self.visaddress = self.wTree.get_widget('visaddress')
		self.viscontact = self.wTree.get_widget('viscontact')
		self.visemail = self.wTree.get_widget('visemail')
		self.visrole = self.wTree.get_widget('visrole')

		self.visUpdatedlg = self.wTree.get_widget('visUpDlg')
		self.visUpdateEntry = self.wTree.get_widget('visUpdEntry')

		self.visSearchdlg = self.wTree.get_widget('visSearchDlg')
		self.visSearchEntry = self.wTree.get_widget('visSearchEntry')

		self.visSearchReportdlg = self.wTree.get_widget('visSearchRepDlg')
		self.visSearchReport = self.wTree.get_widget('visSearchReport')
		
		self.visDeletedlg = self.wTree.get_widget('visDelDlg')
		self.visDeleteEntry = self.wTree.get_widget('visDelEntry')

		self.visReportdlg = self.wTree.get_widget('visdlgReport')
		self.vistxtReport = self.wTree.get_widget('vistxtReport')

 		#Create callback dictionary and autoconnect it
		dic = { 'on_MainWindow_destroy' : self.quit,
			'on_event_clicked' : self.eventdetails,
			'on_organizer_clicked': self.organizerdetails,
			'on_volunteer_clicked' : self.volunteerdetails,
			'on_visitor_clicked' : self.visitordetails,
			'on_exit_clicked' :  self.quit,
			'on_eveadd_clicked' : self.eventAdd,
			'on_eveupdateDlg_clicked' : self.eventUpdlg,
			'on_eveupdate_clicked' : self.eventUpdate,
			'on_evesearch_clicked' : self.eventSearch,
			'on_evedelete_clicked' : self.eventDelete,
			'on_evereport_clicked' : self.eventReport,
			'on_eveexit_clicked' : self.eventexit,
			'on_orgadd_clicked' : self.orgAdd,
			'on_orgUpdlg_clicked' : self.orgUpdlg,
			'on_orgupdate_clicked' : self.orgUpdate,
			'on_orgsearch_clicked' : self.orgSearch,
			'on_orgdelete_clicked' : self.orgDelete,
			'on_orgreport_clicked' : self.orgReport,
			'on_orgexit_clicked' : self.orgexit,
			'on_voladd_clicked' : self.volAdd,
			'on_volUpDlg_clicked' : self.volUpdlg,
			'on_volupdate_clicked' : self.volUpdate,
			'on_volsearch_clicked' : self.volSearch,
			'on_voldelete_clicked' : self.volDelete,
			'on_volreport_clicked' : self.volReport,
			'on_volexit_clicked' : self.volexit,
			'on_visadd_clicked' : self.visAdd,
			'on_visUpDlg_clicked' : self.visUpDlg,
			'on_visupdate_clicked' : self.visUpdate,
			'on_vissearch_clicked' : self.visSearch,
			'on_visdelete_clicked' : self.visDelete,
			'on_visreport_clicked' : self.visReport,
			'on_visexit_clicked' : self.visexit
		      }

		self.wTree.signal_autoconnect(dic)
		self.window.show()

	# ========================= Callbacks ===========================  
	def eventdetails(self,widget):
		self.eventWindow.show()	

	def eventAdd(self,widget):
		eventname = self.eventname.get_text()
		eventdate = self.eventdate.get_text()
		eventduration = self.eventduration.get_text()
		eventplace =  self.eventplace.get_text()
		eventweb = self.eventweb.get_text()
		cursor.execute("""
				insert into event (EventName,Date,Duration,Place,Website)
				values (%s,%s,%s,%s,%s)""",(eventname,eventdate,eventduration,eventplace,eventweb))
		self.eventname.set_text("")
		self.eventdate.set_text("")
		self.eventduration.set_text("")
		self.eventplace.set_text("")
		self.eventweb.set_text("")
	
	def eventUpdlg(self,widget):
		res = self.eventUpdatedlg.run()
		if res == gtk.RESPONSE_OK:
			self.updateEveEntry = self.eventUpdateEntry.get_text()
		self.eventUpdatedlg.hide()

	def eventUpdate(self, widget):	
		updateEveEntry = self.updateEveEntry
		eventname = self.eventname.get_text()
		eventdate = self.eventdate.get_text()
		eventduration = self.eventduration.get_text()
		eventplace =  self.eventplace.get_text()
		eventweb = self.eventweb.get_text()	
		cursor.execute("""
			update event set EventName = %s,Date = %s,Duration = %s,Place = %s,Website = %s
			where EventName = %s""",(eventname,eventdate,eventduration,eventplace,eventweb,updateEveEntry))
		self.eventname.set_text("")
		self.eventdate.set_text("")
		self.eventduration.set_text("")
		self.eventplace.set_text("")
		self.eventweb.set_text("")

	def eventSearch(self,widget):
		res = self.eventSearchdlg.run()
		if res == gtk.RESPONSE_OK:
			e = ()
			f = open('eventreport.txt','w')		
			eventname = self.eventSearchEntry.get_text()
			cursor.execute("select * from event where EventName = %s",eventname)
			rows = cursor.fetchall()
			for record in rows:
				e = record[0],"-->",str(record[1]),"-->",str(record[2]),"-->",record[3],"-->",record[4]
				f.write(" ".join(e))
				f.write("\n")
			f = open("eventreport.txt","r")
			if f:
				string = f.read() 
				f.close() 
				self.eventSearchReport.get_buffer().set_text(string)
				res1 = self.eventSearchReportdlg.run()
				if res1 == gtk.RESPONSE_CLOSE:
					self.eventSearchReportdlg.hide()
		self.eventSearchEntry.set_text("")
		self.eventSearchdlg.hide()


	def eventDelete(self,widget):
		res = self.eventDeletedlg.run()	
		if res == gtk.RESPONSE_OK:
			delEveEntry = self.eventDeleteEntry.get_text()
			cursor.execute("""
					delete from event
					where EventName = %s""",delEveEntry)
			self.eventDeleteEntry.set_text("")
		self.eventDeletedlg.hide()	

	def eventReport(self,widget):
		e = ()
		f = open('eventreport.txt','w')
		cursor.execute("select * from event")
		result = cursor.fetchall()
		for record in result:
			e = record[0],"-->",str(record[1]),"-->",str(record[2]),"-->",record[3],"-->",record[4]
			f.write(" ".join(e))
			f.write("\n")
		f = open("eventreport.txt","r")
		if f:
			string = f.read() 
			f.close() 			
			self.eventtxtReport.get_buffer().set_text(string)
			self.eventReportdlg.run()
		self.eventReportdlg.hide()
			
		
	def eventexit(self,widget):
		self.eventWindow.hide()
	
	def organizerdetails(self,widget):
		self.organizerWindow.show()	
	
	def orgAdd(self,widget):
		eventname = self.orgevename.get_text()
		orgnme = self.orgname.get_text()
		addr = self.orgaddress.get_text()
		cno = self.orgcontact.get_text()
		email = self.orgemail.get_text()
		role = self.orgrole.get_text()
		cursor.execute("""
				insert into organizer (EventName,OrganizerName,Address,ContactNo,EmailAddress,Role)
				values (%s,%s,%s,%s,%s,%s)""",(eventname,orgnme,addr,cno,email,role))
		self.orgevename.set_text("")
		self.orgname.set_text("")
		self.orgaddress.set_text("")
		self.orgcontact.set_text("")
		self.orgemail.set_text("")
		self.orgrole.set_text("")
	
	def orgUpdlg(self,widget):
		res = self.orgUpdatedlg.run()
		if res == gtk.RESPONSE_OK:
			self.updateOrgEntry = self.orgUpdateEntry.get_text()
		self.orgUpdatedlg.hide()	

	def orgUpdate(self,widget):
		updateOrgEntry = self.updateOrgEntry
		eventname = self.orgevename.get_text()
		orgnme = self.orgname.get_text()
		addr = self.orgaddress.get_text()
		cno = self.orgcontact.get_text()
		email = self.orgemail.get_text()
		role = self.orgrole.get_text()
		cursor.execute("""
				update organizer set EventName = %s,OrganizerName = %s,Address = %s,ContactNo = %s,EmailAddress = %s, Role = %s
				where OrganizerName = %s""",(eventname,orgnme,addr,cno,email,role,updateOrgEntry))
		self.orgevename.set_text("")
		self.orgname.set_text("")
		self.orgaddress.set_text("")
		self.orgcontact.set_text("")
		self.orgemail.set_text("")
		self.orgrole.set_text("")

	def orgSearch(self,widget):
		res = self.orgSearchdlg.run()
		if res == gtk.RESPONSE_OK:
			o = ()
			f = open('orgreport.txt','w')			
			orgname = self.orgSearchEntry.get_text()
			cursor.execute("select * from organizer where OrganizerName = %s",orgname)
			result = cursor.fetchall()
			for record in result:
				o = record[0],"-->",record[1],"-->",record[2],"-->",str(record[3]),"-->",record[4],"-->",record[5]
				f.write(" ".join(o))
				f.write("\n")
			f = open("orgreport.txt","r")
			if f:
				string = f.read() 
				f.close() 
				self.orgSearchReport.get_buffer().set_text(string)
				res1 = self.orgSearchReportdlg.run()
				if res1 == gtk.RESPONSE_CLOSE:
					self.orgSearchReportdlg.hide()
		self.orgSearchEntry.set_text("")
		self.orgSearchdlg.hide()

	def orgDelete(self,widget):
		res = self.orgDeletedlg.run()	
		if res == gtk.RESPONSE_OK:
			delOrgEntry = self.orgDeleteEntry.get_text()
			cursor.execute("""
					delete from organizer
					where OrganizerName = %s""",delOrgEntry)
			self.orgDeleteEntry.set_text("")
		self.orgDeletedlg.hide()

	def orgReport(self,widget):
		o = ()
		f = open('orgreport.txt','w')
		cursor.execute("select * from organizer")
		result = cursor.fetchall()
		for record in result:
			o = record[0],"-->",record[1],"-->",record[2],"-->",str(record[3]),"-->",record[4],"-->",record[5]
			f.write(" ".join(o))
			f.write("\n")
		f = open("orgreport.txt","r")
		if f:
			string = f.read() 
			f.close() 
			self.orgtxtReport.get_buffer().set_text(string)
			self.orgReportdlg.run()
		self.orgReportdlg.hide()			

	
	def orgexit(self,widget):
		self.organizerWindow.hide()

	def volunteerdetails(self,widget):
		self.volunteerWindow.show()	

	def volAdd(self,widget):
		eventname = self.volevename.get_text()
		volnme = self.volname.get_text()
		addr = self.voladdress.get_text()
		cno = self.volcontact.get_text()
		email = self.volemail.get_text()
		role = self.volrole.get_text()
		cursor.execute("""
				insert into volunteer (EventName,VoulnteerName,Address,ContactNo,EmailAddress,Role)
				values (%s,%s,%s,%s,%s,%s)""",(eventname,volnme,addr,cno,email,role))
		self.volevename.set_text("")
		self.volname.set_text("")
		self.voladdress.set_text("")
		self.volcontact.set_text("")
		self.volemail.set_text("")
		self.volrole.set_text("")

	def volUpdlg(self,widget):
		res = self.volUpdatedlg.run()
		if res == gtk.RESPONSE_OK:
			self.updateVolEntry = self.volUpdateEntry.get_text()
		self.volUpdatedlg.hide()

	def volUpdate(self,widget):
		updateVolEntry = self.updateVolEntry
		eventname = self.volevename.get_text()
		volnme = self.volname.get_text()
		addr = self.voladdress.get_text()
		cno = self.volcontact.get_text()
		email = self.volemail.get_text()
		role = self.volrole.get_text()	
		cursor.execute("""
				update volunteer set EventName = %s,VoulnteerName = %s,Address = %s,ContactNo = %s,EmailAddress = %s, Role = %s
				where VoulnteerName = %s""",(eventname,volnme,addr,cno,email,role,updateVolEntry))
		
		self.volevename.set_text("")
		self.volname.set_text("")
		self.voladdress.set_text("")
		self.volcontact.set_text("")
		self.volemail.set_text("")
		self.volrole.set_text("")

	def volSearch(self,widget):
		res = self.volSearchdlg.run()
		if res == gtk.RESPONSE_OK:
			vol = ()
			f = open('volreport.txt','w')
			volname = self.volSearchEntry.get_text()
			cursor.execute("select * from volunteer where VoulnteerName = %s",volname)
			result = cursor.fetchall()
			for record in result:
				vol = record[0],"-->",record[1],"-->",record[2],"-->",str(record[3]),"-->",record[4],"-->",record[5]
				f.write(" ".join(vol))
				f.write("\n")
			f = open("volreport.txt","r")
			if f:
				string = f.read() 
				f.close() 
				self.volSearchReport.get_buffer().set_text(string)
				res1 = self.volSearchReportdlg.run()
				if res1 == gtk.RESPONSE_CLOSE:
					self.volSearchReportdlg.hide()
		self.volSearchEntry.set_text("")
		self.volSearchdlg.hide()

	def volDelete(self,widget):
		res = self.volDeletedlg.run()	
		if res == gtk.RESPONSE_OK:
			delVolEntry = self.volDeleteEntry.get_text()
			cursor.execute("""
					delete from volunteer
					where VoulnteerName = %s""",delVolEntry)
			self.volDeleteEntry.set_text("")
		self.volDeletedlg.hide()		

	def volReport(self,widget):
		vol = ()
		f = open('volreport.txt','w')
		cursor.execute("select * from volunteer")
		result = cursor.fetchall()
		for record in result:
			vol = record[0],"-->",record[1],"-->",record[2],"-->",str(record[3]),"-->",record[4],"-->",record[5]
			f.write(" ".join(vol))
			f.write("\n")
		f = open("volreport.txt","r")
		if f:
			string = f.read() 
			f.close() 
			self.voltxtReport.get_buffer().set_text(string)
			self.volReportdlg.run()
		self.volReportdlg.hide()			


	def volexit(self,widget):
		self.volunteerWindow.hide()
	
	def visitordetails(self,widget):
		self.visitorWindow.show()
	
	def visAdd(self,widget):
		eventname = self.visevename.get_text()
		visnme = self.visname.get_text()
		addr = self.visaddress.get_text()
		cno = self.viscontact.get_text()
		email = self.visemail.get_text()
		role = self.visrole.get_text()
		cursor.execute("""
				   insert into visitor (EventName,VisitorName,Address,ContactNo,EmailAddress,Role)
				   values (%s,%s,%s,%s,%s,%s)""",(eventname,visnme,addr,cno,email,role))
		self.visevename.set_text("")
		self.visname.set_text("")
		self.visaddress.set_text("")
		self.viscontact.set_text("")
		self.visemail.set_text("")
		self.visrole.set_text("")

	def visUpDlg(self,widget):
		res = self.visUpdatedlg.run()
		if res == gtk.RESPONSE_OK:
			self.updateVisEntry = self.visUpdateEntry.get_text()
		self.visUpdatedlg.hide()

	def visUpdate(self,widget):
		updateVisEntry = self.updateVisEntry
		eventname = self.visevename.get_text()
		visnme = self.visname.get_text()
		addr = self.visaddress.get_text()
		cno = self.viscontact.get_text()
		email = self.visemail.get_text()
		role = self.visrole.get_text()
		cursor.execute("""
				update visitor set EventName = %s,VisitorName = %s,Address = %s,ContactNo = %s,EmailAddress = %s, Role = %s
				where VisitorName = %s""",(eventname,visnme,addr,cno,email,role,updateVisEntry))
		
		self.visevename.set_text("")
		self.visname.set_text("")
		self.visaddress.set_text("")
		self.viscontact.set_text("")
		self.visemail.set_text("")
		self.visrole.set_text("")

	def visSearch(self,widget):
		res = self.visSearchdlg.run()
		if res == gtk.RESPONSE_OK:
			vis = ()
			f = open('visreport.txt','w')
			visname = self.visSearchEntry.get_text()
			cursor.execute("select * from visitor where VisitorName = %s",visname)
			result = cursor.fetchall()
			for record in result:
				vis = record[0],"-->",record[1],"-->",record[2],"-->",str(record[3]),"-->",record[4],"-->",record[5]
				f.write(" ".join(vis))
				f.write("\n")
			f = open("visreport.txt","r")
			if f:
				string = f.read() 
				f.close() 
				self.visSearchReport.get_buffer().set_text(string)
				res1 = self.visSearchReportdlg.run()
				if res1 == gtk.RESPONSE_CLOSE:
					self.visSearchReportdlg.hide()	
		self.visSearchEntry.set_text("")		
		self.visSearchdlg.hide()

	
	def visDelete(self,widget):
		res = self.visDeletedlg.run()	
		if res == gtk.RESPONSE_OK:
			print 'The record is present'
			delVisEntry = self.visDeleteEntry.get_text()
			cursor.execute("""
					delete from visitor
					where VisitorName = %s""",delVisEntry)
			self.visDeleteEntry.set_text("")
		else:
			print 'The record is not present'
		self.visDeletedlg.hide()	

	def visReport(self,widget):
		vis = ()
		f = open('visreport.txt','w')		
		cursor.execute("select * from visitor")
		result = cursor.fetchall()
		for record in result:
			vis = record[0],"-->",record[1],"-->",record[2],"-->",str(record[3]),"-->",record[4],"-->",record[5]
			f.write(" ".join(vis))
			f.write("\n")
		f = open("visreport.txt","r")
		if f:
			string = f.read() 
			f.close() 
			self.vistxtReport.get_buffer().set_text(string)
			self.visReportdlg.run()
		self.visReportdlg.hide()			
	

	def visexit(self,widget):
		self.visitorWindow.hide()
	
	def quit(self,widget):
		sys.exit()

if __name__ == "__main__":	
	m = ManagementGUI()
	gtk.main()	
