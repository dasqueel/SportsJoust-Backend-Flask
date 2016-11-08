#userTeam, opTeam = createSmallMatchup(userRankings, opRankings)
#{'qb':opContestDoc['qbr'],'rb':opContestDoc['rbr'],'wr':opContestDoc['wrr'],'te':opContestDoc['ter'],'defst':opContestDoc['defstr']}



qb1 = [
    {
        "gameId" : "400791630",
        "team" : "Pittsburgh",
        "opp" : "SF",
        "name" : "Ben Roethlisberger",
        "abbr" : "B. Roethlisberger"
    },
    {
        "gameId" : "400791672",
        "team" : "Atlanta",
        "opp" : "@NYG",
        "name" : "Matt Ryan",
        "abbr" : "M. Ryan"
    },
    {
        "gameId" : "400791705",
        "team" : "Philadelphia",
        "opp" : "DAL",
        "name" : "Sam Bradford",
        "abbr" : "S. Bradford"
    },
    {
        "gameId" : "400791666",
        "team" : "Cincinnati",
        "opp" : "SD",
        "name" : "Andy Dalton",
        "abbr" : "A. Dalton"
    },
    {
        "gameId" : "400791711",
        "team" : "Indianapolis",
        "opp" : "NYJ",
        "name" : "Andrew Luck",
        "abbr" : "A. Luck"
    },
    {
        "gameId" : "400791708",
        "team" : "Green Bay",
        "opp" : "SEA",
        "name" : "Aaron Rodgers",
        "abbr" : "A. Rodgers"
    },
    {
        "gameId" : "400791634",
        "team" : "New Orleans",
        "opp" : "TB",
        "name" : "Drew Brees",
        "abbr" : "D. Brees"
    },
    {
        "gameId" : "400791672",
        "team" : "New York Giants",
        "opp" : "ATL",
        "name" : "Eli Manning",
        "abbr" : "E. Manning"
    },
    {
        "gameId" : "400791666",
        "team" : "San Diego",
        "opp" : "@CIN",
        "name" : "Phillip Rivers",
        "abbr" : "P. Rivers"
    },
    {
        "gameId" : "400791624",
        "team" : "Denver",
        "opp" : "@KC",
        "name" : "Peyton Manning",
        "abbr" : "P. Manning"
    },
    {
        "gameId" : "400791708",
        "team" : "Seattle",
        "opp" : "@GB",
        "name" : "Russell Wilson",
        "abbr" : "R. Wilson"
    },
    {
        "gameId" : "400791638",
        "team" : "Detroit",
        "opp" : "@MIN",
        "name" : "Matthew Stafford",
        "abbr" : "M. Stafford"
    },
    {
        "gameId" : "400791664",
        "team" : "New England",
        "opp" : "@BUF",
        "name" : "Tom Brady",
        "abbr" : "T. Brady"
    },
    {
        "gameId" : "400791628",
        "team" : "Carolina",
        "opp" : "HOU",
        "name" : "Cam Newton",
        "abbr" : "C. Newton"
    },
    {
        "gameId" : "400791705",
        "team" : "Dallas",
        "opp" : "@PHI",
        "name" : "Tony Romo",
        "abbr" : "T. Romo"
    },
    {
        "gameId" : "400791669",
        "team" : "Cleveland",
        "opp" : "TEN",
        "name" : "Johnny Manziel",
        "abbr" : "J. Manziel"
    },
    {
        "gameId" : "400791661",
        "team" : "Chicago",
        "opp" : "ARI",
        "name" : "Jay Cutler",
        "abbr" : "J. Cutler"
    },
    {
        "gameId" : "400791675",
        "team" : "St. Louis",
        "opp" : "@WSH",
        "name" : "Nick Foles",
        "abbr" : "N. Foles"
    },
    {
        "gameId" : "400791638",
        "team" : "Minnesota",
        "opp" : "DET",
        "name" : "Teddy Bridgewater",
        "abbr" : "T. Bridgewater"
    },
    {
        "gameId" : "400791680",
        "team" : "Miami",
        "opp" : "@JAC",
        "name" : "Ryan Tannehill",
        "abbr" : "R. Tannehill"
    },
    {
        "gameId" : "400791661",
        "team" : "Arizona",
        "opp" : "@CHI",
        "name" : "Carson Palmer",
        "abbr" : "C. Palmer"
    },
    {
        "gameId" : "400791702",
        "team" : "Oakland",
        "opp" : "BAL",
        "name" : "Derek Carr",
        "abbr" : "D. Carr"
    },
    {
        "gameId" : "400791680",
        "team" : "Jacksonville",
        "opp" : "MIA",
        "name" : "Blake Bortles",
        "abbr" : "B. Bortles"
    },
    {
        "gameId" : "400791669",
        "team" : "Tennessee",
        "opp" : "@CLE",
        "name" : "Marcus Mariota",
        "abbr" : "M. Mariota"
    },
    {
        "gameId" : "400791711",
        "team" : "New York Jets",
        "opp" : "@IND",
        "name" : "Ryan Fitzpatrick",
        "abbr" : "R. Fitzpatrick"
    },
    {
        "gameId" : "400791634",
        "team" : "Tampa Bay",
        "opp" : "@NO",
        "name" : "Jameis Winston",
        "abbr" : "J. Winston"
    }
]
rb1 = [
    {
        "gameId" : "400791705",
        "team" : "Philadelphia",
        "opp" : "DAL",
        "name" : "DeMarco Murray",
        "abbr" : "D. Murray"
    },
    {
        "gameId" : "400791666",
        "team" : "Cincinnati",
        "opp" : "SD",
        "name" : "Jeremy Hill",
        "abbr" : "J. Hill"
    },
    {
        "gameId" : "400791638",
        "team" : "Minnesota",
        "opp" : "DET",
        "name" : "Adrian Peterson",
        "abbr" : "A. Peterson"
    },
    {
        "gameId" : "400791630",
        "team" : "San Francisco",
        "opp" : "@PIT",
        "name" : "Carlos Hyde",
        "abbr" : "C. Hyde"
    },
    {
        "gameId" : "400791711",
        "team" : "New York Jets",
        "opp" : "@IND",
        "name" : "Chris Ivory",
        "abbr" : "C. Ivory"
    },
    {
        "gameId" : "400791664",
        "team" : "Buffalo",
        "opp" : "NE",
        "name" : "LeSean McCoy",
        "abbr" : "L. McCoy"
    },
    {
        "gameId" : "400791661",
        "team" : "Chicago",
        "opp" : "ARI",
        "name" : "Matt Forte",
        "abbr" : "M. Forte"
    },
    {
        "gameId" : "400791624",
        "team" : "Kansas City",
        "opp" : "DEN",
        "name" : "Jamaal Charles",
        "abbr" : "J. Charles"
    },
    {
        "gameId" : "400791702",
        "team" : "Baltimore",
        "opp" : "@OAK",
        "name" : "Justin Forsett",
        "abbr" : "J. Forsett"
    },
    {
        "gameId" : "400791680",
        "team" : "Miami",
        "opp" : "@JAC",
        "name" : "Lamar Miller",
        "abbr" : "L. Miller"
    },
    {
        "gameId" : "400791708",
        "team" : "Seattle",
        "opp" : "@GB",
        "name" : "Marshawn Lynch",
        "abbr" : "M. Lynch"
    },
    {
        "gameId" : "400791634",
        "team" : "New Orleans",
        "opp" : "TB",
        "name" : "Mark Ingram",
        "abbr" : "M. Ingram"
    },
    {
        "gameId" : "400791708",
        "team" : "Green Bay",
        "opp" : "SEA",
        "name" : "Eddie Lacy",
        "abbr" : "E. Lacy"
    },
    {
        "gameId" : "400791624",
        "team" : "Denver",
        "opp" : "@KC",
        "name" : "C.J. Anderson",
        "abbr" : "C. Anderson"
    },
    {
        "gameId" : "400791638",
        "team" : "Detroit",
        "opp" : "@MIN",
        "name" : "Joique Bell",
        "abbr" : "J. Bell"
    },
    {
        "gameId" : "400791705",
        "team" : "Dallas",
        "opp" : "@PHI",
        "name" : "Joseph Randle",
        "abbr" : "J. Randle"
    },
    {
        "gameId" : "400791711",
        "team" : "Indianapolis",
        "opp" : "NYJ",
        "name" : "Frank Gore",
        "abbr" : "F. Gore"
    },
    {
        "gameId" : "400791661",
        "team" : "Arizona",
        "opp" : "@CHI",
        "name" : "Andre Ellington",
        "abbr" : "A. Ellington"
    },
    {
        "gameId" : "400791675",
        "team" : "Washington",
        "opp" : "STL",
        "name" : "Alfred Morris",
        "abbr" : "A. Morris"
    },
    {
        "gameId" : "400791702",
        "team" : "Oakland",
        "opp" : "BAL",
        "name" : "Latavius Murray",
        "abbr" : "L. Murray"
    },
    {
        "gameId" : "400791628",
        "team" : "Carolina",
        "opp" : "HOU",
        "name" : "Jonathan Stewart",
        "abbr" : "J. Stewart"
    },
    {
        "gameId" : "400791666",
        "team" : "San Diego",
        "opp" : "@CIN",
        "name" : "Melvin Gordon",
        "abbr" : "M. Gordon"
    },
    {
        "gameId" : "400791680",
        "team" : "Jacksonville",
        "opp" : "MIA",
        "name" : "T.J. Yeldon",
        "abbr" : "T. Yeldon"
    },
    {
        "gameId" : "400791628",
        "team" : "Houston",
        "opp" : "@OAK",
        "name" : "Alred Blue",
        "abbr" : "A. Blue"
    },
    {
        "gameId" : "400791669",
        "team" : "Cleveland",
        "opp" : "TEN",
        "name" : "Isaiah Crowell",
        "abbr" : "I. Crowell"
    },
    {
        "gameId" : "400791672",
        "team" : "New York Giants",
        "opp" : "ATL",
        "name" : "Rashad Jennings",
        "abbr" : "R. Jennings"
    },
    {
        "gameId" : "400791666",
        "team" : "Cincinnati",
        "opp" : "SD",
        "name" : "Giovani Bernard",
        "abbr" : "G. Bernard"
    },
    {
        "gameId" : "400791669",
        "team" : "Tennessee",
        "opp" : "@CLE",
        "name" : "Bishop Sankey",
        "abbr" : "B. Sankey"
    }
]
wr1 = [
    {
        "gameId" : "400791630",
        "team" : "Pittsburgh",
        "opp" : "SF",
        "name" : "Antonio Brown",
        "abbr" : "A. Brown"
    },
    {
        "gameId" : "400791672",
        "team" : "Atlanta",
        "opp" : "@NYG",
        "name" : "Julio Jones",
        "abbr" : "J. Jones"
    },
    {
        "gameId" : "400791672",
        "team" : "New York Giants",
        "opp" : "ATL",
        "name" : "Odell Beckham",
        "abbr" : "O. Beckham Jr."
    },
    {
        "gameId" : "400791634",
        "team" : "New Orleans",
        "opp" : "TB",
        "name" : "Brandin Cooks",
        "abbr" : "B. Cooks"
    },
    {
        "gameId" : "400791705",
        "team" : "Philadelphia",
        "opp" : "DAL",
        "name" : "Jordan Matthews",
        "abbr" : "J. Matthews"
    },
    {
        "gameId" : "400791666",
        "team" : "Cincinnati",
        "opp" : "SD",
        "name" : "A.J. Green",
        "abbr" : "A. Green"
    },
    {
        "gameId" : "400791638",
        "team" : "Detroit",
        "opp" : "@MIN",
        "name" : "Calvin Johnson",
        "abbr" : "C. Johnson"
    },
    {
        "gameId" : "400791624",
        "team" : "Denver",
        "opp" : "@KC",
        "name" : "Demaryius Thomas",
        "abbr" : "D. Thomas"
    },
    {
        "gameId" : "400791634",
        "team" : "Tampa Bay",
        "opp" : "@NO",
        "name" : "Mike Evans",
        "abbr" : "M. Evans"
    },
    {
        "gameId" : "400791624",
        "team" : "Kansas City",
        "opp" : "DEN",
        "name" : "Jeremy Maclin",
        "abbr" : "J. Maclin"
    },
    {
        "gameId" : "400791661",
        "team" : "Chicago",
        "opp" : "ARI",
        "name" : "Alshon Jeffery",
        "abbr" : "A. Jeffery"
    },
    {
        "gameId" : "400791708",
        "team" : "Green Bay",
        "opp" : "SEA",
        "name" : "Randall Cobb",
        "abbr" : "R. Cobb"
    },
    {
        "gameId" : "400791624",
        "team" : "Denver",
        "opp" : "@KC",
        "name" : "Emmanuel Sanders",
        "abbr" : "E. Sanders"
    },
    {
        "gameId" : "400791628",
        "team" : "Houston",
        "opp" : "@OAK",
        "name" : "DeAndre Hopkins",
        "abbr" : "D. Hopkins"
    },
    {
        "gameId" : "400791711",
        "team" : "New York Jets",
        "opp" : "@IND",
        "name" : "Brandon Marshall",
        "abbr" : "B. Marshall"
    },
    {
        "gameId" : "400791669",
        "team" : "Tennessee",
        "opp" : "@CLE",
        "name" : "Kendall Wright",
        "abbr" : "K. Wright"
    },
    {
        "gameId" : "400791664",
        "team" : "Buffalo",
        "opp" : "NE",
        "name" : "Sammy Watkins",
        "abbr" : "S. Watkins"
    },
    {
        "gameId" : "400791638",
        "team" : "Detroit",
        "opp" : "@MIN",
        "name" : "Golden Tate",
        "abbr" : "G. Tate"
    },
    {
        "gameId" : "400791664",
        "team" : "New England",
        "opp" : "@BUF",
        "name" : "Julian Edelman",
        "abbr" : "J. Edelman"
    },
    {
        "gameId" : "400791666",
        "team" : "San Diego",
        "opp" : "@CIN",
        "name" : "Keenan Allen",
        "abbr" : "K. Allen"
    },
    {
        "gameId" : "400791634",
        "team" : "Tampa Bay",
        "opp" : "@NO",
        "name" : "Vincent Jackson",
        "abbr" : "V. Jackson"
    },
    {
        "gameId" : "400791638",
        "team" : "Minnesota",
        "opp" : "DET",
        "name" : "Mike Wallace",
        "abbr" : "M. Wallace"
    },
    {
        "gameId" : "400791708",
        "team" : "Green Bay",
        "opp" : "SEA",
        "name" : "Davante Adams",
        "abbr" : "D. Adams"
    },
    {
        "gameId" : "400791708",
        "team" : "Green Bay",
        "opp" : "SEA",
        "name" : "James Jones",
        "abbr" : "J. Jones"
    },
    {
        "gameId" : "400791680",
        "team" : "Miami",
        "opp" : "@JAC",
        "name" : "Jarvis Landry",
        "abbr" : "J. Landry"
    },
    {
        "gameId" : "400791680",
        "team" : "Jacksonville",
        "opp" : "MIA",
        "name" : "Allen Robinson",
        "abbr" : "A. Robinson"
    },
    {
        "gameId" : "400791638",
        "team" : "Minnesota",
        "opp" : "DET",
        "name" : "Charles Johnson",
        "abbr" : "C. Johnson"
    },
    {
        "gameId" : "400791702",
        "team" : "Oakland",
        "opp" : "BAL",
        "name" : "Amari Cooper",
        "abbr" : "A. Cooper"
    },
    {
        "gameId" : "400791702",
        "team" : "Baltimore",
        "opp" : "@OAK",
        "name" : "Steve Smith",
        "abbr" : "S. Smith"
    },
    {
        "gameId" : "400791711",
        "team" : "Indianapolis",
        "opp" : "NYJ",
        "name" : "Andre Johnson",
        "abbr" : "A. Johnson"
    },
    {
        "gameId" : "400791675",
        "team" : "Washington",
        "opp" : "STL",
        "name" : "Pierre Garcon",
        "abbr" : "P. Garcon"
    }
]
te1 = [
    {
        "gameId" : "400791664",
        "team" : "New England",
        "opp" : "@BUF",
        "name" : "Rob Gronkowski",
        "abbr" : "R. Gronkowski"
    },
    {
        "gameId" : "400791708",
        "team" : "Seattle",
        "opp" : "@GB",
        "name" : "Jimmy Graham",
        "abbr" : "J. Graham"
    },
    {
        "gameId" : "400791666",
        "team" : "Cincinnati",
        "opp" : "SD",
        "name" : "Tyler Eifert",
        "abbr" : "T. Eifert"
    },
    {
        "gameId" : "400791705",
        "team" : "Dallas",
        "opp" : "@PHI",
        "name" : "Jason Witten",
        "abbr" : "J. Witten"
    },
    {
        "gameId" : "400791624",
        "team" : "Kansas City",
        "opp" : "DEN",
        "name" : "Travis Kelce",
        "abbr" : "T. Kelce"
    },
    {
        "gameId" : "400791638",
        "team" : "Minnesota",
        "opp" : "DET",
        "name" : "Kyle Rudolph",
        "abbr" : "K. Rudolph"
    },
    {
        "gameId" : "400791634",
        "team" : "Tampa Bay",
        "opp" : "@NO",
        "name" : "Austin Seferian-Jenkins",
        "abbr" : "A. Seferian-Jenkins"
    },
    {
        "gameId" : "400791669",
        "team" : "Tennessee",
        "opp" : "@CLE",
        "name" : "Delanie Walker",
        "abbr" : "D. Walker"
    },
    {
        "gameId" : "400791711",
        "team" : "Indianapolis",
        "opp" : "NYJ",
        "name" : "Dwayne Allen",
        "abbr" : "D. Allen"
    },
    {
        "gameId" : "400791675",
        "team" : "St. Louis",
        "opp" : "@WSH",
        "name" : "Jared Cook",
        "abbr" : "J. Cook"
    },
    {
        "gameId" : "400791628",
        "team" : "Carolina",
        "opp" : "HOU",
        "name" : "Greg Olsen",
        "abbr" : "G. Olsen"
    },
    {
        "gameId" : "400791711",
        "team" : "Indianapolis",
        "opp" : "NYJ",
        "name" : "Coby Fleener",
        "abbr" : "C. Fleener"
    },
    {
        "gameId" : "400791661",
        "team" : "Chicago",
        "opp" : "ARI",
        "name" : "Martellus Bennett",
        "abbr" : "M. Bennett"
    },
    {
        "gameId" : "400791638",
        "team" : "Detroit",
        "opp" : "@MIN",
        "name" : "Eric Ebron",
        "abbr" : "E. Ebron"
    },
    {
        "gameId" : "400791705",
        "team" : "Philadelphia",
        "opp" : "DAL",
        "name" : "Zach Ertz",
        "abbr" : "Z. Ertz"
    },
    {
        "gameId" : "400791624",
        "team" : "Denver",
        "opp" : "@KC",
        "name" : "Owen Daniels",
        "abbr" : "O. Daniels"
    },
    {
        "gameId" : "400791680",
        "team" : "Jacksonville",
        "opp" : "MIA",
        "name" : "Julius Thomas",
        "abbr" : "J. Thomas"
    },
    {
        "gameId" : "400791630",
        "team" : "Pittsburgh",
        "opp" : "SF",
        "name" : "Heath Miller",
        "abbr" : "H. Miller"
    },
    {
        "gameId" : "400791672",
        "team" : "New York Giants",
        "opp" : "ATL",
        "name" : "Larry Donnell",
        "abbr" : "L. Donnell"
    },
    {
        "gameId" : "400791634",
        "team" : "New Orleans",
        "opp" : "TB",
        "name" : "Josh Hill",
        "abbr" : "J. Hill"
    },
    {
        "gameId" : "400791702",
        "team" : "Oakland",
        "opp" : "BAL",
        "name" : "Mychal Rivera",
        "abbr" : "M. Rivera"
    },
    {
        "gameId" : "400791630",
        "team" : "San Francisco",
        "opp" : "@PIT",
        "name" : "Vernon Davis",
        "abbr" : "V. Davis"
    },
    {
        "gameId" : "400791702",
        "team" : "Baltimore",
        "opp" : "@OAK",
        "name" : "Maxx Williams",
        "abbr" : "M. Williams"
    }
]
defst1 = [
    {
        "gameId" : "400791675",
        "opp" : "@WSH",
        "name" : "St. Louis",
        "abbr" : "STL"
    },
    {
        "gameId" : "400791680",
        "opp" : "@JAC",
        "name" : "Miami",
        "abbr" : "MIA"
    },
    {
        "gameId" : "400791628",
        "opp" : "@OAK",
        "name" : "Houston",
        "abbr" : "HOU"
    },
    {
        "gameId" : "400791624",
        "opp" : "DEN",
        "name" : "Kansas City",
        "abbr" : "KC"
    },
    {
        "gameId" : "400791638",
        "opp" : "DET",
        "name" : "Minnesota",
        "abbr" : "MIN"
    },
    {
        "gameId" : "400791705",
        "opp" : "DAL",
        "name" : "Philadelphia",
        "abbr" : "PHI"
    },
    {
        "gameId" : "400791708",
        "opp" : "SEA",
        "name" : "Green Bay",
        "abbr" : "GB"
    },
    {
        "gameId" : "400791711",
        "opp" : "@IND",
        "name" : "New York Jets",
        "abbr" : "NYJ"
    },
    {
        "gameId" : "400791708",
        "opp" : "@GB",
        "name" : "Seattle",
        "abbr" : "SEA"
    },
    {
        "gameId" : "400791638",
        "opp" : "@MIN",
        "name" : "Detroit",
        "abbr" : "DET"
    },
    {
        "gameId" : "400791702",
        "opp" : "@OAK",
        "name" : "Baltimore",
        "abbr" : "BAL"
    },
    {
        "gameId" : "400791661",
        "opp" : "@CHI",
        "name" : "Arizona",
        "abbr" : "ARI"
    },
    {
        "gameId" : "400791664",
        "opp" : "@BUF",
        "name" : "New England",
        "abbr" : "NE"
    },
    {
        "gameId" : "400791664",
        "opp" : "NE",
        "name" : "Buffalo",
        "abbr" : "BUF"
    },
    {
        "gameId" : "400791666",
        "opp" : "SD",
        "name" : "Cincinnati",
        "abbr" : "CIN"
    },
    {
        "gameId" : "400791705",
        "opp" : "@PHI",
        "name" : "Dallas",
        "abbr" : "DAL"
    },
    {
        "gameId" : "400791624",
        "opp" : "@KC",
        "name" : "Denver",
        "abbr" : "DEN"
    },
    {
        "gameId" : "400791666",
        "opp" : "@CIN",
        "name" : "San Diego",
        "abbr" : "SD"
    },
    {
        "gameId" : "400791628",
        "opp" : "HOU",
        "name" : "Carolina",
        "abbr" : "CAR"
    },
    {
        "gameId" : "400791634",
        "opp" : "@NO",
        "name" : "Tampa Bay",
        "abbr" : "TB"
    },
    {
        "gameId" : "400791630",
        "opp" : "SF",
        "name" : "Pittsburgh",
        "abbr" : "PIT"
    },
    {
        "gameId" : "400791669",
        "opp" : "TEN",
        "name" : "Cleveland",
        "abbr" : "CLE"
    },
    {
        "gameId" : "400791702",
        "opp" : "BAL",
        "name" : "Oakland",
        "abbr" : "OAK"
    },
    {
        "gameId" : "400791630",
        "opp" : "@PIT",
        "name" : "San Francisco",
        "abbr" : "SF"
    },
    {
        "gameId" : "400791711",
        "opp" : "NYJ",
        "name" : "Indianapolis",
        "abbr" : "IND"
    },
    {
        "gameId" : "400791672",
        "opp" : "@NYG",
        "name" : "Atlanta",
        "abbr" : "ATL"
    },
    {
        "gameId" : "400791680",
        "opp" : "MIA",
        "name" : "Jacksonville",
        "abbr" : "JAC"
    },
    {
        "gameId" : "400791672",
        "opp" : "ATL",
        "name" : "New York Giants",
        "abbr" : "NYG"
    },
    {
        "gameId" : "400791669",
        "opp" : "@CLE",
        "name" : "Tennessee",
        "abbr" : "TEN"
    },
    {
        "gameId" : "400791634",
        "opp" : "TB",
        "name" : "New Orleans",
        "abbr" : "NO"
    },
    {
        "gameId" : "400791675",
        "opp" : "STL",
        "name" : "Washington",
        "abbr" : "WSH"
    },
    {
        "gameId" : "400791661",
        "opp" : "ARI",
        "name" : "Chicago",
        "abbr" : "CHI"
    }
]
qb2 = [
    {
        "gameId" : "400791634",
        "team" : "New Orleans",
        "opp" : "TB",
        "name" : "Drew Brees",
        "abbr" : "D. Brees"
    },
    {
        "gameId" : "400791708",
        "team" : "Green Bay",
        "opp" : "SEA",
        "name" : "Aaron Rodgers",
        "abbr" : "A. Rodgers"
    },
    {
        "gameId" : "400791711",
        "team" : "Indianapolis",
        "opp" : "NYJ",
        "name" : "Andrew Luck",
        "abbr" : "A. Luck"
    },
    {
        "gameId" : "400791672",
        "team" : "Atlanta",
        "opp" : "@NYG",
        "name" : "Matt Ryan",
        "abbr" : "M. Ryan"
    },
    {
        "gameId" : "400791708",
        "team" : "Seattle",
        "opp" : "@GB",
        "name" : "Russell Wilson",
        "abbr" : "R. Wilson"
    },
    {
        "gameId" : "400791661",
        "team" : "Arizona",
        "opp" : "@CHI",
        "name" : "Carson Palmer",
        "abbr" : "C. Palmer"
    },
    {
        "gameId" : "400791630",
        "team" : "Pittsburgh",
        "opp" : "SF",
        "name" : "Ben Roethlisberger",
        "abbr" : "B. Roethlisberger"
    },
    {
        "gameId" : "400791705",
        "team" : "Dallas",
        "opp" : "@PHI",
        "name" : "Tony Romo",
        "abbr" : "T. Romo"
    },
    {
        "gameId" : "400791672",
        "team" : "New York Giants",
        "opp" : "ATL",
        "name" : "Eli Manning",
        "abbr" : "E. Manning"
    },
    {
        "gameId" : "400791705",
        "team" : "Philadelphia",
        "opp" : "DAL",
        "name" : "Sam Bradford",
        "abbr" : "S. Bradford"
    },
    {
        "gameId" : "400791624",
        "team" : "Denver",
        "opp" : "@KC",
        "name" : "Peyton Manning",
        "abbr" : "P. Manning"
    },
    {
        "gameId" : "400791638",
        "team" : "Detroit",
        "opp" : "@MIN",
        "name" : "Matthew Stafford",
        "abbr" : "M. Stafford"
    },
    {
        "gameId" : "400791664",
        "team" : "New England",
        "opp" : "@BUF",
        "name" : "Tom Brady",
        "abbr" : "T. Brady"
    },
    {
        "gameId" : "400791628",
        "team" : "Carolina",
        "opp" : "HOU",
        "name" : "Cam Newton",
        "abbr" : "C. Newton"
    },
    {
        "gameId" : "400791666",
        "team" : "San Diego",
        "opp" : "@CIN",
        "name" : "Phillip Rivers",
        "abbr" : "P. Rivers"
    },
    {
        "gameId" : "400791669",
        "team" : "Cleveland",
        "opp" : "TEN",
        "name" : "Johnny Manziel",
        "abbr" : "J. Manziel"
    },
    {
        "gameId" : "400791661",
        "team" : "Chicago",
        "opp" : "ARI",
        "name" : "Jay Cutler",
        "abbr" : "J. Cutler"
    },
    {
        "gameId" : "400791666",
        "team" : "Cincinnati",
        "opp" : "SD",
        "name" : "Andy Dalton",
        "abbr" : "A. Dalton"
    },
    {
        "gameId" : "400791675",
        "team" : "St. Louis",
        "opp" : "@WSH",
        "name" : "Nick Foles",
        "abbr" : "N. Foles"
    },
    {
        "gameId" : "400791638",
        "team" : "Minnesota",
        "opp" : "DET",
        "name" : "Teddy Bridgewater",
        "abbr" : "T. Bridgewater"
    },
    {
        "gameId" : "400791680",
        "team" : "Miami",
        "opp" : "@JAC",
        "name" : "Ryan Tannehill",
        "abbr" : "R. Tannehill"
    },
    {
        "gameId" : "400791702",
        "team" : "Oakland",
        "opp" : "BAL",
        "name" : "Derek Carr",
        "abbr" : "D. Carr"
    },
    {
        "gameId" : "400791680",
        "team" : "Jacksonville",
        "opp" : "MIA",
        "name" : "Blake Bortles",
        "abbr" : "B. Bortles"
    },
    {
        "gameId" : "400791669",
        "team" : "Tennessee",
        "opp" : "@CLE",
        "name" : "Marcus Mariota",
        "abbr" : "M. Mariota"
    },
    {
        "gameId" : "400791711",
        "team" : "New York Jets",
        "opp" : "@IND",
        "name" : "Ryan Fitzpatrick",
        "abbr" : "R. Fitzpatrick"
    },
    {
        "gameId" : "400791634",
        "team" : "Tampa Bay",
        "opp" : "@NO",
        "name" : "Jameis Winston",
        "abbr" : "J. Winston"
    }
]
rb2 = [
    {
        "gameId" : "400791708",
        "team" : "Seattle",
        "opp" : "@GB",
        "name" : "Marshawn Lynch",
        "abbr" : "M. Lynch"
    },
    {
        "gameId" : "400791638",
        "team" : "Minnesota",
        "opp" : "DET",
        "name" : "Adrian Peterson",
        "abbr" : "A. Peterson"
    },
    {
        "gameId" : "400791666",
        "team" : "Cincinnati",
        "opp" : "SD",
        "name" : "Jeremy Hill",
        "abbr" : "J. Hill"
    },
    {
        "gameId" : "400791624",
        "team" : "Kansas City",
        "opp" : "DEN",
        "name" : "Jamaal Charles",
        "abbr" : "J. Charles"
    },
    {
        "gameId" : "400791661",
        "team" : "Chicago",
        "opp" : "ARI",
        "name" : "Matt Forte",
        "abbr" : "M. Forte"
    },
    {
        "gameId" : "400791711",
        "team" : "New York Jets",
        "opp" : "@IND",
        "name" : "Chris Ivory",
        "abbr" : "C. Ivory"
    },
    {
        "gameId" : "400791708",
        "team" : "Green Bay",
        "opp" : "SEA",
        "name" : "Eddie Lacy",
        "abbr" : "E. Lacy"
    },
    {
        "gameId" : "400791705",
        "team" : "Philadelphia",
        "opp" : "DAL",
        "name" : "DeMarco Murray",
        "abbr" : "D. Murray"
    },
    {
        "gameId" : "400791664",
        "team" : "Buffalo",
        "opp" : "NE",
        "name" : "LeSean McCoy",
        "abbr" : "L. McCoy"
    },
    {
        "gameId" : "400791634",
        "team" : "New Orleans",
        "opp" : "TB",
        "name" : "Mark Ingram",
        "abbr" : "M. Ingram"
    },
    {
        "gameId" : "400791702",
        "team" : "Baltimore",
        "opp" : "@OAK",
        "name" : "Justin Forsett",
        "abbr" : "J. Forsett"
    },
    {
        "gameId" : "400791624",
        "team" : "Denver",
        "opp" : "@KC",
        "name" : "C.J. Anderson",
        "abbr" : "C. Anderson"
    },
    {
        "gameId" : "400791638",
        "team" : "Detroit",
        "opp" : "@MIN",
        "name" : "Joique Bell",
        "abbr" : "J. Bell"
    },
    {
        "gameId" : "400791630",
        "team" : "San Francisco",
        "opp" : "@PIT",
        "name" : "Carlos Hyde",
        "abbr" : "C. Hyde"
    },
    {
        "gameId" : "400791705",
        "team" : "Dallas",
        "opp" : "@PHI",
        "name" : "Joseph Randle",
        "abbr" : "J. Randle"
    },
    {
        "gameId" : "400791680",
        "team" : "Miami",
        "opp" : "@JAC",
        "name" : "Lamar Miller",
        "abbr" : "L. Miller"
    },
    {
        "gameId" : "400791711",
        "team" : "Indianapolis",
        "opp" : "NYJ",
        "name" : "Frank Gore",
        "abbr" : "F. Gore"
    },
    {
        "gameId" : "400791661",
        "team" : "Arizona",
        "opp" : "@CHI",
        "name" : "Andre Ellington",
        "abbr" : "A. Ellington"
    },
    {
        "gameId" : "400791675",
        "team" : "Washington",
        "opp" : "STL",
        "name" : "Alfred Morris",
        "abbr" : "A. Morris"
    },
    {
        "gameId" : "400791702",
        "team" : "Oakland",
        "opp" : "BAL",
        "name" : "Latavius Murray",
        "abbr" : "L. Murray"
    },
    {
        "gameId" : "400791628",
        "team" : "Carolina",
        "opp" : "HOU",
        "name" : "Jonathan Stewart",
        "abbr" : "J. Stewart"
    },
    {
        "gameId" : "400791666",
        "team" : "San Diego",
        "opp" : "@CIN",
        "name" : "Melvin Gordon",
        "abbr" : "M. Gordon"
    },
    {
        "gameId" : "400791680",
        "team" : "Jacksonville",
        "opp" : "MIA",
        "name" : "T.J. Yeldon",
        "abbr" : "T. Yeldon"
    },
    {
        "gameId" : "400791628",
        "team" : "Houston",
        "opp" : "@OAK",
        "name" : "Alred Blue",
        "abbr" : "A. Blue"
    },
    {
        "gameId" : "400791669",
        "team" : "Cleveland",
        "opp" : "TEN",
        "name" : "Isaiah Crowell",
        "abbr" : "I. Crowell"
    },
    {
        "gameId" : "400791672",
        "team" : "New York Giants",
        "opp" : "ATL",
        "name" : "Rashad Jennings",
        "abbr" : "R. Jennings"
    },
    {
        "gameId" : "400791666",
        "team" : "Cincinnati",
        "opp" : "SD",
        "name" : "Giovani Bernard",
        "abbr" : "G. Bernard"
    },
    {
        "gameId" : "400791669",
        "team" : "Tennessee",
        "opp" : "@CLE",
        "name" : "Bishop Sankey",
        "abbr" : "B. Sankey"
    }
]
wr2 = [
    {
        "gameId" : "400791630",
        "team" : "Pittsburgh",
        "opp" : "SF",
        "name" : "Antonio Brown",
        "abbr" : "A. Brown"
    },
    {
        "gameId" : "400791672",
        "team" : "Atlanta",
        "opp" : "@NYG",
        "name" : "Julio Jones",
        "abbr" : "J. Jones"
    },
    {
        "gameId" : "400791672",
        "team" : "New York Giants",
        "opp" : "ATL",
        "name" : "Odell Beckham",
        "abbr" : "O. Beckham Jr."
    },
    {
        "gameId" : "400791705",
        "team" : "Philadelphia",
        "opp" : "DAL",
        "name" : "Jordan Matthews",
        "abbr" : "J. Matthews"
    },
    {
        "gameId" : "400791634",
        "team" : "New Orleans",
        "opp" : "TB",
        "name" : "Brandin Cooks",
        "abbr" : "B. Cooks"
    },
    {
        "gameId" : "400791634",
        "team" : "Tampa Bay",
        "opp" : "@NO",
        "name" : "Mike Evans",
        "abbr" : "M. Evans"
    },
    {
        "gameId" : "400791638",
        "team" : "Detroit",
        "opp" : "@MIN",
        "name" : "Calvin Johnson",
        "abbr" : "C. Johnson"
    },
    {
        "gameId" : "400791666",
        "team" : "Cincinnati",
        "opp" : "SD",
        "name" : "A.J. Green",
        "abbr" : "A. Green"
    },
    {
        "gameId" : "400791628",
        "team" : "Houston",
        "opp" : "@OAK",
        "name" : "DeAndre Hopkins",
        "abbr" : "D. Hopkins"
    },
    {
        "gameId" : "400791666",
        "team" : "San Diego",
        "opp" : "@CIN",
        "name" : "Keenan Allen",
        "abbr" : "K. Allen"
    },
    {
        "gameId" : "400791680",
        "team" : "Miami",
        "opp" : "@JAC",
        "name" : "Jarvis Landry",
        "abbr" : "J. Landry"
    },
    {
        "gameId" : "400791708",
        "team" : "Green Bay",
        "opp" : "SEA",
        "name" : "Randall Cobb",
        "abbr" : "R. Cobb"
    },
    {
        "gameId" : "400791624",
        "team" : "Kansas City",
        "opp" : "DEN",
        "name" : "Jeremy Maclin",
        "abbr" : "J. Maclin"
    },
    {
        "gameId" : "400791661",
        "team" : "Chicago",
        "opp" : "ARI",
        "name" : "Alshon Jeffery",
        "abbr" : "A. Jeffery"
    },
    {
        "gameId" : "400791624",
        "team" : "Denver",
        "opp" : "@KC",
        "name" : "Demaryius Thomas",
        "abbr" : "D. Thomas"
    },
    {
        "gameId" : "400791624",
        "team" : "Denver",
        "opp" : "@KC",
        "name" : "Emmanuel Sanders",
        "abbr" : "E. Sanders"
    },
    {
        "gameId" : "400791711",
        "team" : "New York Jets",
        "opp" : "@IND",
        "name" : "Brandon Marshall",
        "abbr" : "B. Marshall"
    },
    {
        "gameId" : "400791669",
        "team" : "Tennessee",
        "opp" : "@CLE",
        "name" : "Kendall Wright",
        "abbr" : "K. Wright"
    },
    {
        "gameId" : "400791664",
        "team" : "Buffalo",
        "opp" : "NE",
        "name" : "Sammy Watkins",
        "abbr" : "S. Watkins"
    },
    {
        "gameId" : "400791638",
        "team" : "Detroit",
        "opp" : "@MIN",
        "name" : "Golden Tate",
        "abbr" : "G. Tate"
    },
    {
        "gameId" : "400791664",
        "team" : "New England",
        "opp" : "@BUF",
        "name" : "Julian Edelman",
        "abbr" : "J. Edelman"
    },
    {
        "gameId" : "400791634",
        "team" : "Tampa Bay",
        "opp" : "@NO",
        "name" : "Vincent Jackson",
        "abbr" : "V. Jackson"
    },
    {
        "gameId" : "400791638",
        "team" : "Minnesota",
        "opp" : "DET",
        "name" : "Mike Wallace",
        "abbr" : "M. Wallace"
    },
    {
        "gameId" : "400791708",
        "team" : "Green Bay",
        "opp" : "SEA",
        "name" : "Davante Adams",
        "abbr" : "D. Adams"
    },
    {
        "gameId" : "400791708",
        "team" : "Green Bay",
        "opp" : "SEA",
        "name" : "James Jones",
        "abbr" : "J. Jones"
    },
    {
        "gameId" : "400791680",
        "team" : "Jacksonville",
        "opp" : "MIA",
        "name" : "Allen Robinson",
        "abbr" : "A. Robinson"
    },
    {
        "gameId" : "400791638",
        "team" : "Minnesota",
        "opp" : "DET",
        "name" : "Charles Johnson",
        "abbr" : "C. Johnson"
    },
    {
        "gameId" : "400791702",
        "team" : "Oakland",
        "opp" : "BAL",
        "name" : "Amari Cooper",
        "abbr" : "A. Cooper"
    },
    {
        "gameId" : "400791702",
        "team" : "Baltimore",
        "opp" : "@OAK",
        "name" : "Steve Smith",
        "abbr" : "S. Smith"
    },
    {
        "gameId" : "400791711",
        "team" : "Indianapolis",
        "opp" : "NYJ",
        "name" : "Andre Johnson",
        "abbr" : "A. Johnson"
    },
    {
        "gameId" : "400791675",
        "team" : "Washington",
        "opp" : "STL",
        "name" : "Pierre Garcon",
        "abbr" : "P. Garcon"
    }
]
te2 = [
    {
        "gameId" : "400791664",
        "team" : "New England",
        "opp" : "@BUF",
        "name" : "Rob Gronkowski",
        "abbr" : "R. Gronkowski"
    },
    {
        "gameId" : "400791708",
        "team" : "Seattle",
        "opp" : "@GB",
        "name" : "Jimmy Graham",
        "abbr" : "J. Graham"
    },
    {
        "gameId" : "400791666",
        "team" : "Cincinnati",
        "opp" : "SD",
        "name" : "Tyler Eifert",
        "abbr" : "T. Eifert"
    },
    {
        "gameId" : "400791624",
        "team" : "Kansas City",
        "opp" : "DEN",
        "name" : "Travis Kelce",
        "abbr" : "T. Kelce"
    },
    {
        "gameId" : "400791705",
        "team" : "Dallas",
        "opp" : "@PHI",
        "name" : "Jason Witten",
        "abbr" : "J. Witten"
    },
    {
        "gameId" : "400791628",
        "team" : "Carolina",
        "opp" : "HOU",
        "name" : "Greg Olsen",
        "abbr" : "G. Olsen"
    },
    {
        "gameId" : "400791661",
        "team" : "Chicago",
        "opp" : "ARI",
        "name" : "Martellus Bennett",
        "abbr" : "M. Bennett"
    },
    {
        "gameId" : "400791638",
        "team" : "Minnesota",
        "opp" : "DET",
        "name" : "Kyle Rudolph",
        "abbr" : "K. Rudolph"
    },
    {
        "gameId" : "400791634",
        "team" : "Tampa Bay",
        "opp" : "@NO",
        "name" : "Austin Seferian-Jenkins",
        "abbr" : "A. Seferian-Jenkins"
    },
    {
        "gameId" : "400791680",
        "team" : "Jacksonville",
        "opp" : "MIA",
        "name" : "Julius Thomas",
        "abbr" : "J. Thomas"
    },
    {
        "gameId" : "400791711",
        "team" : "Indianapolis",
        "opp" : "NYJ",
        "name" : "Dwayne Allen",
        "abbr" : "D. Allen"
    },
    {
        "gameId" : "400791669",
        "team" : "Tennessee",
        "opp" : "@CLE",
        "name" : "Delanie Walker",
        "abbr" : "D. Walker"
    },
    {
        "gameId" : "400791711",
        "team" : "Indianapolis",
        "opp" : "NYJ",
        "name" : "Coby Fleener",
        "abbr" : "C. Fleener"
    },
    {
        "gameId" : "400791638",
        "team" : "Detroit",
        "opp" : "@MIN",
        "name" : "Eric Ebron",
        "abbr" : "E. Ebron"
    },
    {
        "gameId" : "400791705",
        "team" : "Philadelphia",
        "opp" : "DAL",
        "name" : "Zach Ertz",
        "abbr" : "Z. Ertz"
    },
    {
        "gameId" : "400791624",
        "team" : "Denver",
        "opp" : "@KC",
        "name" : "Owen Daniels",
        "abbr" : "O. Daniels"
    },
    {
        "gameId" : "400791675",
        "team" : "St. Louis",
        "opp" : "@WSH",
        "name" : "Jared Cook",
        "abbr" : "J. Cook"
    },
    {
        "gameId" : "400791630",
        "team" : "Pittsburgh",
        "opp" : "SF",
        "name" : "Heath Miller",
        "abbr" : "H. Miller"
    },
    {
        "gameId" : "400791672",
        "team" : "New York Giants",
        "opp" : "ATL",
        "name" : "Larry Donnell",
        "abbr" : "L. Donnell"
    },
    {
        "gameId" : "400791634",
        "team" : "New Orleans",
        "opp" : "TB",
        "name" : "Josh Hill",
        "abbr" : "J. Hill"
    },
    {
        "gameId" : "400791702",
        "team" : "Oakland",
        "opp" : "BAL",
        "name" : "Mychal Rivera",
        "abbr" : "M. Rivera"
    },
    {
        "gameId" : "400791630",
        "team" : "San Francisco",
        "opp" : "@PIT",
        "name" : "Vernon Davis",
        "abbr" : "V. Davis"
    },
    {
        "gameId" : "400791702",
        "team" : "Baltimore",
        "opp" : "@OAK",
        "name" : "Maxx Williams",
        "abbr" : "M. Williams"
    }
]
defst2 = [
    {
        "gameId" : "400791675",
        "opp" : "@WSH",
        "name" : "St. Louis",
        "abbr" : "STL"
    },
    {
        "gameId" : "400791680",
        "opp" : "@JAC",
        "name" : "Miami",
        "abbr" : "MIA"
    },
    {
        "gameId" : "400791702",
        "opp" : "@OAK",
        "name" : "Baltimore",
        "abbr" : "BAL"
    },
    {
        "gameId" : "400791624",
        "opp" : "DEN",
        "name" : "Kansas City",
        "abbr" : "KC"
    },
    {
        "gameId" : "400791664",
        "opp" : "NE",
        "name" : "Buffalo",
        "abbr" : "BUF"
    },
    {
        "gameId" : "400791664",
        "opp" : "@BUF",
        "name" : "New England",
        "abbr" : "NE"
    },
    {
        "gameId" : "400791708",
        "opp" : "@GB",
        "name" : "Seattle",
        "abbr" : "SEA"
    },
    {
        "gameId" : "400791628",
        "opp" : "@OAK",
        "name" : "Houston",
        "abbr" : "HOU"
    },
    {
        "gameId" : "400791705",
        "opp" : "DAL",
        "name" : "Philadelphia",
        "abbr" : "PHI"
    },
    {
        "gameId" : "400791638",
        "opp" : "DET",
        "name" : "Minnesota",
        "abbr" : "MIN"
    },
    {
        "gameId" : "400791708",
        "opp" : "SEA",
        "name" : "Green Bay",
        "abbr" : "GB"
    },
    {
        "gameId" : "400791711",
        "opp" : "@IND",
        "name" : "New York Jets",
        "abbr" : "NYJ"
    },
    {
        "gameId" : "400791638",
        "opp" : "@MIN",
        "name" : "Detroit",
        "abbr" : "DET"
    },
    {
        "gameId" : "400791661",
        "opp" : "@CHI",
        "name" : "Arizona",
        "abbr" : "ARI"
    },
    {
        "gameId" : "400791666",
        "opp" : "SD",
        "name" : "Cincinnati",
        "abbr" : "CIN"
    },
    {
        "gameId" : "400791705",
        "opp" : "@PHI",
        "name" : "Dallas",
        "abbr" : "DAL"
    },
    {
        "gameId" : "400791624",
        "opp" : "@KC",
        "name" : "Denver",
        "abbr" : "DEN"
    },
    {
        "gameId" : "400791666",
        "opp" : "@CIN",
        "name" : "San Diego",
        "abbr" : "SD"
    },
    {
        "gameId" : "400791628",
        "opp" : "HOU",
        "name" : "Carolina",
        "abbr" : "CAR"
    },
    {
        "gameId" : "400791634",
        "opp" : "@NO",
        "name" : "Tampa Bay",
        "abbr" : "TB"
    },
    {
        "gameId" : "400791630",
        "opp" : "SF",
        "name" : "Pittsburgh",
        "abbr" : "PIT"
    },
    {
        "gameId" : "400791669",
        "opp" : "TEN",
        "name" : "Cleveland",
        "abbr" : "CLE"
    },
    {
        "gameId" : "400791702",
        "opp" : "BAL",
        "name" : "Oakland",
        "abbr" : "OAK"
    },
    {
        "gameId" : "400791630",
        "opp" : "@PIT",
        "name" : "San Francisco",
        "abbr" : "SF"
    },
    {
        "gameId" : "400791711",
        "opp" : "NYJ",
        "name" : "Indianapolis",
        "abbr" : "IND"
    },
    {
        "gameId" : "400791672",
        "opp" : "@NYG",
        "name" : "Atlanta",
        "abbr" : "ATL"
    },
    {
        "gameId" : "400791680",
        "opp" : "MIA",
        "name" : "Jacksonville",
        "abbr" : "JAC"
    },
    {
        "gameId" : "400791672",
        "opp" : "ATL",
        "name" : "New York Giants",
        "abbr" : "NYG"
    },
    {
        "gameId" : "400791669",
        "opp" : "@CLE",
        "name" : "Tennessee",
        "abbr" : "TEN"
    },
    {
        "gameId" : "400791634",
        "opp" : "TB",
        "name" : "New Orleans",
        "abbr" : "NO"
    },
    {
        "gameId" : "400791675",
        "opp" : "STL",
        "name" : "Washington",
        "abbr" : "WSH"
    },
    {
        "gameId" : "400791661",
        "opp" : "ARI",
        "name" : "Chicago",
        "abbr" : "CHI"
    }
]

