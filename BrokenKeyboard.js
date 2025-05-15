
// image a string is given and a character can't be typed because the key is broken, so you find out how many words you can write at best without the aforementioned character
function brokenKey(string,character){
  if(character.length > 1 || !(string instanceof  String )  || !(character instanceof  String )){
    return;
  }
  // split spring into words that are separated by the space
  const allWordsInString = string.split(' ');
  //maximum count of words writable without the unavailable character
  let maxWords = 0;

  //check for each word if the broken character is inside, if not, you have found a word that you can write without it
  for (const word in allWordsInString){
    maxWords = !(word.includes(p)) ? maxWords + 1: maxWords;
  }
  // return maximum count of words writable without the unavailable character
return maxWords;
}

// console.log("mw", brokenKey("javascript is great","p"));
