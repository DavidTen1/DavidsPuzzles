/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */


// here you mark all matrix elements containing zeroes by saving row and column indexes
var setZeroes = function(matrix) {
    let zeroesCoordinates = [];
    for(let i = 0; i < matrix.length;i++){
      for(let j = 0; j < matrix[i].length;j++){
        if(matrix[i][j] == 0){
        zeroesCoordinates.push([i,j]);
        }
    } 
    }
    // turn all rows with >= 1 zero to zeroed-rows and columns that have the same column indexes
    for(const pos of zeroesCoordinates){
         let rowIndex = pos[0];
       let columnIndex = pos[1];
      for(let i = 0; i < matrix.length;i++){
       matrix[i][columnIndex] = 0;
      }
       matrix[rowIndex] =  matrix[rowIndex].fill(0);
    }
};