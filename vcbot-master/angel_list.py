import urllib
import urllib.request
import json
import datetime
import math
import bot_utils
import crunchbase
import pdb

access_token = "ea1de9207f7e2f5b546128027f378e888c25e36f099f4c4e"

class Key_Attr_Check:

	def __init__( self, attrs ):
		self.attrs = attrs

	def match( self, startup ):
		m = True
		for attr in self.attrs:
			val = startup.get( attr )
			if val is None or val is False:
				m = False
				break
		return m
			
class Startup_Check:

	def match( self, startup ):
		company_type = startup.get( "company_type" )
		if company_type is None:
			return True

		if len( company_type ) == 0:
			return True

		m = False
		for t in company_type:
			if ( t.get( "name" ) == "startup" ):
				m = True
				break

		return m


al_checks = [ Startup_Check(), Key_Attr_Check( [ "name", "high_concept", "company_url" ] ) ]

def recent_startups( startup_map, url, max=1000 ):

	print( "AngelList.recent_startups => %s" % url ) 
	results = bot_utils.load_json( url )
		
	count = 0
	if results is not None:
		for al_data in results.get( "startups" ):
			if bot_utils.match_all( al_data, al_checks ):
				name = al_data.get( "name" );
				if startup_map.get( name ) is None:
					startup = create( al_data )
					startup_map[ name ] = startup
					crunchbase.find_startup( startup, name )
					print( "Found via AL: " + name )
					count = count + 1
					if count > max:
						break
	return startup_map;

def find_startup( name ):
	url = "https://api.angel.co/1/search?access_token=%s&type=Startup&query=%s" % (access_token, name)
	
	results = bot_utils.load_json( url )
	if results is None or len( results ) == 0:
		return None

	al_id = None if results is None else results[0].get( "id" )

	if al_id is not None:
		 al_data = bot_utils.load_json( "https://api.angel.co/1/startups/%s" % al_id )
		 if al_data is not None:
		 	if bot_utils.match_all( al_data, al_checks ):
		 		startup = create( al_data )
		 		crunchbase.find_startup( startup, name )
		 		return startup

	return None

def create( al_data ):
	startup = {}
	startup[ "al_data" ] = al_data
	startup[ "name" ] = property( al_data, "name" )
	startup[ "short_description" ] = property( al_data, "high_concept" )
	startup[ "description" ] = property( al_data, "product_desc" )
	startup[ "url" ] = property( al_data, "company_url" )
	startup[ "angel_list_url" ] = property( al_data, "angellist_url" )
	startup[ "location" ] = location( al_data )
	startup[ "tags" ] = tags( al_data )
	startup[ "quality" ] = property( al_data, "quality" )

	updated = property( al_data, "updated_at" )
	bot_utils.set_if_empty( startup, "updated",  
		datetime.datetime.strptime( updated, '%Y-%m-%dT%H:%M:%SZ').replace(hour=0, minute=0, second=0, microsecond=0 ) )

	funding( startup )

	return startup
	
def property( startup, prop ):
	al_data = startup.get( "al_data" )
	if al_data is None:
		al_data = startup

	value = None
	if al_data is not None:
		value = al_data.get( prop )
	return value

def location( al_data ):
	locs = property( al_data, "locations" )
	loc = None
	if locs is not None and len( locs ) > 0:
		loc = locs[0].get( "display_name" ).lower().title()
	return loc

def tags( al_data ):
	tags = []
	markets = al_data.get( "markets" )
	if markets is not None:		
		for market in markets:
			tags.append( market.get( "name").lower() )
	return tags

def funding( startup ):
	if startup.get( "last_round" ) is None:
		al_data = startup[ 'al_data' ]
		al_id = property( al_data, 'id' )
		al_funding = bot_utils.load_json( "https://api.angel.co/1/startups/%s/funding?access_token=%s" % (al_id, access_token) )
		if al_funding is not None:
			funding_info = al_funding.get( "funding" )
			total_raised = 0
			last_round = None

			for funding in funding_info:
				amount = property( funding, "amount" )

				if amount is not None:					
					closed = property( funding, "closed_at" )
				
					total_raised = total_raised + amount
					if last_round is None or closed > last_round.get( "closed_at" ):
						last_round = funding

			if last_round is not None:
				bot_utils.set_if_empty( startup, "last_round", last_round.get( "amount" ) )
				bot_utils.set_if_empty( startup, "last_round_type", last_round.get( "round_type" ) )
				bot_utils.set_if_empty( startup, "last_round_url", last_round.get( "source_url" ) )
				bot_utils.set_if_empty( startup, "total_funding", total_raised )

if __name__ == "__main__":
	startups = {}
	recent_startups(startups, "https://api.angel.co/1/startups?access_token=%s&filter=raising&page=1" % access_token, 3)
	print(startups)
