const lastYearsMatches = {
	rachel: "jeri",
  glenn: "dave",
  jeri: "lauren",
  dave: "rachel",
  lauren: "glenn"
}; // last years matches
const players = ['rachel', 'glenn', 'jeri', 'dave', 'lauren']; // new player inputs
const shuffled = shuffle(players, lastYearsMatches, 0);
console.log({shuffled});

// lastYearMatches is optional
function shuffle (players, lastYearsMatches = [], counter) {
	counter++; // debug for number of iterations
  const shuffled = _.shuffle(players); // shuffles players list using Fisher-Yates shuffle
  const combined = _.zipObject(players, shuffled); // combines two arrays into key: match pairs

  // .every returns a single truthy value for every iteration
	const passMatchRequirements = _.every(combined, function(key, value) {
    const notSelfMatch = key !== value; // check we didn't match ourself
    const notLastYearMatch = lastYearsMatches[key] !== value; // check we didn't match last year

    return notSelfMatch && notLastYearMatch;
  });

  if (passMatchRequirements) {
  	console.log('final iterations: ' + counter); // debug
  	return combined; // return our list new verified matches
  } else {
  	return shuffle(players, lastYearsMatches, counter); // recursivly call this function if we didn't pass .every until we do
  }
}