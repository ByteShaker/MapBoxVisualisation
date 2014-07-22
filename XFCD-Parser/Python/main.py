# This Python file uses the following encoding: utf-8

import math;
#import numpy;
import copy;
import os;
import json;
import zipfile;

#import Konstanten;
import Funktionen;

def initialisiereXFCDParser(params):
	"""Importiere alle Konstanten und Module und starte die Berechnung"""

	for year in os.listdir(params['RelevanteHotSpotsURL']):
		pfad_year = os.path.join(params['RelevanteHotSpotsURL'],year);

		for month in os.listdir(pfad_year):
			pfad_year_month = os.path.join(pfad_year,month);

			for day in os.listdir(pfad_year_month):
				pfad_year_month_day = os.path.join(pfad_year_month,day);

				for hour in os.listdir(pfad_year_month_day):
					pfad_year_month_day_hour = os.path.join(pfad_year_month_day,hour);

					for element in os.listdir(pfad_year_month_day_hour):
						pfad_file = os.path.join(pfad_year_month_day_hour,element);
						try:
							fh = open(pfad_file,'rb');
							z = zipfile.ZipFile(fh);
							filename = element;
							filename = filename.replace('.zip','.json');
							x = z.read(filename);
							y = json.loads(x);
							#print y;

						except:
							print('\nFile %s does not exist'%pfad_file);

						Funktionen.parseXFCDTrace(y,filename);


	# UnfallanzahlAnalyse = [];

	# Konstanten.ZeitpunktsfaktorenBestimmen();

	# for entry in range(len(RelevanteHotSpots)):

	# 	if ((int(RelevanteHotSpots[entry][2]) > 19) and (int(RelevanteHotSpots[entry][2]) < 500)):
	# 		try: 
	# 			HotSpotUnfallListe = numpy.genfromtxt(params['HotSpotUnfallListeURL']%(int(RelevanteHotSpots[entry][0])), delimiter=',', dtype=None);

	# 		except:
	# 			print('\n\tFile %s does not exist'%(params['HotSpotUnfallListeURL']%(int(RelevanteHotSpots[entry][0]))));

	# 		HS_Info = Funktionen.analysiereHotSpot(HotSpotUnfallListe, params, int(RelevanteHotSpots[entry][0]));

	# 		UnfallanzahlAnalyse.append([HS_Info['HS_ID'], int(RelevanteHotSpots[entry][2]), HS_Info['HS_DS_Eintrittswahrscheinlichkeit'], HS_Info['Jahr_DS_Eintrittswahrscheinlichkeit']])

	# 		numpy.savetxt('../Daten/UnfallanzahlAnalyse.csv', numpy.asarray(UnfallanzahlAnalyse), fmt="%i,%i,%.15f,%.15f");

	# 		#with open('../Daten/HotSpotAnalyse_29/Analyse_%i.json'%(int(RelevanteHotSpots[entry][0])),'wb') as fp:
	# 		#	json.dump(HS_Info,fp);
	# 		#numpy.savetxt('../Daten/HotSpotAnalyse/Analyse_%i.csv'%(int(RelevanteHotSpots[entry][0])), HS_Info);

	return 'Berechnung abgeschlossen';



if __name__ == "__main__":
	params = {	'RelevanteHotSpotsURL' : '../data/',\
				'JahreGrundlage' : ['2013','2014']}; 
	print(initialisiereXFCDParser(params));
