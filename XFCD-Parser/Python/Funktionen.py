# This Python file uses the following encoding: utf-8

#import numpy;
import math;
import os;
import json;

#import Konstanten;

def parseXFCDTrace(TraceJson,filename):
	
	if(TraceJson['XfcdReport']['AppEvent']['AppEventId'] == 'eXaeid_ParkingSearch_StopDriveAndData'):
		
		Trace = {
			'type': 'FeatureCollection',
			'features': [
				{
					'type':'Feature',
					'properties':{},
					'geometry':{
						'type':'LineString',
						'coordinates':[]
					}
				}
			]
		}

		for GPSPoint in TraceJson['XfcdReport']['History']['Pearls']:
			for element in GPSPoint['Datums']:
				if(element['Type'] == 'eDid_Latitude_Wgs84'):
					TempLatitude = int(element['Value'])/1000000;
				elif(element['Type'] == 'eDid_Longitude_Wgs84'):
					TempLongitude = int(element['Value'])/1000000;
				elif(element['Type'] == 'eDid_Time_ms'):
					TempTimeMs = int(element['Value']);
				elif(element['Type'] == 'eDid_DNParkingSearchState'):
					TempParkinSearchState = int(element['Value']);
				elif(element['Type'] == 'eDid_Speed_kmh10'):
					TempSpeed = int(element['Value']);
				elif(element['Type'] == 'eDid_GearStatus'):
					TempGear = int(element['Value']);
				elif(element['Type'] == 'eDid_RoadType'):
					TempRoadType = int(element['Value']);
				elif(element['Type'] == 'eDid_EngineState'):
					TempEngineState = int(element['Value']);
				elif(element['Type'] == 'eDid_Heading_0NorthCw'):
					TempHeading = int(element['Value']);
				elif(element['Type'] == 'eDid_DirectionIndicator'):
					TempIndicator = int(element['Value']);
				else:
					print('Key %s is not included in List'%element['Type']);
			
			Trace['features'][0]['geometry']['coordinates'].append([TempLongitude,TempLatitude]);			

		filename = filename.replace('.json','.geojson');
		with open('../data/parsedData/%s'%filename,'wb') as fp:
			json.dump(Trace, fp);

	else:
		print('Start File does not include Trace Data');



# 	#print(int(HotSpotUnfallListe[0][0][:4]));

# 	(ValidierungsUnfaelle,GrundlagenUnfaelle) = findeValidierungsUnfaelle(HotSpotUnfallListe,params);
# 	#print(ValidierungsUnfaelle);
# 	#print(GrundlagenUnfaelle);
	
# 	HotSpotInfo = {};

# 	HotSpotInfo['HS_ID'] = HS_ID;

# 	EintrittswahrscheinlichkeitUeberValidierungsunfaelle = [];
# 	HotSpotInfo_Temp = [];
# 	for ValidierungsUnfall in ValidierungsUnfaelle:
# 		HotSpotInfo_Temp.append(ValidierungsUnfall[0])
		
# 		Eintrittswahrscheinlichkeit_Temp = analysiereValidierungsUnfall(ValidierungsUnfall,GrundlagenUnfaelle,params)
# 		#print(ValidierungsUnfall);
# 		EintrittswahrscheinlichkeitUeberValidierungsunfaelle.append(Eintrittswahrscheinlichkeit_Temp);

	
# 	HotSpotInfo['Unfaelle_ID'] = HotSpotInfo_Temp;
# 	HotSpotInfo['Unfaelle_Eintrittswahrscheinlichkeit'] = EintrittswahrscheinlichkeitUeberValidierungsunfaelle;

# 	DurchschnittValidierungsunfaelle = numpy.mean(EintrittswahrscheinlichkeitUeberValidierungsunfaelle);
# 	HotSpotInfo['HS_DS_Eintrittswahrscheinlichkeit'] = (DurchschnittValidierungsunfaelle);
# 	print(DurchschnittValidierungsunfaelle);
# 	#print(EintrittswahrscheinlichkeitUeberValidierungsunfaelle);


