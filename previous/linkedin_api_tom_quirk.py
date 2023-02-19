
# https://github.com/tomquirk/linkedin-api

from linkedin_api import Linkedin
import datetime

import os
from dotenv import load_dotenv
load_dotenv()

LINKEDIN_EMAIL = str(os.getenv('LINKEDIN_EMAIL'))
LINKEDIN_PASSWORD = str(os.getenv('LINKEDIN_PASSWORD'))

def LinkedIn_retreive_fn(username):

	is_successful = False
	ret = {}
	ret['img_url'] = None
	ret['aboutus'] = None	
	ret['headline'] = None
	ret['geoLocationName'] = None
	ret['experience'] = []
	ret['education'] = []
	ret['certifications'] = []
	ret['projects'] = []
	ret['honors'] = []
	ret['publications'] = []
	ret['skills'] = []
	ret['connectionsCount'] = None
	# ret['name'] = None
	# ret['email'] = None

	# Authenticate using any Linkedin account credentials using https://github.com/tomquirk/linkedin-api
	api = Linkedin(LINKEDIN_EMAIL,LINKEDIN_PASSWORD)

	def remove_unwanted_char(str):
		str = str.encode("ascii", "ignore").decode()  #removing utf-8 characters �
		str = str.replace("\r","").replace("\n","").replace("\t","")   #removing \n\r\t
		return str

	# ----------------------------------1st request----Profile info-------------------------------------------------------
	
	profile = api.get_profile(username)
	if profile != {}:		
		is_successful = True
		try:
			ret['img_url'] = profile['displayPictureUrl'] + profile['img_400_400']
		except:
			pass

		try:
			ret['aboutus'] = remove_unwanted_char(profile['summary'])
		except:
			pass

		try:
			ret['headline'] = remove_unwanted_char(profile['headline'] )
		except:
			pass

		try:
			ret['geoLocationName'] = profile["geoLocationName"]
		except:
			pass

		def beautify_experience(exp):
			d={}
			d['title'] = exp['title']
			d['companyName'] = exp['companyName']
			d['description'] = None
			if 'description' in exp:
				d['description'] = remove_unwanted_char(exp['description'])

			startDate = datetime.datetime(exp['timePeriod']['startDate']['year'],1,1)
			d['period'] = None
			d['current_role'] = None

			if 'endDate' not in exp['timePeriod']:
				period = startDate.strftime("%Y")
				d['period'] = period
				d['current_role'] = True
				return d

			endDate = datetime.datetime(exp['timePeriod']['endDate']['year'],1,1)
			if startDate==endDate:
				period = startDate.strftime("%Y")
			else:	
				period = startDate.strftime("%Y") + ' - ' + endDate.strftime("%Y")
			d['period'] = period
			d['current_role'] = False
			return d

		try:
			ret['experience'] = list(map(beautify_experience,profile["experience"]))
		except:
			pass
			

		def beautify_education(edu):
			d={}
			d['schoolName'] = edu['schoolName']
			d['degreeName'] = None
			d['fieldOfStudy'] = None
			d['grade'] = None

			if 'degreeName' in edu:
				d['degreeName'] = edu['degreeName']
			if 'fieldOfStudy' in edu:
				d['fieldOfStudy'] = edu['fieldOfStudy']
			if 'grade' in edu:
				d['grade'] = edu['grade']
			return d

		try:
			ret['education'] = list(map(beautify_education,profile["education"]))
		except:
			pass

		def beautify_certifications(cert):
			d={}
			d['name'] = cert['name']
			d['authority'] = None
			d['period'] = None
			d['licenseNumber'] = None
			d['logo'] = None
			d['url'] = None

			if 'authority' in cert:  #issue date
				d['authority'] = cert['authority']

			if 'timePeriod' in cert:  #issue date
				startDate = datetime.datetime(cert['timePeriod']['startDate']['year'],1,1)
				period = startDate.strftime("%Y")
				d['period'] = period

			if "licenseNumber" in cert:
				d["licenseNumber"] = cert["licenseNumber"]

			if "company" in cert:
				d['logo'] = cert['company']['logo']['com.linkedin.common.VectorImage']['rootUrl'] + cert['company']['logo']['com.linkedin.common.VectorImage']['artifacts'][0]['fileIdentifyingUrlPathSegment']

			if "url" in cert:
				d['url'] = cert['url']
			return d

		try:
			ret['certifications'] = list(map(beautify_certifications,profile["certifications"]))
		except:
			pass


		def beautify_projects(project):
			d={}
			d['title'] = project['title'].strip()
			d['description'] = None
			d['url'] = None
			d['members'] = None

			if 'description' in project: 
				d['description'] = remove_unwanted_char(project['description'])
			if 'url' in project:
				d['url'] = project['url']
			if len(project['members'])>1 :
				members = []
				for i in range(1,len(project['members'])):
					name = project['members'][i]['member']['firstName']+' '+project['members'][i]['member']['lastName']
					members.append(name)
				d['members'] = members	

			return d

		try:
			ret['projects'] = list(map(beautify_projects,profile["projects"]))
		except:
			pass

		def beautify_honors(honor):
			d={}
			d['title'] = honor['title']
			d['description'] = None
			d['issuer'] = None
			d['issueDate'] =None

			if 'description' in honor:
				d['description'] = remove_unwanted_char(honor['description'])
			if 'issuer' in honor:
				d['issuer'] = honor['issuer']
			if	'issueDate' in honor:
				date = datetime.datetime(honor['issueDate']['year'],1,1)
				d['issueDate'] = date.strftime("%Y")

			return d

		try:
			ret['honors'] = list(map(beautify_honors,profile["honors"]))
		except:
			pass

		def beautify_publications(publication):
			d={}
			d['name'] = publication['name']
			d['description'] = None
			d['publisher'] = None
			d['issueDate'] = None
			d['url'] = None

			if 'description' in publication:
				d['description'] = remove_unwanted_char(publication['description'])
			if 'publisher' in publication:
				d['publisher'] = publication['publisher']
			if 'date' in publication:
				date = datetime.datetime(publication['date']['year'],publication['date']['month'],1)
				d['issueDate'] = date.strftime("%b %Y")
			if 'url' in publication:
				d['url'] = publication['url']
			return d

		try:
			ret['publications'] = list(map(beautify_publications,profile["publications"]))
		except:
			pass

	else:
		print(f"Linkedin Retreival => Problem with 1st request retreivel of {username} => mostly username is incorrect")
		return None

	# ----------------------------------2nd request----Skills----------------------------------------------------------

	skills = api.get_profile_skills(username)
	if profile!={}:
		is_successful = True
		try:
			if len(skills)!=0:
				skills = [ skill['name'].split('(')[0].strip() for skill in skills]
				ret['skills'] = skills
		except:
			pass
	else:
		print(f"Linkedin Retreival => Problem with 2nd request retreivel of {username} => mostly username is incorrect")

	# ----------------------------------3rd request----no. of connections ----------------------------------------------------------

	network = api.get_profile_connections(username)
	if network!={}:
		is_successful = True
		try:
			ret['connectionsCount'] = network['connectionsCount']
		except:
			pass
	else:
		print(f"Linkedin Retreival => Problem with 3rd request retreivel of {username} status code !=200")

	#---------------------------------------------------------returning-----------------------------------------

	if not is_successful:
		print(f"Linkedin Retreival => Problem with all request retreivals of {username} status code !=200")
		return None

	return ret

# temp = LinkedIn_retreive_fn('selvaramg')
# temp = LinkedIn_retreive_fn('kasinath-j-2881a6200')
# temp = LinkedIn_retreive_fn('cosc-not-1bb93a253')
# print(temp)
