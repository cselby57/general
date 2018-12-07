#pragma once

# include <random>
# include <algorithm>
# include <iostream> 
# include <string>
# include <chrono>

/*	Cameron Selby Spring 2018
	Structures used by bracket march madness bracket generator
	Probably not an efficient setup but it works fine*/
using namespace std;

struct team {
	// a team has a starting seed and a region
	// names are not important as this bracket maker
	// does not use any actual data, just psuedo random numbers
	double seed = 0.0;
	string regionFrom = "a region";
};
struct matchup {
	// a matchup involves two teams and a winner
	team Team1;
	team Team2;
	team winningTeam;
};


struct region {
	// a region is comprised of 4 rounds of different number of matchup arrays
	matchup firstRound[8];
	matchup secondRound[4];
	matchup sweet16[2];
	matchup elite8;
};

struct bracket {
	// a bracket has 4 regions as well as a 2 final four games and a championship
	region east;
	region midwest;
	region south;
	region west;
	matchup final4EastMidwest;
	matchup final4WestSouth;
	matchup championship;
};

class B {
	// class B for bracket
	// contains a bracket that starts empty except for intial seeds
	// has a few methods for filling out the bracket with winning seeds
public:
	B() {
	};
	bracket theBracket;
	

	team getWinner(matchup &theGame);		// decide a game
	team getRegion(region &theRegion);		// decide all games in a region
	void initRegion(region &theRegion, string regionName);  // initialize seeding
	team getChampion(bracket &theBracket);  // decide the whole bracket
};