# 	EintrittswahrscheinlichkeitUeberJahr = [];
# 	Jahresfaktor = findeTendenzUeberJahre(GrundlagenUnfaelle, params);
# 	for i in range(53):
# 		for j in range(7):
# 			for k in range(24):
# 				EintrittswahrscheinlichkeitUeberJahr.append(berechneEintrittswahrscheinlichkeit(i+1,j+1,k,GrundlagenUnfaelle, Jahresfaktor));

# 	HotSpotInfo['Jahr_Eintrittswahrscheinlichkeit'] = EintrittswahrscheinlichkeitUeberJahr;
# 	DurchschnittJahresUnfaelle = numpy.mean(EintrittswahrscheinlichkeitUeberJahr);
# 	HotSpotInfo['Jahr_DS_Eintrittswahrscheinlichkeit'] = DurchschnittJahresUnfaelle;
# 	print(DurchschnittJahresUnfaelle);
# 	#print(EintrittswahrscheinlichkeitUeberJahr);

# 	#print(HotSpotInfo);
# 	return HotSpotInfo;



# def findeValidierungsUnfaelle(HotSpotUnfallListe,params):
# 	ValidierungsUnfaelle = [];
# 	GrundlagenUnfaelle = [];

# 	for entry in HotSpotUnfallListe:
# 		if str(entry[9])[6:10] == params['JahrValidierung']:
# 			ValidierungsUnfaelle.append(entry);
# 		else:
# 			GrundlagenUnfaelle.append(entry);

# 	return (ValidierungsUnfaelle,GrundlagenUnfaelle);

# def analysiereValidierungsUnfall(ValidierungsUnfall,GrundlagenUnfaelle,params):
	
# 	Jahresfaktor = findeTendenzUeberJahre(GrundlagenUnfaelle, params);
	
# 	ValidierungsTageszeit = int(ValidierungsUnfall[11][:2]);
# 	#1 entspricht Sonntag
# 	ValidierungsWochentag = int(ValidierungsUnfall[10]);
# 	ValidierungsKalenderWoche = errechneKalenderWoche(ValidierungsUnfall[9],ValidierungsWochentag);
# 	#ValidierungsMonat = ValidierungsUnfall[9][3:5];
# 	#print(ValidierungsKalenderWoche,ValidierungsWochentag,ValidierungsTageszeit);

# 	Eintrittswahrscheinlichkeit = berechneEintrittswahrscheinlichkeit(ValidierungsKalenderWoche,ValidierungsWochentag,ValidierungsTageszeit,GrundlagenUnfaelle, Jahresfaktor);
# 	#print(Eintrittswahrscheinlichkeit);
# 	#print(len(GrundlagenUnfaelle));

# 	return Eintrittswahrscheinlichkeit;



# def findeTendenzUeberJahre(GrundlagenUnfaelle, params):

# 	UnfaelleUeberJahre = [];
# 	Jahresfaktor = [];
# 	i = 0;
# 	#print(list(reversed(params['JahreGrundlage'])));

# 	for Jahr in list(reversed(params['JahreGrundlage'])):
# 		Jahreszaehler = 0;
# 		for entry in GrundlagenUnfaelle:
# 			if (str(entry[9])[6:10]) == Jahr:
# 				Jahreszaehler += 1;
		
# 		UnfaelleUeberJahre.append(Jahreszaehler);
		
# 		if i == 0:
# 			Jahresfaktor.append(1);
# 			AnzahlUnfaelle = UnfaelleUeberJahre[i];
# 		else:
# 			DurchschnittUnfaelle = AnzahlUnfaelle/i;
# 			if UnfaelleUeberJahre[i] == 0:
# 				Jahresfaktor.append(99);
# 			else:
# 				TempJahresfaktor = float(DurchschnittUnfaelle)/float(UnfaelleUeberJahre[i]);
# 				if (TempJahresfaktor>1.0): TempJahresfaktor = 1.0;
# 				Jahresfaktor.append(TempJahresfaktor);
# 				AnzahlUnfaelle += UnfaelleUeberJahre[i];

