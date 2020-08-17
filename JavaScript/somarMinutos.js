/*
Crie um algoritimo capaz de somar minutos a um horario.
--Objetivo---
Crie uma função com dois parâmetros de entrada:

--Horas (?string no formato "hh:mm");
--MinutosAcrescimo (número inteiro);

A sua função deverá acrescentar o minutos ao horário recebido, respeitando o padrão 24h,
e retornará uma string representando o horário resultante.

importante:

Não serão consideradas soluções baseadads em utilitarios de data da linguagem escolhidad

EXEMPLOS

--Para a entrada hora="11:10" e minutos = 20 temos a saída "11:30"
--Para a entrada hora="13:41" e minutos = 36 temos a saída "14:17"

*/
var minutosAcrescimo = 30;
var horas = "11:30";  

function convertHoursToMinutes(time) {
    let [hour, minutes] = time.split(":")
        return Number ((hour * 60) + parseInt(minutes) + parseInt(minutosAcrescimo))

}

var totalMinutos = convertHoursToMinutes (horas);

function convertMinutesToHours(minutos){
    let hour = minutos / 60;
    let minutes =  minutos % 60;
        return ( hour + ":" + minutes)
}

var resultado = convertMinutesToHours(totalMinutos)

console.log (resultado);
/*
function convertHourToMinutes(time) {
    const hour = time.split(":")[0]
    const minutes = time.split(':')[1]
}
var minutosAcrescimo = 30;
var Horas = "11:30";
var resultado = convertHoursToMinutes (11:10);

*/