#check to see if both rankings have exact rankings for a position
if qb1 == qb2 or rb1 == rb2 or wr1 == wr2 or te1 == te2 or defst1 == defst2:
	#pass and go to next user
	print False
else:
	#final team objects
	team1 = {'qb':[],'rb':[],'wr':[],'te':[],'defst':[]}
	team2 = {'qb':[],'rb':[],'wr':[],'te':[],'defst':[]}

	while len(team1['qb']) == 0 and len(team2['qb']) == 0:
		if qb1[0] != qb2[0]:
			team1['qb'].append(qb1[0])
			team2['qb'].append(qb2[0])
		else:
			del qb1[0]
			del qb2[0]

	while len(team1['rb']) == 0 and len(team2['rb']) == 0:
		if rb1[0] != rb2[0]:
			team1['rb'].append(rb1[0])
			team2['rb'].append(rb2[0])
			if team1['rb'][0] in rb2:
				rb2.remove(team1['rb'][0])
			if team2['rb'][0] in rb1:
				rb1.remove(team2['rb'][0])
			del rb1[0]
			del rb2[0]
			while len(team1['rb']) == 1 and len(team2['rb']) == 1:
				if rb1 == [] or rb2 == []:
					print False
				elif rb1[0] != rb2[0]:
					team1['rb'].append(rb1[0])
					team2['rb'].append(rb2[0])
				else:
					del rb1[0]
					del rb2[0]
		else:
			del rb1[0]
			del rb2[0]

	while len(team1['wr']) == 0 and len(team2['wr']) == 0:
		if wr1[0] != wr2[0]:
			team1['wr'].append(wr1[0])
			team2['wr'].append(wr2[0])
			if team1['wr'][0] in wr2:
				wr2.remove(team1['wr'][0])
			if team2['wr'][0] in wr1:
				wr1.remove(team2['wr'][0])
			del wr1[0]
			del wr2[0]
			while len(team1['wr']) == 1 and len(team2['wr']) == 1:
				if wr1 == [] or wr2 == []:
					print False
				elif wr1[0] != wr2[0]:
					team1['wr'].append(wr1[0])
					team2['wr'].append(wr2[0])
				else:
					del wr1[0]
					del wr2[0]
		else:
			del wr1[0]
			del wr2[0]


	while len(team1['te']) == 0 and len(team2['te']) == 0:
		if te1[0] != te2[0]:
			team1['te'].append(te1[0])
			team2['te'].append(te2[0])
		else:
			del te1[0]
			del te2[0]

	while len(team1['defst']) == 0 and len(team2['defst']) == 0:
		if defst1[0] != defst2[0]:
			team1['defst'].append(defst1[0])
			team2['defst'].append(defst2[0])
		else:
			del defst1[0]
			del defst2[0]

	print team1
	print '\n'
	print team2