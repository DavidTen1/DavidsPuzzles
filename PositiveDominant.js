
function positiveDominant(numsArray){
  const nonNumber = numsArray.find((element) => isNaN(element)); // check if an element in array is no number
  // is the non-number element also of another type that is neither null nor undefined
  const haveWeGotNonNumber =   (isNaN(nonNumber) && nonNumber !== null && nonNumber !== undefined) || numsArray.includes(undefined) || numsArray.includes(null);

  // in order to reject the array that has not only numbers, the program's terminated
  if ( haveWeGotNonNumber ){
    console.log('It is no number array, function aborted');
    return;
  }

  const positives = numsArray.filter((target) => target > 0 ); // count of positive numbers

  const negatives = numsArray.filter((target) => target < 0 ); // count of negative numbers

  console.log('pos', positives,'neg', negatives);

  return positives.length > negatives.length;
}

positiveDominant([3,4,-1,-1,-1]);
