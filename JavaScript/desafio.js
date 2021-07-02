// Funcao que recebe uma integral e retorna um numero em bits que e igual a um in binario. 
// Garantir que o input nao seja negativo.
var countBits = function(n) {
  // make an array with the bit result
  const base = (n).toString(2).split('');
  
  // make a sum with the array and make the index a Number
  const result = base.reduce((sum, num) => sum + Number(num), 0);
  
  return result;
};