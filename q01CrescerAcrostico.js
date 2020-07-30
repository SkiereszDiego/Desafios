/* 
Crie um algoritimo que recebe uma frase (string) e retorna uma nova palavra
formada pela união das iniciais de cada palavra desta frase, como no exemplo:
frase="Comprei rapadura e salsa com entusiasmo rarissimo" retorna "Crescer"
*/
var a = "Comprei rapadura e salsa com entusiasmo raríssimo";

function solucao(frase) {
    var resposta = "";
    let splitFrase = frase.split(' ');
    for (var i = 0; i < splitFrase.length; i++) {
        resposta += splitFrase[i][0];
    }
    return resposta;
} 


console.log(solucao(a));