# 		i += 1;

# 	#print(UnfaelleUeberJahre);
# 	#print(Jahresfaktor);
	
# 	UnfaelleUeberJahre = list(reversed(UnfaelleUeberJahre));

# 	return list(reversed(Jahresfaktor));


# def berechneEintrittswahrscheinlichkeit(KalenderWoche,Wochentag,Tageszeit,GrundlagenUnfaelle, Jahresfaktor):
	
# 	SummeZeitPunktsFaktor=0;

# 	for entry in GrundlagenUnfaelle:
# 		ZeitPunktsFaktor = berechneZeitPunktsFaktor(KalenderWoche,Wochentag,Tageszeit,entry);
# 		ZeitPunktsFaktor *= Jahresfaktor[int(str(entry[9])[6:10])-2005];
# 		SummeZeitPunktsFaktor += ZeitPunktsFaktor;

# 	Eintrittswahrscheinlichkeit = SummeZeitPunktsFaktor;#/Verkehrsfluss;
# 	return Eintrittswahrscheinlichkeit;

# def berechneZeitPunktsFaktor(KalenderWoche,Wochentag,Tageszeit,entry):
# 	KalenderWoche_Temp = errechneKalenderWoche(entry[9],entry[10]);
# 	#print(KalenderWoche,KalenderWoche_Temp,53);
# 	DeltaKalenderWoche = errechneDelta(KalenderWoche,KalenderWoche_Temp,53);

# 	Wochentag_Temp = int(entry[10]);
# 	DeltaWochentag = errechneDelta(Wochentag,Wochentag_Temp,7);

# 	try:
# 		Tageszeit_Temp = int(entry[11][:2]);
# 	except:
# 		Tageszeit_Temp = 0;
# 		print(entry[0],entry[11]);
# 	DeltaTageszeit = errechneDelta(Tageszeit+1,Tageszeit_Temp+1,24);

# 	#Provisorische Lösung soll über Konstanten und Graphen gelöst werden
# 		#KalenderWocheFaktor = math.exp(-math.pow((float(DeltaKalenderWoche)*6.0/26.5),4)); #1.0 - math.pow(float(DeltaKalenderWoche/26.5),2);
# 		#WochentagFaktor = math.exp(-math.pow((float(DeltaWochentag)*2.0/3.5),2)); #1.0 - math.pow(float(DeltaWochentag/3.5),4);
# 		#TageszeitFaktor = math.exp(-math.pow((float(DeltaTageszeit)*3.0/12),4)); #1.0 - math.pow(float(DeltaTageszeit/12),3);
# 	KalenderWocheFaktor = Konstanten.KalenderWocheFaktor[DeltaKalenderWoche];
# 	WochentagFaktor = Konstanten.WochentagFaktor[DeltaWochentag];
# 	TageszeitFaktor = Konstanten.TageszeitFaktor[DeltaTageszeit];

# 	ZeitPunktsFaktor = KalenderWocheFaktor * WochentagFaktor * TageszeitFaktor;

# 	return ZeitPunktsFaktor;

# def errechneKalenderWoche(Datum,Wochentag):
# 	MonatsTage = [31,28,31,30,31,30,31,31,30,31,30,31];
# 	Tag = int(Datum[:2]);
# 	Monat = int(Datum[3:5]) -1;
# 	KalenderTag = Tag;
# 	for i in range(Monat):
# 		KalenderTag += MonatsTage[i];
# 	#print(KalenderTag);
# 	KalenderWoche = int(math.ceil(float(KalenderTag + (7-Wochentag))/7.0));

# 	return KalenderWoche;

# def errechneDelta(X,Y,END):
# 	Delta_1 = X - Y;
# 	if Delta_1 < 0:
# 		Delta_1 += END;
	
# 	Delta_2 = Y - X;
# 	if Delta_2 < 0:
# 		Delta_2 += END;

# 	if Delta_1 < Delta_2:
# 		Delta = Delta_1;
# 	else:
# 		Delta = Delta_2;

# 	return Delta;

