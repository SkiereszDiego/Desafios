/*
Return the factorial of the provided integer
if the integer is erpresented with the letter n, 
a facotiral is the product of all positive integers less than or equal to n

Factorials are ofthen represented with the shorthand notation n!

remember to use Read-Search-Ask


windows.alert('msg')
windows.confirm('sim ou nao')
windows.prompt('Qua é seu nome')

Terminal crtl+shift+crase

Para entrar no node, digite node e para sair .exit

*/


function factorialize (num) {
    var result = 1;
    for (var i=1; i<=num; i++) {
        //result = result * i;
        result *=i;
    }
    return result;
    
}

console.log(factorialize (5))