/* March Madness Bracket Maker
   Cameron Selby spring 2018*/

# include "bracketmaker.h"
using namespace std;





team B::getWinner(matchup &theGame) {
	// initialize a new uniform pseudo random distribution from 0 to 1
	unsigned randomSeed = chrono::system_clock::now().time_since_epoch().count();
	default_random_engine generator(randomSeed);
	uniform_real_distribution<double> distribution(0.0, 1.0);
	
	// now generate a weight for each team based on distribution
	double weight1 = distribution(generator);
	if (theGame.Team1.seed == 1) {
		weight1 -= .05; // needed to tune down 1 seeds a little bit
	}
	double weight2 = distribution(generator);
	if (theGame.Team2.seed == 1) {
		weight2 -= .05;
	}
	// determine the  outcome based on weights and seeds, obviously biased to low seeds
	double result = (weight1 / theGame.Team1.seed) - (weight2 / theGame.Team2.seed);
	if (result == 0) {
		// sometimes get result of 0 (tie) so just sim the game again
		getWinner(theGame);
	}
	// if we got a decision update the matchup with the winner
	else if (result > 0) {
		theGame.winningTeam = theGame.Team1;
	}
	else {
		theGame.winningTeam = theGame.Team2;
	}
	return theGame.winningTeam; // return the matchup
};

team B::getRegion(region &theRegion) {
	// solve an enitre region of the bracket
	team winner1; // initialize the winners of the previous round
	team winner2;

	/* for each set of two games in a round get the winners 
	   and store them as the competing seeds in the next rounds matchups*/
	// first round
	for (int i = 0; i < 4; i++) {
		winner1 = getWinner(theRegion.firstRound[i * 2]);
		winner2 = getWinner(theRegion.firstRound[(i * 2) + 1]);
		theRegion.secondRound[i].Team1 = winner1;
		theRegion.secondRound[i].Team2 = winner2;
	}
	// second round
	for (int i = 0; i < 2; i++) {
		winner1 = getWinner(theRegion.secondRound[i * 2]);
		winner2 = getWinner(theRegion.secondRound[(i * 2) + 1]);
		theRegion.sweet16[i].Team1 = winner1;
		theRegion.sweet16[i].Team2 = winner2;
	}
	// sweet 16
	winner1 = getWinner(theRegion.sweet16[0]);
	winner2 = getWinner(theRegion.sweet16[1]);
	theRegion.elite8.Team1 = winner1;
	theRegion.elite8.Team2 = winner2;
	// elite 8 
	team teamTeam = getWinner(theRegion.elite8);
	return teamTeam; // return the region winner
};

void B::initRegion(region &theRegion, string regionName) {
	// just add the seed numbers to the firstround in each region
	// didnt feel like making a loop today, and this will never change
	//   (unless the number of teams in play changes but then i mean
	//    ok this will be garbage but who cares)
	theRegion.firstRound[0].Team1.seed = 1;
	theRegion.firstRound[0].Team2.seed = 16;
	theRegion.firstRound[1].Team1.seed = 8;
	theRegion.firstRound[1].Team2.seed = 9;
	theRegion.firstRound[2].Team1.seed = 5;
	theRegion.firstRound[2].Team2.seed = 12;
	theRegion.firstRound[3].Team1.seed = 4;
	theRegion.firstRound[3].Team2.seed = 13;
	theRegion.firstRound[4].Team1.seed = 6;
	theRegion.firstRound[4].Team2.seed = 11;
	theRegion.firstRound[5].Team1.seed = 3;
	theRegion.firstRound[5].Team2.seed = 14;
	theRegion.firstRound[6].Team1.seed = 7;
	theRegion.firstRound[6].Team2.seed = 10;
	theRegion.firstRound[7].Team1.seed = 2;
	theRegion.firstRound[7].Team2.seed = 15;
	for (int i = 0; i < 8; i++) {
		theRegion.firstRound[i].Team1.regionFrom = regionName;
	}
};

team B::getChampion(bracket &theBracket) {
	// solve the entire bracket

	// initialize seeds in each region
	initRegion(theBracket.east, "East");
	initRegion(theBracket.west,"West");
	initRegion(theBracket.midwest, "Midwest");
	initRegion(theBracket.south, "South");

	// deternine final 4
	team eastWinner = getRegion(theBracket.east); 
	team midwestWinner = getRegion(theBracket.midwest); 
	team westWinner = getRegion(theBracket.west); 
	team southWinner = getRegion(theBracket.south); 

	// do the final four sort of manually
	theBracket.final4EastMidwest.Team1 = eastWinner;
	theBracket.final4EastMidwest.Team2 = midwestWinner;
	theBracket.final4WestSouth.Team1 = westWinner;
	theBracket.final4WestSouth.Team2 = southWinner;
	cout << "final 4: " << eastWinner.seed << " " << midwestWinner.seed << " " << westWinner.seed << " " << southWinner.seed << "\n";
	team eastMidwestWinner = getWinner(theBracket.final4EastMidwest);
	team westSouthWinner = getWinner(theBracket.final4WestSouth);
	theBracket.championship.Team1 = eastMidwestWinner;
	theBracket.championship.Team2 = westSouthWinner;
	theBracket.championship.winningTeam = getWinner(theBracket.championship);
	return theBracket.championship.winningTeam; // return the full bracke tstructure for display
};


// wqas used in testing ignore
/*void main() {
	bracket testBracket;
	for (int i = 0; i < 25; i++) {
		team winner = getChampion(testBracket);
		cout << "winner: " << winner.regionFrom << " " << winner.seed << "\n";
	}
	getchar();
};*/


