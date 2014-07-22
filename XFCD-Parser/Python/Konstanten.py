# This Python file uses the following encoding: utf-8

import math;

#Zeitpunktsfaktoren 
KalenderWocheFaktor = [];
WochentagFaktor = [];
TageszeitFaktor = [];


def ZeitpunktsfaktorenBestimmen():
	for KalenderWoche in range(28):
		KalenderWocheFaktor.append(math.exp(-math.pow((float(KalenderWoche)*6.0/26.5),4))); #1.0 - math.pow(float(DeltaKalenderWoche/26.5),2);

	for Wochentag in range(5):
		WochentagFaktor.append(math.exp(-math.pow((float(Wochentag)*2.0/3.5),2))); #1.0 - math.pow(float(DeltaWochentag/3.5),4);

	for Tageszeit in range(13):
		TageszeitFaktor.append(math.exp(-math.pow((float(Tageszeit)*3.0/12),4))); #1.0 - math.pow(float(DeltaTageszeit/12),3);

	return None;