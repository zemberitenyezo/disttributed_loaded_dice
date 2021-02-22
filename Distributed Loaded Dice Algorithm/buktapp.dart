import 'package:crypto/crypto.dart';
import 'package:convert/convert.dart';
import 'dart:convert';

String distributed_loaded_dice(Candidates, Chances, Joker) {
	var text;
	var PreviousHash = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
	var NextHash;
	var Greatest;
	var idx = 0;
	for (var Candidate in Candidates) {
		for (var ChanceCounter = 0; ChanceCounter < Chances[idx]; ChanceCounter++) {
			text = utf8.encode('$Candidate$ChanceCounter$Joker');
			NextHash = sha256.convert(text).bytes;
				for (int j=0; j<32; j++) {
					if (NextHash[j] == PreviousHash[j]) {
						continue;
					}
					if (NextHash[j] > PreviousHash[j]) {
						Greatest = Candidate;
						PreviousHash = NextHash;
					}
					break;
				}
		}
		idx++;
	}
	return Greatest;
}

void main(List<String> arguments) {
	
	//testing histogram with diverse Jokers instead of diverse candidate names
	var offset = 147634;

	var candidates = ['Momentum', 'DK', 'Párbeszéd', 'Jobbik', 'MSZP', 'LMP'];
	var chances = [600,1000,100,900,500,200]; // Závecz 2020. február
	var histogram = {'Momentum':0, 'DK':0, 'Párbeszéd':0, 'Jobbik':0, 'MSZP':0, 'LMP':0};
	for (var joker = offset; joker < offset + 100; joker++) {
		histogram[distributed_loaded_dice(candidates, chances, joker)] += 1;
	}
	print('$histogram');
}
