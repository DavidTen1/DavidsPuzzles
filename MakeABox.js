function makeABox(n){
  // an array containing an n x n box
const boxArray = [];
for(let i = 0 ; i < n;i++){
// row that is a buiding part of a box
  const boxRow = [];
  for(let j = 0 ; j < n;j++){
    //if you're on a box edge, use # otherwise ' ' as box space
    let boxValue = (i === 0 || i === n-1) ||  (j === 0 || j === n-1) ? '#': ' ';
    // push either # or a space as value in an array
    boxRow.push(boxValue);
  }
  // create box with a row array which contributes to a box-like output later on
  boxArray.push(boxRow);
}

return boxArray;
}

console.log('box array', makeABox(6));
